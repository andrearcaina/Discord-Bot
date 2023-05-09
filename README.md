# Discord-Bot
### Economy Bot
- All purpose gambling bot where the user can: 
  - Play blackjack! gamble your money away! 
  - Steal other members and rob stores!
  - Made using python and Discord.py

### ```To Run``` ###
- download the zip folder
- have python installed
- create **main.py** file
- copy this:
```Py
import bot
import discord
from discord.ext import commands
from config import TOKEN

if __name__ == "__main__":
    #initializing bot
    econ_bot = commands.Bot(command_prefix="!",help_command=None,intents=discord.Intents.all())

    bot.run_bot(TOKEN,econ_bot) #run bot
```
- create **config.py** file
- copy this and replace 'YOUR_DISCORD_TOKEN_HERE' with your own discord token:
```Py
TOKEN   =               'YOUR_DISCORD_TOKEN_HERE'

DECK    =           [   "<:2spades:1075610591181414422>",
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

EMOJI_ID =          [   "<a:animated_dice:1075250955077038150>",
                        "<:dice1:1075251125319651329>",
                        "<:dice2:1075251123235074138>",
                        "<:dice3:1075251121980964884>",
                        "<:dice4:1075251126871523338>",
                        "<:dice5:1075280427176181791>",
                        "<:dice6:1075251118898159626>"
                    ]
```
- you're good to go! run main.py

or: 
- invite the [bot](https://discord.com/api/oauth2/authorize?client_id=1072622197165793300&permissions=2183991392320&scope=bot)!
