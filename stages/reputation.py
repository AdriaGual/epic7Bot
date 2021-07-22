import templates
from utils import global_utils
import logging


def start_reputation():
    logging.warning("----------------")
    logging.warning("---REPUTATION---")
    logging.warning("----------------")
    global_utils.click_position(1500, 618, 1, "Entering Battle")
    global_utils.click_position(407, 818, 6, "Enter reputation")
    global_utils.click_position(1379, 149, 2, "Daily 3 sisters")
    global_utils.click_position(877, 149, 2, "Daily rewards")
    global_utils.click_position(1150, 227, 2, "Receive 100 daily reward")
    global_utils.click_position(1150, 227, 2, "Receive 100 daily reward")
    global_utils.click_position(1017, 227, 2, "Receive 80 daily reward")
    global_utils.click_position(1017, 227, 2, "Receive 80 daily reward")
    global_utils.click_position(830, 227, 2, "Receive 50 daily reward")
    global_utils.click_position(830, 227, 2, "Receive 50 daily reward")
    global_utils.click_position(696, 227, 2, "Receive 30 daily reward")
    global_utils.click_position(696, 227, 2, "Receive 30 daily reward")
    global_utils.click_position(640, 223, 2, "Receive 20 daily reward")
    global_utils.click_position(640, 223, 2, "Receive 20 daily reward")
    global_utils.click_position(575, 223, 2, "Receive 10 daily reward")
    global_utils.click_position(575, 223, 2, "Receive 10 daily reward")
    global_utils.click_position(1050, 149, 2, "Weekly rewards")
    global_utils.click_position(1144, 227, 2, "Receive 100 weekly reward")
    global_utils.click_position(1144, 227, 2, "Receive 100 weekly reward")
    global_utils.click_position(1015, 227, 2, "Receive 80 weekly reward")
    global_utils.click_position(1015, 227, 2, "Receive 80 weekly reward")
    global_utils.click_position(893, 227, 2, "Receive 60 weekly reward")
    global_utils.click_position(893, 227, 2, "Receive 60 weekly reward")
    global_utils.click_position(765, 227, 2, "Receive 40 weekly reward")
    global_utils.click_position(765, 227, 2, "Receive 40 weekly reward")
    global_utils.click_position(638, 227, 2, "Receive 20 weekly reward")
    global_utils.click_position(638, 227, 2, "Receive 20 weekly reward")
    global_utils.click_position(1376, 270, 2, "Remember chain")
    while global_utils.click_image(templates.epic_seven_receive_reputation_reward, 2) == 1:
        global_utils.click_position(810, 717, 2, "Close popup")
    global_utils.click_position(1376, 390, 2, "Conclave")
    while global_utils.click_image(templates.epic_seven_receive_reputation_reward, 2) == 1:
        global_utils.click_position(810, 717, 2, "Close popup")
    global_utils.click_position(1376, 523, 2, "Mercaderes")
    while global_utils.click_image(templates.epic_seven_receive_reputation_reward, 2) == 1:
        global_utils.click_position(810, 717, 2, "Close popup")
    global_utils.click_position(1376, 523, 2, "CCI Fantom")
    while global_utils.click_image(templates.epic_seven_receive_reputation_reward, 2) == 1:
        global_utils.click_position(810, 717, 2, "Close popup")
    global_utils.click_position(100, 50, 2, "Go back reputation")
