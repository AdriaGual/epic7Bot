from stages import arena, open_app, sanctuary, summon, abyss, mail, reputation, guild, altar, hunt
from utils import android_connection
import logging
import coloredlogs

coloredlogs.install()
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


android_connection.connect(2)
open_app.start_open()
sanctuary.start_sanctuary()
summon.start_summon()
arena.start_arena(5)
abyss.start_abyss()
mail.start_mail()
altar.start_altar()
hunt.start_hunt(1)
reputation.start_reputation()
guild.start_guild()
hunt.start_hunt(-1)
