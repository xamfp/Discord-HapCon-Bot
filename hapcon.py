import discord
import asyncio
import time
import uuid
import threading
import random

#### CONFIG ####
token = ''          # Insert your Discord API Key Here
password = ''       # This is the event deletion password
#### END OF CONFIG ###

client = discord.Client()
@client.event
async def on_ready():
    	print('# Logged in as')
    	print('# Name: ' + client.user.name)
    	print('# User ID' + client.user.id)
    	print('################')
    	print('# Commands: ')
    	print('# !HAPCON -> Posts a recent happening')
    	print('# !HAPPENING <URL> -> Adds a happening to a list')
    	print('# !clear <password>')

@client.event
async def on_message(message):
	if message.content.lower().startswith('!happening'):
		client.loop.create_task(addHappening(message))
	if message.content.lower().startswith('!hapcon'):
		client.loop.create_task(postHappening(message))
	if message.content.lower().startswith('!clear'):
		client.loop.create_task(clearHappenings(message))

async def addHappening(message):
	try:
		if message.content.lower().startswith('!happening'):
			url = message.content.split(' ')[1].strip()
		if url != '':
			await client.send_message(message.channel, url + ' has been added to recent happenings!')
			with open('happenings.txt', 'a') as f:
				f.write(url + '\n')
		else:
			await client.send_message(message.channel, 'HappeningBot Error! Proper Usage: !HAPPENING http://example.com')
	except:
		await client.send_message(message.channel, 'HappeningBot Error! Proper Usage: !HAPPENING http://example.com')
async def postHappening(message):
	with open('happenings.txt', 'r') as r:
		happening = random.choice(r.read().strip().split('\n'))
		if happening == '':
			await client.send_message(message.channel, 'There are no happenings to display!')
		else:
			await client.send_message(message.channel, 'Recent Happening: ' + happening)

async def clearHappenings(message):
	if message.content.split('!clear')[1].strip() == password:
		with open('happenings.txt', 'w') as f:
			f.write('')
		await client.send_message(message.channel, 'Happenings Cleared!')
	else:
		await client.send_message(message.channel, 'Invalid Password!')

print('# Clear Happenings Password: ' + password)
print('# Connecting to Discord...')
client.run(token.strip(), bot=True)
