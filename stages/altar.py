import templates
from utils import global_utils
import logging


def start_altar():
    logging.warning("-----------")
    logging.warning("---ALTAR---")
    logging.warning("-----------")
    global_utils.click_position(1500, 618, 1, "Entering Battle")
    global_utils.click_position(1330, 816, 4, "Enter Battle")
    global_utils.click_position(740, 250, 4, "Enter Altar")
    global_utils.click_position(1060, 300, 4, "Enter Altar Option")
    global_utils.click_position(1440, 820, 4, "Team Select")
    global_utils.click_position(1440, 820, 4, "Start")
    while global_utils.click_image(templates.epic_seven_stage_clear, 3) == 0:
        logging.info("Retry finish fight")
    global_utils.click_position(1440, 820, 4, "Confirm End")
    global_utils.click_position(124, 820, 4, "Go Back")
    global_utils.click_position(50, 50, 4, "Go Back")
    global_utils.click_position(50, 50, 4, "Go Back")
