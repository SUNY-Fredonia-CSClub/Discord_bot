import discord

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
    
    if message.content.startswith('$help'):
      await message.channel.send('Happy to help. To start my prefix is $ put that in front of any of the listed commands to activate me. \n My current supported commands include: \n $hello \n $website \n $wholesome \n $help')
client.run('your toekn here')
