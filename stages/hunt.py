import os
import time
import templates
from stages import stage_replay
from utils import global_utils
import logging


def start_hunt(max_replays):
    logging.warning("----------")
    logging.warning("---HUNT---")
    logging.warning("----------")
    global_utils.click_position(1500, 618, 2, "Refresh")
    global_utils.click_position(1500, 618, 2, "Refresh")
    global_utils.click_position(1500, 618, 4, "Refresh")
    global_utils.click_position(1500, 618, 4, "Refresh")
    global_utils.click_position(1330, 816, 6, "Enter Battle")
    global_utils.click_position(970, 780, 4, "Enter Hunt")
    global_utils.click_position(1058, 276, 4, "Wyvern Hunt")
    while global_utils.click_image(templates.epic_seven_hunt_level_11, 2) == 0:
        logging.info("Looking for level 11")
    global_utils.click_position(1400, 840, 4, "Team")
    counter = 0
    unlimited_replay = 0
    if max_replays < 0:
        unlimited_replay = 1
    while counter < max_replays or unlimited_replay == 1:
        if global_utils.click_image(templates.epic_seven_arena_pnj_fight_2, 4) == 1:

            while global_utils.click_image(templates.epic_seven_stage_clear, 5) == 0:
                logging.info("Retry finish fight")
            while global_utils.click_image(templates.epic_seven_confirm_hunt_2, 2) == 0:
                global_utils.click_position(932, 290, 4, "Confirm")
            global_utils.click_image(templates.epic_seven_confirm_hunt, 2)
            while global_utils.click_image(templates.epic_seven_hunt_another_time, 2) == 0:
                logging.info("Retry another time")
            counter = counter + 1

    global_utils.click_position(50, 50, 4, "Go back")
    global_utils.click_position(150, 840, 4, "Go back")
    global_utils.click_position(50, 50, 4, "Go back")
    global_utils.click_position(50, 50, 4, "Go back")
