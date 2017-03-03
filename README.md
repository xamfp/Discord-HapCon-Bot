# Discord-HapCon-Bot
Discord bot used to keep track of current news stories / other related happenings

### Installation
Login to http://discordapp.com and go to https://discordapp.com/developers/applications/me and create an application and add it as a bot user.

Go to to https://discordapp.com/oauth2/authorize?client_id=YOUR-BOTS-CLIENT-ID-GOES-HERE&scope=bot&permissions=0 and add your bot to your server.

To install the discord api for python3 run the following command:
```
python3 -m pip install -U discord.py
```

Edit the `hapcon.py` file and add your discord API Key and a password to allow deletion of events under the configuration section.

Execute the following command:
```
python3 hapcon.py
```

If you're going to be running this command on a VPS, it is recommended to run this command using screen:
```
screen python3 hapcon.py
```


### Usage
````
Commands:
!HAPCON -> Posts a recent happening
!HAPPENING <URL> -> Adds a happening to a list

# IMPORTANT: When using the clear command be sure to either private message 
# this command to the bot or send it in a private channel otherwise people in 
# the discord server will be able to see the password.
!clear <password>     
```
