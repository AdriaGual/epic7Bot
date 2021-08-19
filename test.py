import templates
from stages import arena, open_app, sanctuary, summon, abyss, mail, reputation, guild, altar, hunt
import sys
from utils import android_connection, global_utils
import subprocess
import time
android_connection.connect(0)

if len(sys.argv) > 1:
    print(sys.argv[1])
    if sys.argv[1] == "-abyss":
        print("AAA")
