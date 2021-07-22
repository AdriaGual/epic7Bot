import os
import time
import templates
from stages import stage_replay
from utils import global_utils, android_connection
import logging
import coloredlogs

coloredlogs.install()
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

android_connection.connect(0)
logging.warning("----------")
logging.warning("---HUNT---")
logging.warning("----------")

while 1:
    if global_utils.click_image(templates.epic_seven_arena_pnj_fight_2, 4) == 1:
        while global_utils.click_image(templates.epic_seven_stage_clear, 5) == 0 and global_utils.click_image(templates.epic_seven_stage_failed, 5) == 0:
            logging.info("Retry finish fight")
        global_utils.click_position(660, 660, 4, "Cancel")
        while global_utils.click_image(templates.epic_seven_confirm_hunt_2, 2) == 0:
            global_utils.click_position(932, 290, 4, "Confirm")
        global_utils.click_image(templates.epic_seven_confirm_hunt, 2)
        while global_utils.click_image(templates.epic_seven_hunt_another_time, 2) == 0:
            logging.info("Retry another time")
