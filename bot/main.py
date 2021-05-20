import discord
import os
# import requests
# import json
# import random
# from dotenv import load_dotenv

# load_dotenv()

client = discord.Client()

# sad_words= ["sad", "depressed", "unhappy", "miserable", "depressing"]
# basic_encouragements= ["Cheer up!", "You can do it!", "You are a good person!"]

# def get_quote():
#     response= requests.get("https://zenquotes.io/api/random")
#     json_data= json.loads(response.text)
#     quote= json_data[0]['q'] + " -" + json_data[0]['a']
#     return quote

@client.event 
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # msg= message.content    

    if message.content.startswith('$Hello'):
        # quote= get_quote()
        await message.channel.send("Hello!")

    # if any (word in msg for word in sad_words):
        # await message.channel.send(random.choice(basic_encouragements))

client.run(os.getenv('TOKEN'))