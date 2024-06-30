import os
import json

# Load configs for local hosting
path = 'config.json'
if os.path.isfile(path): # <-- file won't exist in production
  with open(path) as f: 
    config = json.loads(f.read())
  for key, value in config.items():
    os.environ[key] = value
  os.environ['test'] = '1'
  print('Using test bot configs!')


from src.bot import run

print("""
  ____            _      ____        _   _ 
 |  _ \          (_)    |  _ \      | | | |
 | |_) | __ _ ___ _  ___| |_) | ___ | |_| |
 |  _ < / _` / __| |/ __|  _ < / _ \| __| |
 | |_) | (_| \__ \ | (__| |_) | (_) | |_|_|
 |____/ \__,_|___/_|\___|____/ \___/ \__(_)                                                                                                         
""")

# Run the bot
app = run()