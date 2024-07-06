"""
/ping is simple command that tells you the bot's latency.
It also includes other timestamps to help calculate the coldstart time.
"""

import time
import discohook

@discohook.command.slash('ping', description = 'Ping test the bot!')
async def ping_command(interaction):
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