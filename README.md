# Watch Laser Trip Wire with Discord Bot 
This project utilized two Discord bots to watch a laser trip wire where a master bot,
named Wire_Bot, a.k.a Hal, who responded to certain commands in general chat. The images bellow demonstrate what prompts Hal would respond to, and the last two pictures show a simple setup for the trip wire.

<p align="center">
  <img title='Bot Chat Ex. One' src=docs/images/image01.png width="650">
  <img title='Bot Chat Ex. Two' src=docs/images/image02.png width="650">
</p>

<p align="center">
  <img title='Trip Wire Pic One' src=docs/images/tripWirePic01.png width="300">
  <img title='Trip Wire Pic Two' src=docs/images/tripWirePic02.png width="300">
</p>

# Hardware & Circuits
Here's a list of components used in the project:

| |Components |
|--| --|
|1| Raspberry Pi 3B+ |
|2| Light Dependent Resistor (LDR)|
|3| 1uF Capacitor|
|4| N-MOSFET|
|5| 470Ω Resistor| 
|6| 5V Laser Diode|

Next, lets take a look at the two circuits. 
### Light Sensor Circuit 
<p align="center">
  <img title='Light Sensor Circuit' src=docs/circuits/light_sensor.png width="800">
</p>

### Laser Circuit 
<p align="center">
  <img title='Laser Circuit' src=docs/circuits/laser.png width="800">
</p>

# Setup & Run Application 
Create two Discord bots and provide them with read and send permissions for your chosen server. The bot Wire_Bot, the master bot, responds to chat commands and since we don't want this bot to be blocked when watching the trip wire, another bot, Watch_Bot, is assigned this task (which was only used to log on to noftify general chat that the wire has been tripped, and then immediately logs off). 

### Test Circuits
After setting up both the laser and light sensor circuits make sure they are working by using the 'test_devices.py'. 

### Store Bot Tokens & Define General Chat ID
In the root directory of the project create a file '.env'. This will contain a safe place for storing the tokens for the bots. Add the tokens and the following variables to '.env': 
```
DISCORD_TOKEN=[Add token for Wire_Bot]
DISCORD_TOKEN2=[Add token for Watch_Bot]
```
Next, in files 'main.py' and 'watch_bot.py', there is a global variable called 'GENERAL_CHANNEL_ID', that must be defined using your server's general chat ID.

### Run Main
Finally, install necessary packages used in this project:
```
pip install -r ./docs/requirements.txt
```

Then, start running the application:
```
python main.py
```

Expect the bot, Hal, to greet you in general chat, as shown in the bellow image:
<p align="center">
  <img title='Laser Circuit' src=docs/images/hal_greet.png width="400">
</p>

When done with application, close main program with 'Ctrl + c'

