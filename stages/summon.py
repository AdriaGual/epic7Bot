import os
import time
import templates
from utils import global_utils
import logging


def start_summon():
    logging.warning("------------")
    logging.warning("---SUMMON---")
    logging.warning("------------")
    logging.info("Entering summon")
    global_utils.click_position(1500, 618, 1, "Entering Battle")
    global_utils.click_image(templates.epic_seven_summon, 2)
    time.sleep(2)
    os.system("adb shell input swipe 1400 856 1400 156 200")
    time.sleep(1)
    logging.info("Choosing normal summon (not banner)")
    global_utils.click_image(templates.epic_seven_free_summon, 2)
    logging.info("Choosing daily free summon")
    global_utils.click_image(templates.epic_seven_confirm_free_summon, 2)
    if global_utils.click_image(templates.epic_seven_confirm_free_summon_2, 2) == 1:
        time.sleep(20)
        logging.info("Leaving free summon")
        global_utils.click_image(templates.epic_seven_go_back_free_summon, 2)
    logging.info("Leaving summon")
    global_utils.click_image(templates.epic_seven_go_back_summon, 2)
    global_utils.click_image(templates.epic_seven_go_back_summon, 2)
