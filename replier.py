import discord
import codecs
import random
from discord.ext import commands

TOKEN = '' # bot token

client = discord.Client()


@client.event
async def on_ready():
    print(f'ok, throw me some numbers')

with codecs.open('pls.txt', 'r', 'utf-8') as f:
    quotes = f.readlines()

    def quoter():
        return random.choice(quotes).strip()

coolest = commands.CooldownMapping.from_cooldown(1, 180, commands.BucketType.user)

@client.event
async def on_message(message):
    bucket = coolest.get_bucket(message)
    retry_after = bucket.update_rate_limit()
    if retry_after:
        return
    else:
        if message.author.id == : # insert user ID without quotes ex == 123456789:
            await message.channel.send(quoter(), reference=message)
            return
        elif message.author.bot:
            return

client.run(TOKEN)