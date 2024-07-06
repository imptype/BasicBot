import time
import discohook

@discohook.command.slash('ping', description = 'Ping test the bot!')
async def command(interaction):
  created_at = interaction.created_at
  now = time.time()
  since = now - created_at

  text = '\n'.join([
    'Pong! Latency: `{:.2f}ms`'.format(since * 1000),
    '',
    'Bot started at: {}'.format(interaction.client.started_at.timestamp()),
    'Interaction created at: {}'.format(created_at),
    'Time right now: {}'.format(now)
  ])

  await interaction.response.send(text)