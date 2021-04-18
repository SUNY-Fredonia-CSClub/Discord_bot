import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('ODMwOTgzMzc0MDk2MDM5OTc2.YHOnkw.4NnnGHLzFyQsYvDu3mM9RbgQLZ0')
