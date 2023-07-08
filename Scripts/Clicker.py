# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:26:41 2022

@author: Admin
"""
import time
import random
import pyautogui as ui
import winsound as sound

# %% Setting Positions
ui.size() 
desktop, center = (1920, 1060), (960, 540)  
quad = [(1440, 720), (480, 270), (480, 810), (1440, 810)]
apps = []
x = 590        #Calibrate the x position of the first app here
for i in range(10):
    apps.append((x + 60*i, 1050))
    
# %% Define Functions
def click_wait(pos: tuple, t: int):
    """ Wait for t seconds, click a specific position """
    time.sleep(t)
    ui.click(pos)
    
def scroll_wait(s_min: int, s_max: int, t: int):
    """ Wait for t seconds, scroll down a random amount """
    time.sleep(t)
    amount = random.randint(s_min, s_max)
    ui.scroll(amount)

def alarm(times: int, wait: int):
    """ Produce warning sound at 2000Hz for 2000ms
        times: number of repetition
        wait: interval bewtween each repetition """
    for i in list(range(times)):
        sound.Beep(2000, 2000)
        time.sleep(wait)
        
# %% Initializer (Open all the apps)
time.sleep(5)
for app in apps:
    click_wait(app, 2)

# %% Random Tab Controller
time.sleep(5)
while True:
    try:
        random.shuffle(apps)
        for app in apps:
            q = quad[random.randint(0,3)]
            click_wait(app, 5)
            click_wait(q, 5)
            scroll_wait(-2000, 2000, 5)
    except ui.FailSafeException:
        alarm(3, 3)