from utils import global_utils
import logging


def start_guild():
    logging.warning("-----------")
    logging.warning("---GUILD---")
    logging.warning("-----------")
    global_utils.click_position(1500, 618, 1, "Entering Battle")
    global_utils.click_position(644, 822, 2, "Enter Guild")
    global_utils.click_position(1116, 822, 4, "Daily reward")
    global_utils.click_position(50, 50, 6, "Go back guild")
