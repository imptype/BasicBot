import os
import asyncio
import datetime
import traceback
import contextlib
import aiohttp
import discohook
from starlette.responses import JSONResponse
from .cogs.ping import ping_command

from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

# class CustomMiddleware(BaseHTTPMiddleware):
#   check = False
#   async def dispatch(self, request, call_next):
#     # run once
#     print('recieve request')
#     if not self.check:
#       self.check = True
#       await request.app.http.session.close() # close bot session
#       request.app.http.session = aiohttp.ClientSession('https://discord.com', loop = asyncio.get_running_loop()) # create session on current event loop
#     return await call_next(request)

def run():

  # Lifespan to gracefully shutdown, which only happens during local testing
  # This can also be used to setup .session and .db attributes
  @contextlib.asynccontextmanager
  async def lifespan(app):
    # async with aiohttp.ClientSession() as app.session:
    #   async with Database(app, os.getenv('SPACE_DATA_KEY')) as app.db:
    await app.http.session.close() # close bot session
    app.http.session = aiohttp.ClientSession('https://discord.com', loop = asyncio.get_running_loop()) # create session on current event loop
    app.used_lifespan = datetime.datetime.utcnow()
    try:
      yield
    except asyncio.CancelledError:
      print('Ignoring cancelled error.')
    else:
      print('Closed without errors.')
    finally:
      await app.http.session.close() # close bot session

  # Define the bot
  app = discohook.Client(
    application_id = os.getenv('DISCORD_APPLICATION_ID'),
    public_key = os.getenv('DISCORD_PUBLIC_KEY'),
    token = os.getenv('DISCORD_BOT_TOKEN'),
    password = os.getenv('SYNC_PASSWORD'),
    lifespan = lifespan#,
    #middleware = [Middleware(CustomMiddleware)]
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
  app.used_lifespan = False

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
      'Used lifespan' : str(app.used_lifespan),
      'Errors' : app.errors
    })

  # Return app object
  return app