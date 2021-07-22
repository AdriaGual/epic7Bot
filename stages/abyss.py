from utils import global_utils
import templates
import logging


def start_abyss():
    logging.warning("-----------")
    logging.warning("---ABYSS---")
    logging.warning("-----------")
    global_utils.click_position(1500, 618, 4, "Entering Battle")
    while global_utils.click_image(templates.epic_seven_enter_battle, 2) == 0:
        logging.info("Trying to enter battle")
    global_utils.click_position(905, 490, 2, "Opening Abyss")
    global_utils.click_position(1072, 804, 2, "Enter Abyss")
    global_utils.click_position(158, 832, 2, "Purify")
    global_utils.click_position(960, 656, 2, "Confirm purify")
    global_utils.click_position(794, 677, 2, "Confirm collect abyss")
    global_utils.click_position(71, 71, 4, "Go back abyss")
    global_utils.click_position(100, 71, 4, "Go back abyss")
