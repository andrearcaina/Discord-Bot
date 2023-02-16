import discord
from random import choice
from support import *
import asyncio
import interactions
from config import DECK

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
        self.playerhit = None
        self.dealerhit = None
        self.deck = DECK
        
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

        self.dValue1 = Blackjack().first_value(dcard1[2])
        self.dValue2 = Blackjack().hit_value(dcard2[2],self.dValue1)
        self.pValue1 = Blackjack().first_value(pcard1[2])
        self.pValue2 = Blackjack().hit_value(pcard2[2],self.pValue1)

        self.dealerTotal = self.dValue1+self.dValue2
        self.playerTotal = self.pValue1+self.pValue2

        embed = discord.Embed(title="Dealer is drawing cards...") #add animation emote
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed.title = "Dealer: 'Lets Play Some Blackjack!'" #add animation emote
        embed.description = f"Your Hand: {pcard1} {pcard2} Total value: {self.playerTotal}\n\nDealer Hand: {dcard1} {dcard2} Total value: {self.dealerTotal}"
        view = interactions.Play(ctx.author,self.playerTotal,self.dealerTotal,self.pdeck,self.ddeck,self.deck,2,2,user_eco,amount)
        await msg.edit(embed=embed,view=view)

        await asyncio.sleep(1)

        if self.dealerTotal == 21:
            await Blackjack().L(msg,embed,self.pdeck,self.ddeck,self.playerTotal,self.dealerTotal,user_eco,amount)

        if self.playerTotal == 21:
            await Blackjack().B(ctx,msg,embed,self.pdeck,self.ddeck,self.playerTotal,self.dealerTotal,user_eco,amount)
    
    async def T(self,ctx,msg,embed,user_eco,amount):
        user_eco[str(ctx.author.id)]["Balance"] += amount
        write(user_eco)
        embed.title="Dealer: 'Not Bad...'"
        embed.description = f'You Tied with the Dealer!\n\nYou got your money back!'
        return await msg.edit(embed=embed,view=None)

    async def B(self,ctx,msg,embed,pd,dd,ptotal,dtotal,user_eco,amount):
        user_eco[str(ctx.author.id)]["Balance"] += amount*3
        write(user_eco)
        pd = " ".join(pd)
        dd = " ".join(dd)
        embed.title="Dealer: 'Congrats, I guess.'"
        embed.description = f"Your Hand: {pd} Total value: {ptotal}\n\nDealer Hand: {dd} Total value: {dtotal}\n\nYou won: ${amount*3}!"
        return await msg.edit(embed=embed,view=None)

    async def L(self,msg,embed,pd,dd,ptotal,dtotal,user_eco,amount):
            write(user_eco)
            embed.title="Dealer: 'Take L.'"
            pd = " ".join(pd)
            dd = " ".join(dd)
            embed.description = f"Your Hand: {pd} Total value: {ptotal}\n\nDealer Hand: {dd} Total value: {dtotal}\n\nYou're bad!\nSome unfortunate news! You lost: ${amount}!"
            await msg.edit(embed=embed,view=None)

    async def newPlayerCard(self,total):
        self.playerhit = choice(self.deck)
        self.deck.remove(self.playerhit)
        
        hitValue = Blackjack().hit_value(self.playerhit[2],total)

        return int(hitValue),self.playerhit

    async def newDealerCard(self,total):
        self.dealerhit = choice(self.deck)
        self.deck.remove(self.dealerhit)

        hitValue = Blackjack().hit_value(self.dealerhit[2],total)

        return int(hitValue),self.dealerhit

    async def displayCards(self,pdeck,ddeck,ptotal,dtotal):
        pdeck = " ".join(pdeck)
        ddeck = " ".join(ddeck)
        return discord.Embed(title="Dealer: 'Lets Play Some Blackjack!'",description=f"Your Hand: {pdeck} Total value: {ptotal}\n\nDealer Hand: {ddeck} Total value: {dtotal}")
    
    def hit_value(self,value,total):
        if value == "a":
            if total > 10:
                return 1
            else:
                return 11
        elif value == "j":
            return 10
        elif value == "q":
            return 10
        elif value == "k":
            return 10
        elif value == "1":
            return 10
        else:
            return int(value) 

    def first_value(self,value):
        if value == "a":
            return 11
        elif value == "j":
            return 10
        elif value == "q":
            return 10
        elif value == "k":
            return 10
        elif value == "1":
            return 10
        else:
            return int(value)