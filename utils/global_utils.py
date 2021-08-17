import base64
import os
import time
import cv2
import numpy as np
import logging


def click_position(x, y, waitTime, message):
    time.sleep(waitTime)
    logging.info(message)
    os.system("adb shell input tap " + str(x) + " " + str(y))
    logging.info('Input tap at position: [ %s , %s ]',  str(x), str(y))

# templateName -- Image name that you're searching
# Returns 1 if found (and clicked the image)


def click_image(template, waitTime):
    time.sleep(waitTime)
    command = "adb shell \"screencap -p | busybox base64\""
    pcommand = os.popen(command)
    png_screenshot_data = pcommand.read()
    png_screenshot_data = base64.b64decode(png_screenshot_data)
    pcommand.close()
    images = cv2.imdecode(np.frombuffer(png_screenshot_data, np.uint8), 0)
    result = cv2.matchTemplate(images, template, cv2.TM_CCOEFF_NORMED)
    position_x = np.unravel_index(result.argmax(), result.shape)[1]
    position_y = np.unravel_index(result.argmax(), result.shape)[0]
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.8:
        os.system("adb shell input tap " +
                  str(position_x) + " " + str(position_y))
        logging.info('Found at position: [ %s , %s ]', str(
            position_x), str(position_y))
        return 1
    else:
        return 0


def click_image_loop(template, waitTime):
    while click_image(template, waitTime) == 0:
        logging.warning('Not found: %s', template[0])
