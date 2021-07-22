import os
import time
import templates
from utils import global_utils
import logging


def start_event_daily_rewards():
    logging.warning("------------")
    logging.warning("---EVENT DAILY---")
    logging.warning("------------")
    logging.info("Searching event")
    global_utils.click_position(1500, 618, 1, "Focus screen")
    global_utils.click_position(1407, 52, 2, "Enter mail")
    global_utils.click_position(1250, 250, 2, "Enter event")
    time.sleep(5)
    os.system("adb shell input swipe 952 738 952 246 200")
    time.sleep(2)
    while global_utils.click_image(templates.epic_seven_arena_pnj_fight, 2) == 1:
        global_utils.click_position(826, 559, 2, "Enter event")
