from random import randint

def respond(message, user) -> str:
    m = message.lower()

    if m == 'hello':
        return "Hey there "+str(user)[:-5]+"! If you need help with the bot, type !help"
    
    if m == 'roll':
        return str(randint(1,6))
    