import templates
from utils import global_utils
import logging


def start_battle_event():
    logging.warning("------------------")
    logging.warning("---BATTLE EVENT---")
    logging.warning("------------------")
    global_utils.click_position(1500, 618, 1, "Entering Battle")
    global_utils.click_position(1330, 816, 4, "Enter Battle")
    if global_utils.click_image(templates.epic_seven_event_cover, 2) == 1:
        global_utils.click_position(
            882, 250, 2, "Choosing Secondary Story Event")
        global_utils.click_position(1369, 843, 2, "Choose Infernal difficulty")
        global_utils.click_position(1369, 843, 2, "Start")
        while global_utils.click_image(templates.epic_seven_no_energy_event, 3) == 0:
            global_utils.click_position(1369, 843, 2, "Start")
            global_utils.click_position(1090, 843, 2, "Start")
            while global_utils.click_image(templates.epic_seven_stage_clear, 3) == 0:
                logging.info("Retry finish fight")
            global_utils.click_position(1500, 817, 2, "Confirm fight results")
            global_utils.click_position(1500, 817, 2, "Fight another time")
            global_utils.click_position(1369, 843, 2, "Start")
        global_utils.click_position(646, 649, 2, "Close refill energy popup")
        global_utils.click_position(60, 60, 2, "Go back battle")
        global_utils.click_position(120, 820, 2, "Go back battle")
        global_utils.click_position(60, 60, 2, "Go back battle")
        global_utils.click_position(60, 60, 2, "Go back battle")
