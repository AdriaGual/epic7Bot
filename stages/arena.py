import os
import time
import templates
from utils import global_utils
import logging


def start_arena(times):
    logging.warning("-----------")
    logging.warning("---ARENA---")
    logging.warning("-----------")

    while global_utils.click_image(templates.epic_seven_arena, 2) == 0:
        logging.info("Entering arena")
        global_utils.click_position(1500, 618, 1, "Entering Battle")
    logging.info("Choosing normal arena")
    global_utils.click_image(templates.epic_seven_enter_arena, 4)
    logging.info("Choosing normal arena")
    global_utils.click_image(templates.epic_seven_enter_arena, 4)
    logging.info("Collecting gems rewards")
    global_utils.click_image(templates.epic_seven_arena_gems_reward, 2)
    logging.info("Confirming gems rewards")
    global_utils.click_image(templates.epic_seven_arena_receive_rewards, 2)
    counter = 0
    while counter < times:
        while global_utils.click_image(templates.epic_seven_pnj_fight, 2) == 0:
            logging.info("Autoplay")
        if global_utils.click_image(templates.epic_seven_arena_pnj_fight, 2) == 1:
            npc_arena_fight()
        else:
            os.system("adb shell input swipe 1057 856 1057 156 200")
            time.sleep(2)
            if global_utils.click_image(templates.epic_seven_arena_pnj_fight, 2) == 1:
                npc_arena_fight()
            else:
                logging.info("No NPC fights found, going to PVP")
                find_pvp_fight()
        counter = counter + 1
    global_utils.click_position(87, 58, 2, "Leaving arena")


def npc_arena_fight():
    global_utils.click_position(1050, 830, 4, "Start NPC Fight")
    global_utils.click_position(1050, 830, 2, "Start NPC Fight")
    if global_utils.click_image(templates.epic_seven_gems_required_arena, 2) == 1:
        arena_no_flags()
    else:
        global_utils.click_position(1512, 10, 10, "Passing dialog")
        while global_utils.click_image(templates.epic_seven_autoplay_button, 2) == 0:
            logging.info("Autoplay")
        while global_utils.click_image(templates.epic_seven_skip_arena, 2) == 0:
            logging.info("Closing fight")
        global_utils.click_position(1470, 832, 2, "End NPC fight")
        global_utils.click_position(1470, 832, 4, "End NPC fight")


def arena_no_flags():
    global_utils.click_position(620, 650, 2, "0 PVP Flags")
    global_utils.click_position(80, 40, 2, "0 PVP Flags")


def pvp_arena_fight():
    logging.info("Finding PVP Fight")
    time.sleep(2)
    if global_utils.click_image(templates.epic_seven_arena_pnj_fight, 2) == 1:
        logging.info("PVP battle found")
        if global_utils.click_image(templates.epic_seven_arena_pnj_fight_2, 4) == 1:
            if global_utils.click_image(templates.epic_seven_gems_required_arena, 10) == 1:
                arena_no_flags()
            else:
                logging.info("Autoplay")
                time.sleep(10)
                os.system("adb shell input tap 1407 40")
                while global_utils.click_image(templates.epic_seven_pvp_confirm_end, 2) == 0:
                    logging.info("Closing fight")
                    time.sleep(5)
                global_utils.click_position(794, 870, 6, "League update")
                os.system("adb shell input tap 1470 870")
                time.sleep(2)
    else:
        global_utils.click_image(templates.epic_seven_refresh_arena_pvp, 2)
        global_utils.click_position(880, 622, 2, "Update PVP Rivals")
        time.sleep(2)
        if global_utils.click_image(templates.epic_seven_arena_pnj_fight, 2) == 1:
            logging.info("PVP battle found")
            if global_utils.click_image(templates.epic_seven_arena_pnj_fight_2, 4) == 1:
                if global_utils.click_image(templates.epic_seven_gems_required_arena, 10) == 1:
                    arena_no_flags()
                else:
                    logging.info("Autoplay")
                    time.sleep(10)
                    os.system("adb shell input tap 1407 40")
                    while global_utils.click_image(templates.epic_seven_pvp_confirm_end, 2) == 0:
                        logging.info("Closing fight")
                        time.sleep(5)
                    global_utils.click_position(794, 870, 6, "League update")
                    os.system("adb shell input tap 1470 870")
                    time.sleep(2)


def find_pvp_fight():
    global_utils.click_position(1393, 150, 4, "Choose Rivals")
    pvp_arena_fight()
