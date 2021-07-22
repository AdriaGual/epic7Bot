import time
import templates
from utils import global_utils
import logging


def start_sanctuary():
    logging.warning("---------------")
    logging.warning("---SANCTUARY---")
    logging.warning("---------------")
    global_utils.click_position(100, 150, 1, "refresh")
    global_utils.click_position(100, 150, 1, "refresh")
    logging.info("Entering sanctuary")
    global_utils.click_image(templates.epic_seven_go_to_sanctuary, 10)
    time.sleep(2)
    logging.info("Getting gems")
    global_utils.click_image(templates.epic_seven_get_gems_sanctuary, 5)
    logging.info("Confirming get gems")
    global_utils.click_image(
        templates.epic_seven_confirm_received_sanctuary_gems, 5)
    logging.info("Opening sanctuary forest")
    global_utils.click_image(templates.epic_seven_open_sanctuary_forest, 5)
    summon_forest_creature()
    summon_forest_creature()
    summon_forest_creature()
    refill_forest_creature()
    refill_forest_creature()
    refill_forest_creature()
    logging.info("Leaving forest")
    global_utils.click_image(templates.epic_seven_go_back_forest, 2)
    logging.info("Leaving sanctuary")
    global_utils.click_image(templates.epic_seven_go_back_sanctuary, 2)


def summon_forest_creature():
    logging.info("Summoning forest creature")
    global_utils.click_image(templates.epic_seven_summon_forest_creature, 5)


def refill_forest_creature():
    if global_utils.click_image(templates.epic_seven_choose_forest_creature, 5) == 1:
        global_utils.click_position(1250, 520, 2, "Refilling forest creature")
