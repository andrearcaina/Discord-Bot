import discord
from support import *
import blackjack as BJ
import asyncio

class Play(discord.ui.View):
    def __init__(self,author,playerTotal,dealerTotal,pdeck,ddeck,deck,pH,dH,user_eco,amount):
        super().__init__()
        self.author = author
        self.pT = playerTotal
        self.dT = dealerTotal
        self.pd = pdeck
        self.dd = ddeck
        self.deck = deck
        self.ue = user_eco
        self.a = amount
        self.pH = pH
        self.dH = dH

    async def interaction_check(self,interaction: discord.Interaction):
        return interaction.user.id == self.author.id

    @discord.ui.button(label="Hit",style=discord.ButtonStyle.green,emoji="🃏")
    async def btn1(self, interaction: discord.Interaction, button: discord.ui.Button):
        print("pH "+str(self.pH))
        if self.pH != 0:
            for i in self.pd:
                if i[2] == "a":
                    self.pT -= 10
                    self.pH = 0

        print("pH "+str(self.pH))

        hitValue, new_card = await BJ.Blackjack().newPlayerCard(self.pT)

        self.pd.append(new_card)
        self.pT += hitValue
        
        if self.pT > 21:
            write(self.ue)
            embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
            self.pd = " ".join(self.pd)
            self.dd = " ".join(self.dd)
            embed.title="Dealer: 'Take L.'"
            embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou busted!\nSome unfortunate news! You lost: ${self.a}!"
            return await interaction.response.edit_message(embed=embed,view=None)

        elif self.pT == 21:
            self.ue[str(self.author.id)]["Balance"] += self.a*2
            write(self.ue)
            embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
            self.pd = " ".join(self.pd)
            self.dd = " ".join(self.dd)
            embed.title="Dealer: 'Congrats, I guess.'"
            embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou won: ${self.a*2}!"
            return await interaction.response.edit_message(embed=embed,view=None)

        else: #if player's total is less than or equal to 21
            view = Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.pH,self.dH,self.ue,self.a)
                
            embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
        
            await interaction.response.edit_message(embed=embed,view=view)

    @discord.ui.button(label="Double Down",style=discord.ButtonStyle.green,emoji="💵")
    async def btn2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.ue[str(self.author.id)]["Balance"] -= self.a
        write(self.ue)
        
        print("pH "+str(self.pH))
        if self.pH != 0:
            for i in self.pd:
                if i[2] == "a":
                    self.pT -= 10
                    self.pH = 0

        print("pH "+str(self.pH))

        hitValue, new_card = await BJ.Blackjack().newPlayerCard(self.pT)

        self.pd.append(new_card)
        self.pT += hitValue
        
        if self.pT > 21:
            write(self.ue)
            embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
            self.pd = " ".join(self.pd)
            self.dd = " ".join(self.dd)
            embed.title="Dealer: 'Take L.'"
            embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou busted!\nSome unfortunate news! You lost: ${self.a*2}!"
            return await interaction.response.edit_message(embed=embed,view=None)

        elif self.pT == 21:
            self.ue[str(self.author.id)]["Balance"] += self.a*4
            write(self.ue)
            embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
            self.pd = " ".join(self.pd)
            self.dd = " ".join(self.dd)
            embed.title="Dealer: 'Congrats, I guess.'"
            embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou won: ${self.a*4}!"
            return await interaction.response.edit_message(embed=embed,view=None)
        
        else:
            if self.dT >= 17:    
                if self.pT == self.dT: #Tie
                    self.ue[str(self.author.id)]["Balance"] += self.a*2
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Wow. Not Bad.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Tied with the Dealer!\n\nYou got your money back!"
                    return await interaction.response.edit_message(embed=embed,view=None)
                elif self.pT > self.dT: #Win
                    self.ue[str(self.author.id)]["Balance"] += self.a*4
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Congrats, I guess.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou won: ${self.a*4}!"
                    return await interaction.response.edit_message(embed=embed,view=None)
                elif self.pT < self.dT: #Lose
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Take L.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou LOST!\nSome unfortunate news! You lost: ${self.a*2}!"
                    return await interaction.response.edit_message(embed=embed,view=None)
            
            else: #if dealer total is less than 17 or player hand > dealer hand
                print("dH "+str(self.dH))
                if self.dH != 0:
                    for i in self.dd:
                        if i[2] == "a":
                            self.dT -= 10
                            self.dH = 0

                print("dH "+str(self.dH))

                while True:
                    dhitValue, d_new_card = await BJ.Blackjack().newDealerCard(self.dT)
                    self.dd.append(d_new_card)
                    self.dT += dhitValue
                    
                    if 17 < self.dT < 21:
                        break 
                    
                    elif self.dT > 21:
                        self.ue[str(self.author.id)]["Balance"] += self.a*4
                        write(self.ue)
                        embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                        self.pd = " ".join(self.pd)
                        self.dd = " ".join(self.dd)
                        embed.title="Dealer: 'Congrats. mhm.'"
                        embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Won.\nYou gained: ${self.a*4}!"
                        return await interaction.response.edit_message(embed=embed,view=None)

                #let x = self.dT =? if xE(17,21), then run below
            
                if self.pT == self.dT: #Tie
                    self.ue[str(self.author.id)]["Balance"] += self.a*2
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Wow. Not Bad.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Tied with the Dealer!\n\nYou got your money back!"
                    return await interaction.response.edit_message(embed=embed,view=None)
                
                elif self.pT > self.dT: #Win
                    self.ue[str(self.author.id)]["Balance"] += self.a*4
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Congrats, I guess.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou won: ${self.a*4}!"
                    return await interaction.response.edit_message(embed=embed,view=None)
                
                elif self.pT < self.dT: #Lose
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Take L.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou LOST!\nSome unfortunate news! You lost: ${self.a*2}!"
                    return await interaction.response.edit_message(embed=embed,view=None)
            
    @discord.ui.button(label="Stand",style=discord.ButtonStyle.green,emoji="🤚")
    async def btn3(self, interaction: discord.Interaction, button: discord.ui.Button):        
        if self.dT >= 17:    
            if self.pT == self.dT: #Tie
                self.ue[str(self.author.id)]["Balance"] += self.a
                write(self.ue)
                embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                self.pd = " ".join(self.pd)
                self.dd = " ".join(self.dd)
                embed.title="Dealer: 'Wow. Not Bad.'"
                embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Tied with the Dealer!\n\nYou got your money back!"
                return await interaction.response.edit_message(embed=embed,view=None)
            elif self.pT > self.dT: #Win
                self.ue[str(self.author.id)]["Balance"] += self.a*2
                write(self.ue)
                embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                self.pd = " ".join(self.pd)
                self.dd = " ".join(self.dd)
                embed.title="Dealer: 'Congrats, I guess.'"
                embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou won: ${self.a*2}!"
                return await interaction.response.edit_message(embed=embed,view=None)
            elif self.pT < self.dT: #Lose
                write(self.ue)
                embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                self.pd = " ".join(self.pd)
                self.dd = " ".join(self.dd)
                embed.title="Dealer: 'Take L.'"
                embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou LOST!\nSome unfortunate news! You lost: ${self.a}!"
                return await interaction.response.edit_message(embed=embed,view=None)
        
        else: #if dealer total is less than 17 or player hand > dealer hand
            print("dH "+str(self.dH))
            if self.dH != 0:
                for i in self.dd:
                    if i[2] == "a":
                        self.dT -= 10
                        self.dH = 0

            print("dH "+str(self.dH))

            while True:
                dhitValue, d_new_card = await BJ.Blackjack().newDealerCard(self.dT)
                self.dd.append(d_new_card)
                self.dT += dhitValue
                
                if 17 < self.dT < 21:
                    break 
                
                elif self.dT > 21:
                    self.ue[str(self.author.id)]["Balance"] += self.a*2
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Congrats. mhm.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Won.\nYou gained: ${self.a*2}!"
                    return await interaction.response.edit_message(embed=embed,view=None)

            #let x = self.dT =? if xE(17,21), then run below
        
            if self.pT == self.dT: #Tie
                self.ue[str(self.author.id)]["Balance"] += self.a
                write(self.ue)
                embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                self.pd = " ".join(self.pd)
                self.dd = " ".join(self.dd)
                embed.title="Dealer: 'Wow. Not Bad.'"
                embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Tied with the Dealer!\n\nYou got your money back!"
                return await interaction.response.edit_message(embed=embed,view=None)
            
            elif self.pT > self.dT: #Win
                self.ue[str(self.author.id)]["Balance"] += self.a*2
                write(self.ue)
                embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                self.pd = " ".join(self.pd)
                self.dd = " ".join(self.dd)
                embed.title="Dealer: 'Congrats, I guess.'"
                embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou won: ${self.a*2}!"
                return await interaction.response.edit_message(embed=embed,view=None)
            
            elif self.pT < self.dT: #Lose
                write(self.ue)
                embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                self.pd = " ".join(self.pd)
                self.dd = " ".join(self.dd)
                embed.title="Dealer: 'Take L.'"
                embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou LOST!\nSome unfortunate news! You lost: ${self.a}!"
                return await interaction.response.edit_message(embed=embed,view=None)