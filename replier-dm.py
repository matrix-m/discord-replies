import discord
import codecs
import random
from discord.ext import commands

TOKEN = '' # bot token

client = discord.Client()


@client.event
async def on_ready():
    print(f'ok, throw me some numbers')

with open('pls.txt') as f, open('gas.txt') as g:
    quotes = f.readlines()
    quotes1 = g.readlines()

    def quoter():
        return random.choice(quotes).strip()

    def quoter1(): #Sends DM from g
        return random.choice(quotes1).strip()

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
            try:  # removes errors, user might not allow DMs from non-friends
                await message.author.send(quoter1()) #DMs the author specified
            except:
                pass
            return
        elif message.author.bot:
            return

client.run(TOKEN)
