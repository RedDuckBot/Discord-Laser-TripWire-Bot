from typing import Final
import os 
from dotenv import load_dotenv
from discord import Intents, Client, Message

TOKEN: Final[str] = os.getenv("DISCORD_TOKEN2") #Token for Watch_Bot

#Setup Watch_Bot
intents: Intents = Intents.default()
intents.message_content = True 
watch_bot: Client = Client(intents=intents)  

GENERAL_CHANNEL_ID = -1 #TO DEFINE 

@watch_bot.event
async def on_ready():
    print(f"We have logged in as {watch_bot.user}")
    channel = watch_bot.get_channel(GENERAL_CHANNEL_ID)
    await channel.send("Intruder alert, wire has been tripped!")
    await watch_bot.close()

if __name__ == "__main__":
    watch_bot.run(token=TOKEN)
    print("watch_bot logging out")