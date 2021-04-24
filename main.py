#Made by Cameron Showard for the Suny Fredonia Computer Science Club

import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello my name is FredBot. I am a discord bot built by the Suny Fredonia Computer Science Club!')
    
	if message.content.startswith('$website'):
		await message.channel.send('The link to our website is http://cs.fredonia.edu/~csclub/')
    
	if message.content.startswith('$wholesome'):
		await message.channel.send('You are not a drop in the ocean, you are the entire ocean in a drop.')
    
	if message.content.startswith('$joke'):
		await message.channel.send('A girl named Autumn tried to prank me. I didn’t fall for it!')

	if message.content.startswith('$puppy'):
		file = os.listdir('puppies/')
		dog=[]
		for i in file:
			dog.append(i)
		response = random.choice(dog)
		await message.channel.send(file=discord.File('puppies/'+response))
	if message.content.startswith('$snap'):
		file = os.listdir('Thanos/')
		thanos = []
		for i in file:
			thanos.append(i)
		response = random.choice(thanos)
		await message.channel.send(file=discord.File('Thanos/' + response))

	if message.content.startswith('$thumbsup'):
		emoji = '\U0001F44D'
		await message.add_reaction(emoji)

	if message.content.startswith('$help'):
		await message.channel.send('Happy to help. To start my prefix is $ put that in front of any of the listed commands to activate me. \n My current supported commands include: \n $hello \n $website \n $wholesome \n $joke \n $puppy \n snap \n $help')
client.run('Your token here')
