
# install git https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe
# then run this in cmd: python -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum

import discum, asyncio, time, json, os
from threading import Thread
from discum.utils.slash import SlashCommander
print("""
 /$$$$$$$
| $$__  $$
| $$  \ $$ /$$   /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$
| $$$$$$$ | $$  | $$| $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$
| $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$
|_______/  \______/ |__/ |__/ |__/| $$____/  \_______/|__/
                                  | $$
                                  | $$
                                  |__/""");time.sleep(1)
print("""
                   ......   /*.******,,,,,.*,,*.            ,*.  .***,.
                ,.......  ,*..*...*/*/,,,, ..                   .,            ,*
             .. .......  .    .,          . ....   .,              .*.  .***,.
           ,, ........... ..                           ,           /****.
         ..,........,,..                                 ,   ,/***/**,***.
        ,,,,./..,....                   .         ..       . *(******,*/,,.,.
       ,.*/,,...           .            .,          ..  .    *(/**..******//
    .,. ....             ..             ,..*         ..  . .///*,.,..*******/
  ,..   .              .,,    .        .. ...,        ..  ,/****,*.****///,.
,.     .              ,.,     .       .*..... ,   .... ..  *(/*//(/****,/.
   ..,              .,..,    .        ,..   ,,..,       ,.  ..   (//**//(.
...                ,.  ..    ,       ./..     ....,      *. .     ./*/..
.,             .,.*...... ,  ,       ...           .,.   .. ,    .. .,..
                .,...  .,.,  ..      /.             ...,  , .     , ..*.
       ,       ,.. .    .,.,  ,      /   ,/*..***,...,,..**       . ,.*,
       .   .  ,. .       .*.*.,.     *    /*.. *,/  ./, ,.*      .  ,..*.
,        ,..  ..                *.   *       .,***((/,**  ,    . .  ...,..
..*    . ,... .,  .*,**.,/, ,.   , *...       /*.....,*,  .    , ,   .,.,*
....,   ./..,.*..  **..,*(*(/*,                /,    *,  *    ,  .    */*.,
 .. ...,,,,...*,.,./   *,.//..*                  ...    ,   **     .   *./,,. .,
  ,...      .*..,.,    ,,,.  ./  .             ..... ..,  ,  .  .. .  , ../(* .
   ,..       *..,...     .*,*.                    ..*,,.,  .   . ,   ,.  *,.,.,
    ,. ,.    *.,...*                ,,,,.              ,       .  *...,  .,,.
     *. *.,   **....*,..         .,,,,..... ..        ,       ,.....,.  /*, ,
    *,**/ ,..,..,,../.           ,,,.  ... ...       ,       ,..../,..*,,,*,,
  .*,,,,/,*.    ...../,          ..............      ,      .,,,.,*//(,,,,,,.
 *,,..,.**      ,..*,,.,/           . ......         /. ..  *..,,*/ *,,,,,,*.
*,,,../,* ,.*.   *.,...*   ,/,                    ,*/..., ...  ..* .,,,,,,,*.
 .,,    ....  *.  *.,,..,,, ,,   .,****//*,. ....,......*.   *,..  *,,,(,,,*.
.        .*       .,,,.,..,. .  ,***,,,,,,/*.  .......,/.    ...  .*.,*(((**,
.,*.   .,           ,....*  .../,,,...,, ,..        .**      ... . *.,,*/,,*,
  ,,,.      .      ....,,  ..*..,,,,../ .*..        /.      ...    ,,,,,,,,,/
Created by cherryy#0001 User id: 950559051102703628
Github Page: https://github.com/aiaemx""");time.sleep(1)

#First time setup\
if os.path.exists('options.json') == True:
    pass
else:
	for i in range(5):
		print(" ")
	print("First time setup")
	server1 = input("Server 1 serverID: ")
	server2 = input("Server 2 serverID: ")
	server3 = input("Server 3 serverID: ")
	server4 = input("Server 4 serverID: ")
	channel1 = input("Bump channel 1 ChannelID: ")
	channel2 = input("Bump channel 2 ChannelID: ")
	channel3 = input("Bump channel 3 ChannelID: ")
	channel4 = input("Bump channel 4 ChannelID: ")
	token = input("User Token: ")
	data = {
	"server1":server1,
	"server2":server2,
	"server3":server3,
	"server4":server4,
	"channel1":channel1,
	"channel2":channel2,
	"channel3":channel3,
	"channel4":channel4,
	"token":token}
	with open("options.json", "w") as options:
		options.write(str(json.dumps(data)))

f = open("options.json", "r")
settings=json.load(f)

server1=settings["server1"];server2=settings["server2"];server3=settings["server3"];server4=settings["server4"];
channel1=settings["channel1"];channel2=settings["channel2"];channel3=settings["channel3"];channel4=settings["channel4"];
token=settings["token"]
botID = "302050872383242240"

#discum stuff
from discum.utils.slash import SlashCommander

def task(guildID, channelID):
	bot = discum.Client(token = token, log=False)
	def bump(resp, guildID, channelID, botID):
		if resp.event.ready_supplemental:
			bot.gateway.request.searchSlashCommands(guildID, limit=10, query="bump")
		if resp.event.guild_application_commands_updated:
			bot.gateway.removeCommand(bump)
			slashcommands = resp.parsed.auto()['application_commands']
			s = SlashCommander(slashcommands, application_id=botID)
			data = s.get(['bump'])
			bot.triggerSlashCommand(botID, channelID=channelID, guildID=guildID, data=data, sessionID=bot.gateway.session_id)
			print("Successfully bumped")
            	bot.gateway.close()
	bot.gateway.command(
	    {
		    "function": bump,
		    "params": {"guildID": guildID, "channelID": channelID, "botID": botID},
	    }
	)

	bot.gateway.run()
thingy = 0
while True:
	guildID = [server1, server2, server3, server4]
	channelID = [channel1, channel2, channel3, channel4]
	t1 = Thread(target=task, args=(guildID[thingy], channelID[thingy]))
	t1.start()
	t1.join()
	time.sleep(1925)
	if guildID and channelID == None:
		guildID = [server1, server2, server3, server4]
		channelID = [channel1, channel2, channel3, channel4]
	thingy = thingy + 1
	if thingy == 4:
		thingy = 0

# Credits
# popsicle
# cherryy
