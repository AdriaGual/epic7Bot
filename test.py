import templates
from stages import arena, open_app, sanctuary, summon, abyss, mail, reputation, guild, altar, hunt

from utils import android_connection, global_utils
import subprocess
import time
android_connection.connect(0)

arena.start_arena(5)
