import time
from pymata4 import pymata4
import pyautogui
from datetime import datetime

ctr = 0
speed = 18
left_trig = 8
left_echo = 9

right_trig = 2
right_echo = 3

bottom_trig = 4
bottom_echo = 5

top_trig = 10
top_echo = 13

scroll_echo = 12
scroll_trig = 11

distance = [0, 0, 0, 0, 0]
board = pymata4.Pymata4()


def left_call(data):
    global ditance
    distance[0] = data[2]


def right_call(data):
    global distance
    distance[1] = data[2]


def bottom_call(data):
    global distance
    distance[2] = data[2]


def top_call(data):
    global distance
    distance[3] = data[2]


def scroll_call(data):
    global distance
    distance[4] = data[2]


def printer():
    global distance
    x_pos = pyautogui.position()[0]
    y_pos = pyautogui.position()[1]
    time_now = datetime.now()
    temp = str(time_now)[:18]
    print(distance)
    if distance[3] < 30 and distance[4] < 30:
        temp = 40
        pyautogui.scroll(80)
        time.sleep(0.1)
        return
    elif distance[0] < 30 and distance[3] < 30:
        time.sleep(1)
        if distance[0] < 30 and distance[3] < 30:
            pyautogui.click()
            time.sleep(2)
        return
    elif distance[1] < 30 and distance[2] < 30:
        time.sleep(1)
        if distance[1] < 30 and distance[2] < 30:
            pyautogui.click(button='right')
            time.sleep(2)
        return
    elif distance[1] < 30 and distance[4] < 30:
        pyautogui.scroll(-80)
        time.sleep(0.1)
        return
    else:
        if distance[3] < 30:
            time.sleep(1)
            if distance[3] < 30:
                pyautogui.press('f11')
            return
        elif distance[0] < 30:
            time.sleep(1)
            if distance[0] < 30:
                pyautogui.keyDown('alt')
                pyautogui.press('left')
                pyautogui.Keyup('alt')
            time.sleep(0.1)
            return
        elif distance[1] < 30:
            pyautogui.moveTo(
                x_pos+(speed/distance[1]), y_pos, duration=0.000001)
            time.sleep(0.1)
            return
        elif distance[2] < 30:
            time.sleep(1)
            if distance[2] < 30:

                pyautogui.screenshot(temp+'.png')
                time.sleep(0.1)
            return


board.set_pin_mode_sonar(left_trig, left_echo, left_call)
board.set_pin_mode_sonar(right_trig, right_echo, right_call)
board.set_pin_mode_sonar(top_trig, top_echo, top_call)
board.set_pin_mode_sonar(bottom_trig, bottom_echo, bottom_call)
board.set_pin_mode_sonar(scroll_trig, scroll_echo, scroll_call)

while True:
    try:
        time.sleep(0.000001)
        board.sonar_read(left_trig)
        time.sleep(0.000001)
        board.sonar_read(right_trig)
        time.sleep(0.000001)
        board.sonar_read(top_trig)
        time.sleep(0.000001)
        board.sonar_read(bottom_trig)
        time.sleep(0.000001)
        board.sonar_read(scroll_trig)
        printer()
    except Exception:
        board.shutdown()
