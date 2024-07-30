from enum import Enum

#Responses related to wire_bot
class Bot_responses(Enum):
    ON_WATCH = 0 #Put bot on watch duty 
    ALREADY_ON = 1 #Bot already on watch duty
    OFF_WATCH = 2 #Take bot off watch duty
    ALREADY_OFF = 3 #Bot already off watch duty
    NO_RESP = 4 #Current message not relevant to bot
    UNKNOWN = 5 #Not a valud instruction for bot


def get_response(instruct_bot: Bot_responses) -> str:

    if instruct_bot == Bot_responses.ON_WATCH: 
        return "On watch for intruders! Delegating this responsibility to my assistant, Watch_Bot."
    elif instruct_bot == Bot_responses.ALREADY_ON:
        return "My assistant, Watch_Bot, is already on watch duty." 
    elif instruct_bot == Bot_responses.OFF_WATCH:
        return "Taking Watch_Bot off watch duty."
    elif instruct_bot == Bot_responses.ALREADY_OFF:
        return "Already not on watch duty."
    else:
        return "I don't understand... To instruct me, use the following commands: 'Hal:watch_on' or 'Hal:watch_off'." 
