from __future__ import print_function, division
from time import sleep
import os
import sys
import time
from PIL import Image


if sys.version_info.major != 3:
    print('Please run under Python3')
    exit(1)

#请确保位于新浪微博的手机app关注页

def follow():
    x = 970
    os.system('adb shell input tap {} 480 '.format(x))
    sleep(0.3)
    os.system('adb shell input tap {} 480 '.format(x+800))
    sleep(0.3)
    os.system('adb shell input swipe 655 1800 822 1070')
    sleep(0.3)

    for i in range(100):
        follow()



follow()