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
logging.warning("---REPLAY STAGE---")
logging.warning("----------")

while 1:
    while global_utils.click_image(templates.replay_stage_start_button, 1) == 0:
        logging.info("Start")
    global_utils.click_image(templates.leaf_payment, 2)
    global_utils.click_image(templates.replay_stage_start_button, 1)
    while global_utils.click_image(templates.epic_seven_stage_clear, 2) == 0 and global_utils.click_image(templates.epic_seven_stage_failed, 2) == 0:
        logging.info("Stage clear")
    global_utils.click_image(templates.cancel_friend_request, 3)
    while global_utils.click_image(templates.confirm_stage_cleared, 1) == 0:
        logging.info("Confirm stage cleared")
    while global_utils.click_image(templates.another_time, 1) == 0:
        logging.info("Another time")
    global_utils.click_image(templates.confirm_replay_stage, 2)
    while global_utils.click_image(templates.team_replay_stage, 1) == 0:
        logging.info("Team replay stage")
