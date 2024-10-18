# Information
[![Deploy with Vercel](https://vercel.com/button)][1]

This Discord bot is **SERVERLESS** which means it can run for **FREE** and be **ALWAYS** online on [Vercel](https://vercel.com)!  
You can also treat this repository as a template for making serverless bots with the [discohook](https://github.com/jnsougata/discohook) library.

### Table of Contents
- [Information](#information)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [File Structure](#file-structure)
- [Running the bot](#running-the-bot)
  - [Run Locally](#run-locally)
  - [Deploy Online](#deploy-online)
  - [Now make it your own!](#now-make-it-your-own)
- [Links and Resources](#links-and-resources)

# Features
<!-- todo
- `/color` - a simple command that shows how to use a button.
- `/quiz` - a simple command that shows how to use command options.
- `/count` - a medium command that shows how to store a count without a database.
- `/pages` - an advanced command that shows how to nest multiple views together.
or meta features vs commands
-->
- `/ping` - a simple command that tells you the bot's latency. 
- And you can easily create and add more commands yourself!

An example deployment of BasicBot is at: https://basic-bot.vercel.app *(Not recommended to share publically)*  
Invite the bot and test the features: https://discord.com/oauth2/authorize?client_id=1257121896021889094

# File Structure
```
.
├─ src/                       # Source code
│  ├─ cogs/                   # All command files
│  │  └─ ping.py              # Ping command
│  └─ bot.py                  # Defines the Discord bot
├─ .gitignore                 # Hides certain files
├─ LICENSE                    # License
├─ README.md                  # Defines this README page
├─ example-config.json        # Example of a config.json file
├─ main.py                    # Entry point
├─ requirements.txt           # Library dependencies
└─ vercel.json                # Vercel deployment configuration
```

# Running the bot
A quick way to run your own instance of the bot is to click the Vercel Deploy Button:

[![Deploy with Vercel](https://vercel.com/button)][1]

### Run Locally
1. Make sure you have these first.
   - [Python 3.9+](https://www.python.org/downloads) - to run Python files.
     - Run `python -V` in Terminal to check what Python version you have.
     - *Any version under 3.9 will probably result in errors when deployed to Vercel.*
   - [Visual Studio Code](https://code.visualstudio.com/download) - a code editor to write your code in.
     - You might also want the [Discord Presence](https://marketplace.visualstudio.com/items?itemName=icrawl.discord-vscode) extension to show people you're editing your project.
   - [A Discord bot](https://discord.com/developers/applications) - make one for free and copy these things:
     - Application ID ➔ Located in General Information, used to identify your app in requests.
     - Public Key ➔ Located in General Information, used to validate interactions are coming from Discord.
     - Token ➔ Located in Bots, used to authenticate requests, **don't share this with anyone!**
   - [Github Account](https://github.com/join) - to make a GitHub repository for your project.
     - Repositories (like this one) are a place to store code, files, and preserve commit history.
     - This is used by Vercel later on to deploy your code automatically.
   - Either one of the following to commit code to your repo:
     - [Git](https://git-scm.com/downloads) - a CLI command to update changes by typing things like `git commit` in Terminal.
     - [Github Desktop](https://desktop.github.com/download) - an app that's easier to use than running Git commands in Terminal.
   - [Ngrok](https://ngrok.com) - a CLI command that starts a reverse proxy, making your localhost visible to the internet.
     - Create an Ngrok account.
     - Install the CLI command.
       - Windows:
         - Download ZIP file from [Ngrok downloads](https://ngrok.com/download) and click keep anyway if it says unsafe.
         - Extract and move `ngrok.exe` to a folder like `C:\Program Files\Ngrok\bin`.
         - Search "Edit the system environment variables" in Windows search and click it.
         - Click Environment Variables, under System variables select the Path variable and click Edit.
         - Click New, paste the file path of the folder like `C:\Program Files\Ngrok\bin` and click Ok.
         - You may need to whitelist it via Windows Security ➔ Protection History ➔ Find and click Allow.
       - Linux: Run this [one command](https://ngrok.com/docs/getting-started/?os=linux) in Terminal:
         ```bash
         curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
         sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
         echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
         sudo tee /etc/apt/sources.list.d/ngrok.list && \
         sudo apt update && sudo apt install ngrok
         ```
     - Find your Ngrok token from dashboard and then run `ngrok config add-authtoken <token>` in Terminal.
     - P.S. Discord recommends using Ngrok for local development in their official [JavaScript Tutorial](https://discord.com/developers/docs/quick-start/getting-started#:~:text=ngrok).
     - NOTE: Ngrok's Free Tier has a 60 requests/min ratelimit. For a higher one, use [Cloudflare Tunnels](https://developers.cloudflare.com/pages/how-to/preview-with-cloudflare-tunnel).

2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.
   - Git:
     - Open Terminal at the location you want your project to be like `C:\Users\imp\Documents\Projects`.
       - You can open File Explorer to that location, right-click an empty space and click Open in Terminal.
     - Run `git clone https://github.com/imptype/BasicBot` to copy this repo into a `BasicBot` folder.
   - Github Desktop:
     - Open GitHub Desktop (and login if not already) and select File ➔ Clone Repository ➔ URL
     - Paste the URL `https://github.com/imptype/BasicBot` and choose a location, then click Clone.

3. Open the `BasicBot` folder in [Visual Studio Code](vscode:).
   - Whenever you make changes to a file, remember to do CTRL+S to save.
   - And from now on, use the Terminal in Visual Studio Code to run any of the commands below.

4. Rename `example-config.json` to `config.json` and paste the values in the quotes.
   - `DISCORD_APPLICATION_ID` is your Discord Application ID.
   - `DISCORD_PUBLIC_KEY` is your Discord Public Key.
   - `DISCORD_BOT_TOKEN` is your Discord Bot Token, **don't share it!**
   - `ERROR_LOG_WEBHOOK` is a Discord webhook URL that relays error messages your bot encounters.
     - Discord channel settings ➔ Integrations ➔ New Webhook ➔ Copy Webhook URL.
   - `SYNC_PASSWORD` is a password set by you and you type it when you sync commands later on.

5. Install requirements. A venv is recommended.
   - Run `python -m venv venv` to create a venv folder.
   - Activate the venv.
     - Windows: `venv/Scripts/activate`
     - Linux: `source venv/bin/activate`
   - Run `pip install -r requirements.txt` to install dependencies to that venv folder.
     - `discohook` subclasses the ASGI app `Starlette`, it adds an `/interactions` route and Discord functions.
     - `uvicorn` is the ASGI server used to run the ASGI app and start a web server.
   - To deactivate run `deactivate`. You still need to be in venv when running the bot though.

6. Run `uvicorn main:app` to start the web server.
   - By default this is located at web browser address `127.0.0.1:8000` AKA `localhost:8000`.
   - Only you and devices on your local network can access it, so we'll need a reverse proxy.
   - You can do CTRL+C to stop running.

7. In another Terminal, run `ngrok http 8000` to start the reverse proxy.
   - This returns an ngrok URL like `https://123123123.ngrok.io` or ends with `ngrok-free.app`.
   - Now anyone on the internet can visit this URL and see your website, including Discord's API.
   - You can do CTRL+C to stop running.

8. Set the Interactions Endpoint URL to `<url>/interactions` where `url` is your Ngrok URL.
   - This is located in General Information of your app's [Discord developers](https://discord.com/developers/applications) page.
   - `discohook` recieves Discord interactions/requests by default through the `/interactions` route.
   - Make sure your Uvicorn server and Ngrok proxy are still running or it will fail to set.

9. Visit the `/api/dash` route of your website to register slash commands for the first time.
   - Visit `127.0.0.1/api/dash` or `localhost/api/dash` or `<ngrok-url>/api/dash` either one works.
   - You need to type the value of `SYNC_PASSWORD` you set in `config.json`.
   - This route returns a JSON of all the commands that have been succesfully registered to Discord.
   - You only need to sync commands when you create/update public facing things, like slash command names.
   - You can only do [~200 command creates per day](https://discord.com/developers/docs/interactions/application-commands#registering-a-command), so don't spam this route.

Now invite your bot to your server if you haven't already and run the slash commands! 

Remember:  
&nbsp;&nbsp;➔ Whenever you start coding, start Uvicorn and Ngrok and update your Interactions Endpoint URL.  
&nbsp;&nbsp;➔ Whenever you make code changes, CTRL+S to save, CTRL+C Uvicorn and up and enter to start it again.  
&nbsp;&nbsp;➔ Whenever you change client side stuff, like command options and descriptions, sync your commands again.  
&nbsp;&nbsp;➔ Sometimes you need to CTRL+R (refresh) your Discord (clears cache) after syncing for commands to show.  
&nbsp;&nbsp;➔ You can use the `uvicorn main:app --reload` argument to reload the server automatically when files change.

### Deploy Online
1. Make a GitHub repository and link it to the `BasicBot` folder.
   - Git CLI:
     - Go to [Github.com](https://github.com) and make an empty repository.
     - Go to [Personal Access Tokens in User Settings](https://github.com/settings/tokens?type=beta) and create a token for this repository.
       - Make sure the token has `Read and write` permissions for `Contents` in `Repository Permissions`.
     - Open the `BasicBot` folder in Terminal.
     - Run `git init` to initialize a new local Git repository.
     - Set your Git configuration:
       - Run `git config user.email "your-email@example.com"`
       - Run `git config user.name "Your Name"`
     - Run `git remote add origin https://github.com/your-username/your-repo.git` to link them.
     - Stage your files with `git add .` and commit them with `git commit -m "Initial commit"`.
     - Push your changes to GitHub with `git push -u origin main`.
   - GitHub Desktop:
     - Open GitHub Desktop (and login if not already) and select File ➔ Add Local Repository.
     - Choose the `BasicBot` folder and follow the prompts to create a new repository.

2. [Login to Vercel](https://vercel.com/login) and add your GitHub repository.
   - Dashboard ➔ Add New ➔ Project ➔ Adjust Github App Permissions ➔ Auth ➔ Select then Import.
   - Set Build Command to `uvicorn main:app`.
   - Set Install Command to `pip install -r requirements.txt`.
   - Paste all your environment variables from `config.json` into Environment Variables and click Deploy.
   - NOTE: `vercel.json` uses an [edited version](https://www.npmjs.com/package/@imptype/vercel-python) of the NPM package [`@vercel/python`](https://www.npmjs.com/package/@vercel/python) to fix event loop issues.

3. Set the Interactions Endpoint URL to `<url>/interactions` where `url` is your Vercel URL.
   - Once deployed, click your preview box to know what your `123123123.vercel.app` URL is.

Your bot is now online 24/7 in a **serverless** environment. Cold starts are < 3 seconds, so your bot will reply in time!

Some things to note:  
&nbsp;&nbsp;➔ Serverless means cache will not retain after ~5 minutes of inactivity.  
&nbsp;&nbsp;➔ You also can't do things that require a persistent websocket, like listening for message/voice/guild events.  
&nbsp;&nbsp;➔ You may want to use 2 bots, 1 is a test bot with dev credentials locally, the other with prod credentials on Vercel.  
&nbsp;&nbsp;➔ If you want to be able to cache properly across multiple simultaneous serverless instances, use Redis / [Vercel KV](https://vercel.com/docs/storage/vercel-kv).

### Now make it your own!
BasicBot is just a demonstration, so feel free to change the name and add more commands and do whatever you want. If you need inspiration for things to add or to know what's possible, check out the [discohook/examples](https://github.com/jnsougata/discohook/tree/main/examples) folder, which contains a lot of simple examples like modals, buttons, slash command arguments, etc. You can also check out [MazeRace](https://github.com/imptype/MazeRace), a small Discord bot that shows how to do things like storing variables inside of custom IDs, image generation, nested and persistent views, and uses a simple database.

# Links and Resources
- **Discohook Discord:** https://discord.gg/xEEpJvE9py
  - If you need help then visit and ask here.
- **Discord API Documentation:** https://discord.com/developers/docs/interactions/overview
  - Read up what's possible with Interactions on the Discord API.
- **Vercel Documentation:** https://vercel.com/docs
  - Read up other things you can do on Vercel.

<!-- REFERENCES -->
[1]: https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fimptype%2FBasicBot&env=DISCORD_APPLICATION_ID,DISCORD_PUBLIC_KEY,DISCORD_BOT_TOKEN,ERROR_LOG_WEBHOOK,SYNC_PASSWORD&envDescription=Read%20the%20README.md%20file%20to%20know%20what%20to%20put%20in%20each%20value.&project-name=basicbot&repository-name=BasicBot&demo-title=BasicBot%20Quick%20Deploy&demo-description=A%20quick%20way%20to%20deploy%20a%20serverless%20Python%20Discord%20bot%20on%20Vercel.&demo-url=https%3A%2F%2Fbasic-bot.vercel.app&demo-image=https%3A%2F%2Fi.imgur.com%2FwR99MHB.png
