from support import *
from random import randint, choice
import discord
import asyncio,time
from config import EMOJI_ID

async def play_roll(ctx,guess,amount,user_eco):
    '''
    main idea

    bot will show animated dice
    after 3 seconds
    will show the first die
    then it will show animated dice
    after 3 seconds
    will show second die

    purely based on luck and rng ofc lololol

    '''
    
    numb = randint(1,6)

    embed = discord.Embed(title="Rolling a...",description=f"{EMOJI_ID[0]}",color=discord.Colour.gold()) 
    message = await ctx.send(embed=embed)
    await asyncio.sleep(3)

    embed.description=f"{EMOJI_ID[numb]}"
    await message.edit(embed=embed)

    if numb == 6 and (guess == "<7" or guess == "l"):
        write(user_eco)
        embed.title="Game!"
        embed.description=f"{EMOJI_ID[numb]}\nThere is no possible two die combinations\nto get less than 7!\nUnlucky, You lost ${amount}! L."
        await message.edit(embed=embed)
        return
    if numb == 1 and (guess == ">7" or guess == "g"):
        write(user_eco)
        embed.title="Game!"
        embed.description=f"{EMOJI_ID[numb]}\nThere is no possible two die combinations\nto get greater than 7!\nUnlucky, You lost ${amount}! L."
        await message.edit(embed=embed)
        return
    else:
        embed.description=f"{EMOJI_ID[numb]} {EMOJI_ID[0]}"
        await message.edit(embed=embed)
        await asyncio.sleep(3)

        numb2 = randint(1,6)

        embed.description=f"{EMOJI_ID[numb]} {EMOJI_ID[numb2]}"
        await message.edit(embed=embed)

        if (guess == "=7" or guess == "e") and (numb+numb2==7):
            user_eco[str(ctx.author.id)]["Balance"] += amount*5
            write(user_eco)
            embed.title="Game!"
            embed.description=f"{EMOJI_ID[numb]} {EMOJI_ID[numb2]}\n\n You won ${amount*5}!"
            await message.edit(embed=embed)
            return
        elif (guess == ">7" or guess == "g") and (numb+numb2>7):
            user_eco[str(ctx.author.id)]["Balance"] += amount*3
            write(user_eco)
            embed.title="Game!"
            embed.description=f"{EMOJI_ID[numb]} {EMOJI_ID[numb2]}\n\n You won ${amount*3}!"
            await message.edit(embed=embed)
            return
        elif (guess == "<7" or guess == "l") and (numb+numb2<7):
            user_eco[str(ctx.author.id)]["Balance"] += amount*3
            write(user_eco)
            embed.title="Game!"
            embed.description=f"{EMOJI_ID[numb]} {EMOJI_ID[numb2]}\n\n You won ${amount*3}!"
            await message.edit(embed=embed)
            return
        else:
            write(user_eco)
            embed.title="Game!"
            embed.description=f"{EMOJI_ID[numb]} {EMOJI_ID[numb2]}\n\n You lost ${amount}! Take the L."
            await message.edit(embed=embed)
            return

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
             "game_die",
             "playground_slide",
             "airplane",
             "placard",
             "bison",
             "coffee",
             "giraffe",
             "children_crossing",
             "coffin",
             "womans_hat",
             "billed_cap",
             "bell_pepper",
             "mermaid",
             "dragon",
             "four_leaf_clover",
             "beer",
             "clinking_glass",
             "wine_glass",
             "basketball",
             "drum",
             "jigsaw",
            ]

    slot1 = slots[randint(0,30)]
    slot2 = slots[randint(0,30)]
    slot3 = slots[randint(0,30)]
    slot4 = slots[randint(0,30)]
    slot5 = slots[randint(0,30)]
    slot6 = slots[randint(0,30)]
    slot7 = slots[randint(0,30)]
    slot8 = slots[randint(0,30)]
    slot9 = slots[randint(0,30)]

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

