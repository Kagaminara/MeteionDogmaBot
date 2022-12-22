import configparser

import discord

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
botToken = config['SECRETS']['BOT_TOKEN']

intents = discord.Intents.default()
intents.reactions = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print("message received")
    if message.author == client.user:
        print("Ignored")
        return

    if message.content.startswith('$hello'):
        print("Should answer")
        await message.channel.send('Hello!')

@client.event
async def on_raw_reaction_add(payload):
    print("reaction added")
    print(payload.channel_id)
    if payload.channel_id == 1055242387997347840 and payload.emoji.name == "🐣":
        print("inside rules")
        await payload.member.add_roles(payload.member.guild.get_role(role_id=1055241418324582410))
        print("Roled added to")
        print(payload.member)

client.run(botToken)
