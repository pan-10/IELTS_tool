# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 16:20:13 2023

@author: 20304
"""

from tkinter import Tk  # Python 3
import pyttsx3
run_flag = True
memory_var = '0'
clip = '0'
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
while run_flag:
    try:
        clip = Tk().clipboard_get()
        print(clip)
        clip = clip.split()
    except:
        pass
    if memory_var != clip:
        engine.say(clip)
        engine.runAndWait()
        print(clip)
        memory_var = clip
    
