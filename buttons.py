import discord
from discord.ext import commands
from blackjack import Blackjack

class allButtons(discord.ui.View):
    def __init__(self,author,playerTotal,dealerTotal,pValue1,pValue2,dValue1,dValue2,pdeck,ddeck,pHand,deck):
        super().__init__()
        self.author = author
        self.pT = playerTotal
        self.dT = dealerTotal
        self.pV1 = pValue1
        self.pV2 = pValue2
        self.dV1 = dValue1
        self.dV2 = dValue2
        self.pd = pdeck
        self.dd = ddeck
        self.pH = pHand
        self.deck = deck

    async def interaction_check(self,interaction: discord.Interaction):
        return interaction.user.id == self.author.id

    @discord.ui.button(label="Hit",style=discord.ButtonStyle.green,emoji="🃏")
    async def btn1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("hit")

    @discord.ui.button(label="Double Down",style=discord.ButtonStyle.green,emoji="💵")
    async def btn2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("double down")

    @discord.ui.button(label="Stand",style=discord.ButtonStyle.green,emoji="🤚")
    async def btn3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("stand")

        #await interaction.response.edit_message(embed=embed)