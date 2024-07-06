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

  # Lifespan can also be used to async setup .session and .db attributes
  # https://www.starlette.io/lifespan
  @contextlib.asynccontextmanager
  async def lifespan(app):
    try:
      yield
    finally:
      if app.http.session: # close bot session
        await app.http.session.close() 

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
      'Errors' : app.errors
    })

  # Return app object
  return app