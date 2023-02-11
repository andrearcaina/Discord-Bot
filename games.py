from support import *
from random import randint
import discord

async def play_cf(ctx,choice,numb,amount,user_eco):
    if (choice == "tails" and numb == 1) or (choice == "heads" and numb == 2):
        user_eco[str(ctx.author.id)]["Balance"] += amount*2
        write(user_eco)
        await ctx.send(f"You won {amount*2} :dollar:!")
        return
    else:
        write(user_eco)
        await ctx.send(f"You lost ${amount}. Trash")
        return

async def play_slots(ctx,amount,user_eco):
    slots = ["banana",
             "apple",
             "moneybag",
             "dollar",
             "ping_pong",
             "crown",
             "spy",
             "anatomical_heart",
             "dumpling",
             "t_rex",
             "llama",
             "koko",
             "yen",
             "ghost",
             "flag_us",
             "game_die"
            ]

    slot1 = slots[randint(0,14)]
    slot2 = slots[randint(0,14)]
    slot3 = slots[randint(0,14)]
    slot4 = slots[randint(0,14)]
    slot5 = slots[randint(0,14)]
    slot6 = slots[randint(0,14)]
    slot7 = slots[randint(0,14)]
    slot8 = slots[randint(0,14)]
    slot9 = slots[randint(0,14)]

    print(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9)

    slotOutput1 = '| :{}: | :{}: | :{}: |\n'.format(slot1,slot2,slot3)
    slotOutput2 = '| :{}: | :{}: | :{}: |\n'.format(slot4,slot5,slot6)
    slotOutput3 = '| :{}: | :{}: | :{}: |\n'.format(slot7,slot8,slot9)

    slot = ''.join([slotOutput1,slotOutput2,slotOutput3])

    egg = discord.Embed(title = "Slots Machine", color = discord.Colour.dark_blue())
    egg.add_field(name = "{}\ndino love".format(slot), value = f'You won {1000*amount} dollars! :t_rex:',inline=False)

    pot = discord.Embed(title = "Slots Machine", color = discord.Colour.gold())
    pot.add_field(name = "{}\nJACKPOT".format(slot), value = f'You won {9*amount} dollars! :moneybag:',inline=False)

    won = discord.Embed(title = "Slots Machine", color = discord.Colour.green())
    won.add_field(name = "{}\nWon".format(slot), value = f'You won {3*amount} dollars! :dollar:',inline=False)
    
    mid = discord.Embed(title = "Slots Machine", color = discord.Colour.green())
    mid.add_field(name = "{}\nWon".format(slot), value = f'You won {2*amount} dollars! :coin:',inline=False)

    lost = discord.Embed(title = "Slots Machine", color = discord.Colour.red())
    lost.add_field(name = "{}\nLost".format(slot), value = f'You lost {1*amount} dollars. L bozo.',inline=False)

    if slot1==slot2==slot3==slot4==slot5==slot6==slot7==slot8==slot9=="t_rex":
        user_eco[str(ctx.author.id)]["Balance"] += amount*1000
        await ctx.send(embed = egg)
        return

    elif (slot1 == slot2 == slot3) and (slot4 == slot5 == slot6) and (slot7 == slot8 == slot9) or (slot1==slot2==slot3==slot4==slot5==slot6==slot7==slot8==slot9):
        user_eco[str(ctx.author.id)]["Balance"] += amount*9
        await ctx.send(embed = pot)
        return
    
    elif (slot1 == slot2 == slot3) or (slot4 == slot5 == slot6) or (slot7 == slot8 == slot9) or (slot1 == slot4 == slot7) or (slot2 == slot5 == slot8) or (slot3 == slot6 == slot9) or (slot1 == slot5 == slot9) or (slot3 == slot5 == slot7):
        user_eco[str(ctx.author.id)]["Balance"] += amount*3
        write(user_eco)
        await ctx.send(embed = won)
        return

    elif (slot1 == slot2) or (slot2 == slot3) or (slot4 == slot5) or (slot5 == slot6) or (slot7 == slot8) or (slot8 == slot9) or (slot1 == slot4) or (slot4 == slot7) or (slot2 == slot5) or (slot5 == slot8) or (slot3 == slot6) or (slot6 == slot9): 
        user_eco[str(ctx.author.id)]["Balance"] += amount*2
        write(user_eco)
        await ctx.send(embed = mid)
        return

    else:
        write(user_eco)
        await ctx.send(embed = lost)
        return