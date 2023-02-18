import discord
from support import *
import blackjack as BJ

class Play(discord.ui.View):
    def __init__(self,author,playerTotal,dealerTotal,pdeck,ddeck,deck,dV,pH,dH,user_eco,amount):
        super().__init__()
        self.author = author
        self.pT = playerTotal
        self.dT = dealerTotal
        self.pd = pdeck
        self.dd = ddeck
        self.deck = deck
        self.ue = user_eco
        self.a = amount
        self.dV = dV
        self.pH = pH
        self.dH = dH

    async def interaction_check(self,interaction: discord.Interaction):
        return interaction.user.id == self.author.id

    #hit button
    @discord.ui.button(label="Hit",style=discord.ButtonStyle.green,emoji="🃏")
    async def btn1(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.pH != 0:
            for i in self.pd:
                if i[2] == "a":
                    self.pT -= 10
                    self.pH = 0

        hitValue, new_card = await BJ.Blackjack().newPlayerCard(self.pT)

        self.pd.append(new_card)
        self.pT += hitValue
        
        if self.pT >= 21:
            await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).do_hit(interaction)
        else: #if player's total is less than 21
            view = Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a)
            view.remove_item(view.btn2)
            view.remove_item(view.btn4)
            self.pd = " ".join(self.pd)
            self.dd = " ".join(self.dd[0:2])
            embed = discord.Embed(title="Dealer: 'Lets Play Some Blackjack!'",description=f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dV}")
            await interaction.response.edit_message(embed=embed,view=view)

    #double down button
    @discord.ui.button(label="Double Down",style=discord.ButtonStyle.green,emoji="💵")
    async def btn2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.ue[str(self.author.id)]["Balance"] -= self.a
        write(self.ue)
    
        if self.pH != 0:
            for i in self.pd:
                if i[2] == "a":
                    self.pT -= 10
                    self.pH = 0

        hitValue, new_card = await BJ.Blackjack().newPlayerCard(self.pT)

        self.pd.append(new_card)
        self.pT += hitValue
        
        if self.pT >= 21:
            await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).do_hit(interaction)
        else:
            amt = self.a*2
            await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).do_stand(interaction,amt)

    #stand button     
    @discord.ui.button(label="Stand",style=discord.ButtonStyle.green,emoji="🤚")
    async def btn3(self, interaction: discord.Interaction, button: discord.ui.Button):        
        self.dd.remove("<:facedown:1076126049743675533>")
        await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).do_stand(interaction,self.a)

    @discord.ui.button(label="Insurance Bet",style=discord.ButtonStyle.green,emoji="📋")
    async def btn4(self, interaction: discord.Interaction, button: discord.ui.Button):        
        pass #insurance bet, will work on later

    #hit lose win
    async def do_hit(self,interaction: discord.Interaction):
        self.dd.remove("<:facedown:1076126049743675533>")
        if self.pT > 21: #if they bust
            await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).L(interaction,self.a)

        elif self.pT == 21: #if they get 21 they insta win
            await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).W(interaction,self.a)

    #stand win lose
    async def do_stand(self, interaction: discord.Interaction,amt):
        self.a = amt
        if self.dT >= 17:    
            if self.pT == self.dT: #Tie
                await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).T(interaction,self.a)
            
            elif self.pT > self.dT: #Win
                await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).W(interaction,self.a)
            
            elif self.pT < self.dT: #Lose
                await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).L(interaction,self.a)
        
        else: #if dealer total is less than 17 or player hand > dealer hand
            if self.dH != 0:
                for i in self.dd:
                    if i[2] == "a":
                        self.dT -= 10
                        self.dH = 0

            while True:
                dhitValue, d_new_card = await BJ.Blackjack().newDealerCard(self.dT)
                self.dd.append(d_new_card)
                self.dT += dhitValue
                
                if 17 < self.dT < 21:
                    break 
                
                elif self.dT > 21:
                    self.ue[str(self.author.id)]["Balance"] += self.a*2
                    self.ue[str(self.author.id)]["In Game"] = False
                    write(self.ue)
                    embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
                    self.pd = " ".join(self.pd)
                    self.dd = " ".join(self.dd)
                    embed.title="Dealer: 'Congrats. mhm.'"
                    embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Won.\nYou gained: ${self.a*2}!"
                    return await interaction.response.edit_message(embed=embed,view=None)

            #let x = self.dT => if xE(17,21), then run below
        
            if self.pT == self.dT: #Tie
                await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).T(interaction,self.a)
            
            elif self.pT > self.dT: #Win
                await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).W(interaction,self.a)
            
            elif self.pT < self.dT: #Lose
                await Play(self.author,self.pT,self.dT,self.pd,self.dd,self.deck,self.dV,self.pH,self.dH,self.ue,self.a).L(interaction,self.a)

    async def L(self,interaction: discord.Interaction,amt):
        self.a = amt
        self.ue[str(self.author.id)]["In Game"] = False
        write(self.ue)
        embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
        self.pd = " ".join(self.pd)
        self.dd = " ".join(self.dd)
        embed.title="Dealer: 'Take L.'"
        embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou LOST!\nSome unfortunate news! You lost: ${self.a}!"
        return await interaction.response.edit_message(embed=embed,view=None)

    async def W(self,interaction: discord.Interaction,amt):
        self.a = amt
        self.ue[str(self.author.id)]["Balance"] += self.a*2
        self.ue[str(self.author.id)]["In Game"] = False
        write(self.ue)
        embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
        self.pd = " ".join(self.pd)
        self.dd = " ".join(self.dd)
        embed.title="Dealer: 'Congrats, I guess.'"
        embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou won: ${self.a*2}!"
        return await interaction.response.edit_message(embed=embed,view=None)
    
    async def T(self, interaction: discord.Interaction,amt):
        self.a = amt
        self.ue[str(self.author.id)]["Balance"] += self.a
        self.ue[str(self.author.id)]["In Game"] = False
        write(self.ue)
        embed = await BJ.Blackjack().displayCards(self.pd,self.dd,self.pT,self.dT)
        self.pd = " ".join(self.pd)
        self.dd = " ".join(self.dd)
        embed.title="Dealer: 'Wow. Not Bad.'"
        embed.description = f"Your Hand: {self.pd} Total value: {self.pT}\n\nDealer Hand: {self.dd} Total value: {self.dT}\n\nYou Tied with the Dealer!\n\nYou got your money back!"
        return await interaction.response.edit_message(embed=embed,view=None)