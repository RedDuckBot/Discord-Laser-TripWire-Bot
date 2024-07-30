from typing import Final
import os, time, sys, subprocess 
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response, Bot_responses
from light_sensor import LightSensor 
from laser import Laser
from threading import Thread, Lock
import RPi.GPIO as GPIO

#Load tokens from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN") #Token for Wire_Bot

#Setup Wire Bot
intents: Intents = Intents.default()
intents.message_content = True
wire_bot: Client = Client(intents=intents)

GENERAL_CHANNEL_ID = -1 #TO DEFINE

#Initialize light sensor and laser
GPIO.setmode(GPIO.BCM)
LASER_PIN = 27
LIGHT_SENSOR_PIN = 17
laser: Laser = Laser(LASER_PIN)
light_sensor: LightSensor = LightSensor(LIGHT_SENSOR_PIN)

#File path to watch_bot
PATH = "./watch_bot.py"
watch_bot_active = False #Shared between Wire_bot and watch thread

sensor_watch_lock = Lock()

#Acts as a thread for watching light sensor circuit
def watch_sensor() -> None:
    global watch_bot_active 

    light_sensor.wait_for_dark()

    if watch_bot_active:
        subprocess.run([sys.executable,PATH])
        time.sleep(2)

    sensor_watch_lock.acquire()
    watch_bot_active = False
    sensor_watch_lock.release()

#Wire Bot Message functionality 
async def send_message(message:Message, user_message: str) -> None:

    if not user_message:
        print("Message was empty")
        return 

    msg: str = user_message[4:] 
    instruct_bot: Bot_responses = process_user_message(msg)

    #Wire Bot's reply back to user
    try:
        response: str = get_response(instruct_bot)
        await message.channel.send(response)
    except Exception as e:
        print(e)

#Process user message and identify the appropriate response for wire_bot
def process_user_message(msg: str) -> Bot_responses:
    global watch_bot_active 
    if msg == "watch_on":  
        if watch_bot_active: 
            return Bot_responses.ALREADY_ON
        else: #Notify Watch_Bot he's been placed on watch duty
            sensor_thread = Thread(target=watch_sensor,args=())
            sensor_thread.start()
            sensor_watch_lock.acquire()
            watch_bot_active = True
            sensor_watch_lock.release()
            return Bot_responses.ON_WATCH
    elif msg == "watch_off":
        if not watch_bot_active:
            return Bot_responses.ALREADY_OFF
        else: #Notify watch_bot that he's been absolved from watch duty
              #And manually trigger trip wire
            sensor_watch_lock.acquire()
            watch_bot_active = False
            sensor_watch_lock.release()
            laser.off()
            time.sleep(2)
            laser.on()
            return Bot_responses.OFF_WATCH
    else:
        return Bot_responses.UNKNOWN

#Handle the startup for wire_bot
@wire_bot.event
async def on_ready() -> None:
    print(f"{wire_bot.user} is now running.")
    channel = wire_bot.get_channel(GENERAL_CHANNEL_ID)
    await channel.send("Hal, online and ready to manage trip wire. Begin instruction prompts with 'Hal:[command]'")

#Handling incoming messages
@wire_bot.event
async def on_message(message: Message) -> None:
    if message.author == wire_bot.user: #Avoid endless bot replies to itself
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    #Return if message is not relevant to wire bot, a.k.a Hal
    if user_message[0:4] != "Hal:":
        return

    print(f"[{channel}] {username}: '{user_message}'")
    await send_message(message, user_message)

def main() -> None:
    wire_bot.run(token=TOKEN)

if __name__ == "__main__":
    laser.on()
    main()
    print("Cleaning up resources.")
    laser.off()
    GPIO.cleanup()
