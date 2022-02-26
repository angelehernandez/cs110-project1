from ctypes import util
import string
from tkinter import Canvas, Tk
import helpers
import utilities
import helpers
import time
import random

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width,
                height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

def make_world(canvas, morning_color='#4beff2', night_color='#3b46c4', tag='sky', duration=5):
    '''Makes everything'''
    # start timer
    start = time.time()
    
    # make morning sky
    setting = 'morning'
    utilities.make_rectangle(canvas, (0, 0), 2000, 2000, morning_color, tag=tag)

    # loop day and night
    while True:
        time_elapsed = round(time.time() - start)

        # morning to night
        if setting == 'morning' and time_elapsed == duration:
            # reset conditionals
            start = time.time()
            setting = 'night'

            # add background
            utilities.make_rectangle(canvas, (0, 750), 2000, 300, '#573a0f')
            helpers.make_landscape_object(canvas, (100,600), bark_color='#6b581d', leaves_color='#1c5711')
            helpers.make_landscape_object(canvas, (540,600), bark_color='#6b581d', leaves_color='#1c5711')
            helpers.make_landscape_object(canvas, (700,600), 110, bark_color='#6b581d', leaves_color='#1c5711')
            helpers.make_landscape_object(canvas, (900,600), 90, bark_color='#6b581d', leaves_color='#1c5711')
            helpers.make_landscape_object(canvas, (1130,600), 125, bark_color='#6b581d', leaves_color='#1c5711')
            helpers.make_landscape_object(canvas, (300,600), 130, bark_color='#6b581d', leaves_color='#1c5711')
            helpers.make_landscape_object(canvas, (1320,600), 50, bark_color='#6b581d', leaves_color='#1c5711')

            # update gui
            utilities.update_fill_by_tag(canvas, tag, night_color)
            gui.update()
            continue

        # night to morning
        elif setting == 'night' and time_elapsed == duration:
            # reset conditionals
            start = time.time()
            setting = 'morning'

            # add background
            utilities.make_rectangle(canvas, (0, 750), 2000, 300, '#573a0f')
            helpers.make_landscape_object(canvas, (100,600))
            helpers.make_landscape_object(canvas, (540,600))
            helpers.make_landscape_object(canvas, (700,600), 110)
            helpers.make_landscape_object(canvas, (900,600), 90)
            helpers.make_landscape_object(canvas, (1130,600), 125)
            helpers.make_landscape_object(canvas, (300,600), 130)
            helpers.make_landscape_object(canvas, (1320,600), 50)

            # update gui
            utilities.update_fill_by_tag(canvas, tag, morning_color)
            gui.update()
            continue

        # make floor
        utilities.make_rectangle(canvas, (0, 1000), 2000, 50, 'brown')

# main
make_world(canvas)

# canvas.bind('<b-Button-1>', click_handle) # this doesnt work
# while True:


########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