async def play_race(ctx,racer,amount,user_eco):
    '''
    main idea

    🐎 - horse :racehorse
    🐉 - dragon :dragon:
    🦖 - t rex :t_rex:
    🐌 - snail :snail:
    🐅 - tiger :tiger2:

    user must bet on one of them

    whoever makes the finish line (right to left cuz they facing left) <- gave up and did left to right
    
    the race is bet on rng basically
    

    FOR LATER, DON'T HAVE TO DO THIS YET
    if user does !cheat (easter egg command), 
    the choice the user bet on will run faster (by 2 spaces, instead of 1)
    implement this later

    '''
    
    racer = racer.lower()

    race = ''.join(['🐎\n', '🐉\n', '🦖\n', '🐌\n', '🐅\n'])
    embed = discord.Embed(title="STARTING RACE IN 3",description=f"{race}",color=discord.Colour.dark_gray()) 
    message = await ctx.send(embed=embed)
    
    for x in range(3,-1,-1):
        embed.title = f'STARTING RACE IN {x}'
        await message.edit(embed=embed)
        await asyncio.sleep(1)

    animals = ['🐎', '🐉', '🦖', '🐌', '🐅']

    embed.title = "OFF THEY GO!"
    while max(len(animal) for animal in animals) <= 10:
        select = choice(range(len(animals)))
        animals[select] = '=' + animals[select]
        the_race = "\n".join(animals)
        embed.description = f'{the_race}'
        await message.edit(embed=embed)
        time.sleep(0.1)

    print('race done')
    print(len(animals[0]))
    print(len(animals[1]))
    print(len(animals[2]))
    print(len(animals[3]))
    print(len(animals[4]))

    if len(animals[0]) == 11:
        embed.description = f'{the_race}\n\n🐎 **Won!**'
        await message.edit(embed=embed)
        print("horse")

        if racer == "horse":
            user_eco[str(ctx.author.id)]["Balance"] += amount*10
            write(user_eco)
            embed.description = f'{the_race}\n\n🐎 **Won!**\n\nYou gained: ${amount*10}!'
            await message.edit(embed=embed)
        else:
            write(user_eco)
            embed.description = f'{the_race}\n\n🐎 **Won!**\n\nYou lost: ${amount}!'
            await message.edit(embed=embed)

    elif len(animals[1]) == 11:
        embed.description = f'{the_race}\n\n🐉 **Won!**'
        await message.edit(embed=embed)
        print("dragon")

        if racer == "dragon":
            user_eco[str(ctx.author.id)]["Balance"] += amount*10
            write(user_eco)
            embed.description = f'{the_race}\n\n🐉 **Won!**\n\nYou gained: ${amount*10}!'
            await message.edit(embed=embed)
        else:
            write(user_eco)
            embed.description = f'{the_race}\n\n🐉 **Won!**\n\nYou lost: ${amount}!'
            await message.edit(embed=embed)

    elif len(animals[2]) == 11:
        embed.description = f'{the_race}\n\n🦖 **Won!**'
        await message.edit(embed=embed)
        print("trex")
        
        if racer == "trex":
            user_eco[str(ctx.author.id)]["Balance"] += amount*10
            write(user_eco)
            embed.description = f'{the_race}\n\n🦖 **Won!**\n\nYou gained: ${amount*10}!'
            await message.edit(embed=embed)
        else:
            write(user_eco)
            embed.description = f'{the_race}\n\n🦖 **Won!**\n\nYou lost: ${amount}!'
            await message.edit(embed=embed)

    elif len(animals[3]) == 11:
        embed.description = f'{the_race}\n\n🐌 **Won!**'
        await message.edit(embed=embed)
        print("snail")
        
        if racer == "snail":
            user_eco[str(ctx.author.id)]["Balance"] += amount*10
            write(user_eco)
            embed.description = f'{the_race}\n\n🐌 **Won!**\n\nYou gained: ${amount*10}!'
            await message.edit(embed=embed)
        else:
            write(user_eco)
            embed.description = f'{the_race}\n\n🐌 **Won!**\n\nYou lost: ${amount}!'
            await message.edit(embed=embed)

    elif len(animals[4]) == 11:
        embed.description = f'{the_race}\n\n🐅 **Won!**'
        await message.edit(embed=embed)
        print("tiger")

        if racer == "tiger":
            user_eco[str(ctx.author.id)]["Balance"] += amount*10
            write(user_eco)
            embed.description = f'{the_race}\n\n🐅 **Won!**\n\nYou gained: ${amount*10}!'
            await message.edit(embed=embed)
        else:
            write(user_eco)
            embed.description = f'{the_race}\n\n🐅 **Won!**\n\nYou lost: ${amount}!'
            await message.edit(embed=embed)
