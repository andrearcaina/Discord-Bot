import discord
from discord.ext import commands
from random import choice
from support import *
import asyncio
import buttons

'''
    Standard rules of blackjack
    
    - card values are their representive number 
    - except for ace and face cards
    - ace = 1 or 11 (depends on user)
    - face cards (jack queen king) = 10
    - closest to 21 or is 21 wins 
    - if dealer wins, player loses the money they bet (if they don't have 21)
    - if player wins, player gets their money back twice (bet $10 you get $20)
    - if player gets blackjack (21 with two cards only) then the payout is 3:1 (bet $10 you get $30) -> (3:2 is normal, but nah, 3:1 instead!)
    - you can also double down (bet $10 initially, then you double down, pay another $10, draw your last card, if you win you get $40)
    - general payouts = 1:1 (normal/double down) and 3:1 (blackjack)
    - odds of getting blackjack (1 in 20.8 hands)
    - odds of winning a game of blackjack (42.22%)
    - odds of dealer winning (49.1%)
    - odds of tying (8.48%)

    This file is meant for readability and manageability

'''

class Blackjack():
    def __init__(self):
        self.playerTotal = 0
        self.dealerTotal = 0
        self.pValue1 = 0
        self.pValue2 = 0
        self.dValue1 = 0
        self.dValue2 = 0
        self.pdeck = []
        self.ddeck = []
        self.pHand = 2
        self.deck = [   "<:2spades:1075610591181414422>",
                        "<:2hearts:1075610590183174144>",
                        "<:2diamonds:1075610589012959274>",
                        "<:2clovers:1075610587033260122>",
                        "<:3spades:1075610595824504942>",
                        "<:3hearts:1075610594427797535>",
                        "<:3diamonds:1075610593874153574>",
                        "<:3clover:1075610592188059658>",
                        "<:4spades:1075611286706061402>",
                        "<:4hearts:1075611285699440700>",
                        "<:4diamonds:1075610598370443324>",
                        "<:4clovers:1075611283950415962>",
                        "<:5spades:1075611290606776462>",
                        "<:5hearts:1075611288958402560>",
                        "<:5diamonds:1075610601759449098>",
                        "<:5clovers:1075611287779823646>",
                        "<:6spades:1075611294369075220>",
                        "<:6hearts:1075611292674568273>",
                        "<:6diamonds:1075610604926156880>",
                        "<:6clovers:1075611291529515108>",
                        "<:7spades:1075611435138285599>",
                        '<:7hearts:1075611434454626304>',
                        '<:7diamonds:1075610608331919451>',
                        '<:7clovers:1075611432156147742>',
                        '<:8spades:1075611439785578657>',
                        '<:8hearts:1075611297766453389>',
                        '<:8diamonds:1075610611788034058>',
                        '<:8clovers:1075611436589514772>',
                        '<:9spades:1075611526733500436>',
                        '<:9hearts:1075610615323824128>',
                        '<:9diamonds:1075611525433274491>',
                        '<:9clovers:1075611523503886366>',
                        '<:10spades:1075611530462240798>',
                        '<:10hearts:1075611528734179339>',
                        '<:10diamonds:1075610618444386406>',
                        '<:10clovers:1075611301893636107>',
                        '<:acespades:1075611534488768612>',
                        '<:acehearts:1075610622298951680>',
                        '<:acediamonds:1075611305026793503>',
                        '<:aceclovers:1075611531535974480>',
                        '<:jackspades:1075610626061250641>',
                        '<:jackhearts:1075611654538137620>',
                        '<:jackdiamond:1075611653141434368>',
                        '<:jackclovers:1075611650721316925>',
                        '<:queenspades:1075612145192022046>',
                        '<:queenhearts:1075612144189591552>',
                        '<:queendiamond:1075612143115829309>', 
                        '<:queenclovers:1075612141475872838>',
                        '<:kingspades:1075610629366358087>',
                        '<:kinghearts:1075612139613589505>',
                        '<:kingdiamonds:1075611657075703858>', 
                        '<:kingclovers:1075611655297323039>'
                    ]
        
    async def play_bj(self,ctx,amount,user_eco):
        #first round of cards dealt and drawn
        dcard1 = choice(self.deck)
        self.deck.remove(dcard1)
        self.ddeck.append(dcard1)
        dcard2 = choice(self.deck)
        self.deck.remove(dcard2)
        self.ddeck.append(dcard2)

        pcard1 = choice(self.deck)
        self.deck.remove(pcard1)
        self.pdeck.append(pcard1)
        pcard2 = choice(self.deck)
        self.deck.remove(pcard2)
        self.pdeck.append(pcard2)

        self.dValue1 = first_value(dcard1[2])
        self.dValue2 = first_value(dcard2[2])
        self.pValue1 = first_value(pcard1[2])
        self.pValue2 = first_value(pcard2[2])

        self.dealerTotal = self.dValue1+self.dValue2
        self.playerTotal = self.pValue1+self.pValue2

        embed = discord.Embed(title="Dealer is drawing cards...") #add animation emote
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed.title = "Dealer: 'Lets Play Some Blackjack!'" #add animation emote
        embed.description = f"Your Hand: {pcard1} {pcard2} Total value: {self.playerTotal}\n\nDeal Hand: {dcard1} {dcard2} Total value: {self.dealerTotal}"
        await msg.edit(embed=embed,view=buttons.allButtons(ctx.author,self.playerTotal,self.dealerTotal,self.pValue1,self.pValue2,self.dValue1,self.dValue2,self.pdeck,self.ddeck,self.pHand,self.deck))

        async def pWin(ctx,embed):
            user_eco[str(ctx.author.id)]["Balance"] += amount*2
            write(user_eco)
            embed.title="Dealer: 'Congrats...'"
            embed.description = f'You Won!\n\nYou gained: ${amount*2}!'
            await msg.edit(embed=embed)
        
        async def tie(ctx,embed):
            user_eco[str(ctx.author.id)]["Balance"] += amount
            write(user_eco)
            embed.title="Dealer: 'Mhm...'"
            embed.description = f'You Tied with the Dealer!\n\nYou going your money back!'
            await msg.edit(embed=embed)

        async def BJ(ctx,embed):
            user_eco[str(ctx.author.id)]["Balance"] += amount*3
            write(user_eco)
            embed.title="Dealer: 'Congrats...'"
            embed.description = f'You got Blackjack!\n\nYou gained: ${amount*3}!'
            await msg.edit(embed=embed)

        async def L(embed):
            write(user_eco)
            embed.title="Dealer: 'Take L.'"
            embed.description = f'You lost!\n\nYou lost: ${amount}!'
            await msg.edit(embed=embed)