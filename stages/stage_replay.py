import os
import time
import templates
from utils import global_utils
import logging


def start_stage_replay(max_replays):
    counter = 0
    unlimited_replay = 0
    if max_replays < 0:
        unlimited_replay = 1

    while counter < max_replays or unlimited_replay == 1:
        global_utils.click_position(1460, 830, 2, "Iniciar")
        time.sleep(4)
        if global_utils.click_image(templates.epic_seven_no_energy_event, 2) == 1:
            global_utils.click_position(916, 640, 4, "Get energy")
            global_utils.click_position(1460, 830, 2, "Iniciar")
        fight()
        counter = counter + 1


def fight():
    while global_utils.click_image(templates.epic_seven_stage_clear, 3) == 0:
        logging.info("Retry finish fight")
    global_utils.click_position(640, 640, 4, "Friendship close")
    global_utils.click_position(1460, 830, 4, "Close Popup")
    global_utils.click_position(883, 226, 4, "Close Popup")
    global_utils.click_position(1460, 830, 4, "Confirm")
    global_utils.click_position(1460, 830, 4, "Equipo")
    global_utils.click_position(1460, 830, 4, "Equipo")
