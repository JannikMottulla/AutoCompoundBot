import pyautogui
import time
from datetime import datetime


class AdvancedCompoundingBot:
    def __init__(self):
        self.timers = {}

    def compound(self):
        time.sleep(1)
        compound_button_location = pyautogui.locateOnScreen(
            'compound-button.png', confidence=0.95)
        if compound_button_location != None:
            print("compound button found")
            compound_button_location_center = pyautogui.center(
                compound_button_location)
            pyautogui.click(compound_button_location_center.x,
                            compound_button_location_center.y)
            time.sleep(2)
            pyautogui.click(2855, 865)
            time.sleep(1)
            pyautogui.scroll(-200)
            time.sleep(1)
            pyautogui.click(2944, 1120)
            time.sleep(20)
            compound_success = self.check_if_compound_succes()
            if compound_success == True:
                return True
        print('compound button not found or not ready')
        return True

    def check_if_compound_succes(self):
        return pyautogui.locateOnScreen('mm.png', confidence=0.85) == None and pyautogui.locateOnScreen('ready.png', confidence=0.95) != None

    def cycle(self):
        while True:
            if not self.compound():
                print("breaking")
                break


x = AdvancedCompoundingBot()
x.cycle()
