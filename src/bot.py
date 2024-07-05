import os
import asyncio
import datetime
import traceback
import contextlib
import aiohttp
import discohook
from starlette.responses import JSONResponse
from .cogs.ping import ping_command

def run():

  # Lifespan to gracefully shutdown, which only happens during local testing
  # This can also be used to setup .session and .db attributes
  @contextlib.asynccontextmanager
  async def lifespan(app):
    await app.http.session.close() # close bot session
    app.http.session = aiohttp.ClientSession('https://discord.com', loop = asyncio.get_running_loop()) # create session on current event loop
    app.start_lifespan = '{}-{}'.format(datetime.datetime.utcnow(), id(asyncio.get_running_loop()))
    try:
      yield
    except asyncio.CancelledError:
      print('Ignoring cancelled error.')
    else:
      print('Closed without errors.')
    finally:
      app.stop_lifespan = '{}-{}'.format(datetime.datetime.utcnow(), id(asyncio.get_running_loop()))
      await app.http.session.close() # close bot session

  # Define the bot
  app = discohook.Client(
    application_id = os.getenv('DISCORD_APPLICATION_ID'),
    public_key = os.getenv('DISCORD_PUBLIC_KEY'),
    token = os.getenv('DISCORD_BOT_TOKEN'),
    password = os.getenv('SYNC_PASSWORD'),
    lifespan = lifespan
  )

  # Attach error handler
  app.errors = []
  error_log_webhook = discohook.PartialWebhook.from_url(app, os.getenv('ERROR_LOG_WEBHOOK'))
  @app.on_interaction_error()
  async def on_error(interaction, error):
    trace = tuple(traceback.TracebackException.from_exception(error).format())
    app.errors.append(trace)
    text = ''.join(trace)
    print(text)
    if interaction.responded:
      await interaction.response.followup('Sorry, an error has occurred (after responding).')
    else:
      await interaction.response.send('Sorry, an error has occurred.')
    await error_log_webhook.send(text[:2000])

  # Set bot started at timestamp
  app.started_at = datetime.datetime.utcnow()
  app.start_lifespan = False
  app.stop_lifespan = False

  # Set if bot is test or not
  app.test = bool(os.getenv('test'))

  # Add commands
  app.add_commands(
    ping_command
  )

  # Attach / route for debugging
  @app.route('/', methods = ['GET'])
  async def root(request):
    return JSONResponse({
      'Started' : str(app.started_at),
      'Now' : str(datetime.datetime.utcnow()),
      'Test' : app.test,
      'Start lifespan' : str(app.start_lifespan),
      'Stop lifespan' : str(app.stop_lifespan),
      'Lifespan debug' : getattr(app, '__lifespan_debug', []),
      'loop' : str(id(asyncio.get_running_loop())),
      'Errors' : app.errors
    })

  # Attach /stop route for debugging
  @app.route('/stop', methods = ['GET'])
  async def stop(request):
    asyncio.get_event_loop().stop()
    return JSONResponse({'code' : 200})

  # Return app object
  return app