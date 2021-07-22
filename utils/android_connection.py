import os
import subprocess
import time
import config
import logging


def connect(connectTime):
    subprocess.Popen(config.path+'\\Nox.exe')
    time.sleep(connectTime)
    os.chdir(config.path)
    device = os.popen("adb devices").read().split(
        '\n', 1)[1].split("device")[0].strip()
    logging.info("Waiting for connection ...")
    connect_result = os.popen("adb connect " + device).read()
    logging.info(connect_result)
