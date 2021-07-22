import os
import time
import templates
from utils import global_utils
import logging


def start_open():
    logging.warning("----------------")
    logging.warning("---EPIC SEVEN---")
    logging.warning("----------------")
    time.sleep(2)
    while global_utils.click_image(templates.epic_seven_logo, 1) == 0:
        logging.info("Waiting Nox")
    while global_utils.click_image(templates.epic_seven_start, 1) == 0:
        logging.info("Loading E7")
    logging.info("Merurina Reward")
    global_utils.click_image(templates.epic_seven_confirm_merurina_reward, 4)
    logging.info("Helping points Reward")
    global_utils.click_image(templates.epic_seven_helping_points_reward, 2)
    global_utils.click_image(templates.epic_seven_another_time, 2)
    global_utils.click_position(35, 353, 2, "refresh")
    global_utils.click_image(templates.epic_seven_another_time, 2)
    logging.info("Closing collab")
    global_utils.click_image(templates.epic_seven_confirm_close_popup, 2)
    logging.info("Closing collab")
    global_utils.click_image(templates.epic_seven_confirm_close_popup, 2)
    logging.info("Closing offer")
    global_utils.click_position(35, 353, 2, "refresh")
    global_utils.click_image(templates.epic_seven_close_offer, 2)
    logging.info("Closing first popup")
    global_utils.click_image(templates.epic_seven_another_time, 2)
    global_utils.click_position(35, 353, 2, "refresh")
    global_utils.click_image(templates.epic_seven_another_time, 2)
    global_utils.click_image(templates.epic_seven_close_popup, 2)
    global_utils.click_image(templates.epic_seven_close_popup, 2)
    global_utils.click_position(35, 353, 2, "refresh")
    global_utils.click_image(templates.epic_seven_close_popup, 2)
    global_utils.click_image(templates.epic_seven_close_popup, 2)
    global_utils.click_image(templates.epic_seven_close_popup, 2)
    global_utils.click_position(35, 353, 2, "refresh")
    global_utils.click_image(templates.epic_seven_another_time, 2)
    global_utils.click_image(templates.epic_seven_another_time, 2)
    global_utils.click_position(1540, 630, 2, "refresh")
    global_utils.click_position(35, 353, 2, "refresh")
    logging.info("Opening treasure")
    global_utils.click_image(templates.epic_seven_treasure, 2)