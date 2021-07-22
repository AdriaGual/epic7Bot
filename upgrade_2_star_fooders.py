import templates
from stages import arena, open_app, sanctuary, summon, abyss, mail, reputation, guild, altar, hunt
from utils import android_connection, global_utils
import subprocess
import time
import logging
import coloredlogs

coloredlogs.install()
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

android_connection.connect(0)

while(1):
    global_utils.click_position(848, 848, 3, "")
    global_utils.click_position(1456, 350, 2, "")
    global_utils.click_position(1456, 350, 2, "")
    global_utils.click_position(1090, 820, 2, "")
    global_utils.click_position(916, 555, 2, "")
