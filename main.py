from ctypes import util
from email import utils
import string
from tkinter import Canvas, Tk
import helpers
import utilities
import helpers
import time
import random
import math

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width,
                height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# initialize oscillations
# oscillations = range

def make_world(canvas, morning_color='#4beff2', night_color='#3b46c4', tag='sky', duration=5):
    '''Makes everything'''
    # start timer
    start = time.time()
    
    # make morning sky
    setting = 'morning'
    utilities.make_rectangle(canvas, (0, 0), 2000, 2000, morning_color, tag=tag)
    helpers.make_cloud(canvas, (200, 300), size=30, tag='cloud1')
    helpers.make_cloud(canvas, (600, 400), size=100, tag='cloud2')
    helpers.make_cloud(canvas, (200, 100), size=60, tag='cloud3')
    helpers.make_cloud(canvas, (600, 250), size=130, tag='cloud4')

    # make background
    utilities.make_rectangle(canvas, (0, 750), 2000, 300, '#573a0f')
    helpers.make_landscape_object(canvas, (100,600))
    helpers.make_landscape_object(canvas, (540,600))
    helpers.make_landscape_object(canvas, (700,600), 110)
    helpers.make_landscape_object(canvas, (900,600), 90)
    helpers.make_landscape_object(canvas, (1130,600), 125)
    helpers.make_landscape_object(canvas, (300,600), 130)
    helpers.make_landscape_object(canvas, (1320,600), 50)

    # make monkeys
    helpers.make_creature(canvas, (200, 600), 50, 'monkey1')
    monkey1_direction = 'down'
    helpers.make_creature(canvas, (500, 600), 50, 'monkey2')
    monkey2_x_direction = 'right'
    helpers.make_creature(canvas, (800, 650), 50, 'monkey3')
    monkey3_direction = 'up'
    helpers.make_creature(canvas, (1300, 600), 50, 'monkey4')
    monkey4_x_direction = 'left'

    # animation loop
    while True:
        time_elapsed = round(time.time() - start)

        # cloud logic
        cloud1_left_coord = utilities.get_left(canvas, 'cloud1')
        if cloud1_left_coord >= window_width:
            utilities.update_position_by_tag(canvas, 'cloud1', window_width*-1, 0)
        cloud2_left_coord = utilities.get_left(canvas, 'cloud2')
        if cloud2_left_coord >= window_width:
            utilities.update_position_by_tag(canvas, 'cloud2', window_width*-1, 0)
        cloud3_right_coord = utilities.get_right(canvas, 'cloud3')
        if cloud3_right_coord <= 0:
            utilities.update_position_by_tag(canvas, 'cloud3', window_width, 0)
        cloud4_right_coord = utilities.get_right(canvas, 'cloud4')
        if cloud4_right_coord <= 0:
            utilities.update_position_by_tag(canvas, 'cloud4', window_width, 0)

        # animate clouds
        utilities.update_position_by_tag(canvas, 'cloud1', x=3, y=0)
        utilities.update_position_by_tag(canvas, 'cloud2', x=3, y=0)
        utilities.update_position_by_tag(canvas, 'cloud3', x=-3, y=0)
        utilities.update_position_by_tag(canvas, 'cloud4', x=-3, y=0)

        # monkey1 logic
        monkey1_y_position = utilities.get_bottom(canvas, 'monkey1')
        if monkey1_direction == 'down':
            utilities.update_position_by_tag(canvas, 'monkey1', x=0, y=1)
            if monkey1_y_position > 750:
                monkey1_direction = 'up'
        if monkey1_direction == 'up':
            utilities.update_position_by_tag(canvas, 'monkey1', x=0, y=-1)
            if monkey1_y_position < 700:
                monkey1_direction = 'down'

        # monkey2 logic
        monkey2_x_position = utilities.get_center(canvas, 'monkey2')
        if monkey2_x_direction == 'right':
            utilities.update_position_by_tag(canvas, 'monkey2', x=1, y=0)
            if monkey2_x_position > 550:
                monkey2_x_direction = 'left'
        if monkey2_x_direction == 'left':
            utilities.update_position_by_tag(canvas, 'monkey2', x=-1, y=0)
            if monkey2_x_position < 450:
                monkey2_x_direction = 'right'

        # monkey3 logic
        monkey3_y_position = utilities.get_bottom(canvas, 'monkey3')
        if monkey3_direction == 'down':
            utilities.update_position_by_tag(canvas, 'monkey3', x=0, y=1)
            if monkey3_y_position > 750:
                monkey3_direction = 'up'
        if monkey3_direction == 'up':
            utilities.update_position_by_tag(canvas, 'monkey3', x=0, y=-1)
            if monkey3_y_position < 700:
                monkey3_direction = 'down'

        # monkey4 logic
        monkey4_x_position = utilities.get_center(canvas, 'monkey4')
        if monkey4_x_direction == 'right':
            utilities.update_position_by_tag(canvas, 'monkey4', x=2, y=0)
            if monkey4_x_position > 1350:
                monkey4_x_direction = 'left'
        if monkey4_x_direction == 'left':
            utilities.update_position_by_tag(canvas, 'monkey4', x=-2, y=0)
            if monkey4_x_position < 1100:
                monkey4_x_direction = 'right'

        gui.update()

        # morning to night
        if setting == 'morning' and time_elapsed == duration:
            # reset conditionals
            start = time.time()
            setting = 'night'

            # change cloud colors
            utilities.update_fill_by_tag(canvas, 'cloud1', color='#5c5c5c')
            utilities.update_fill_by_tag(canvas, 'cloud2', color='#5c5c5c')
            utilities.update_fill_by_tag(canvas, 'cloud3', color='#5c5c5c')
            utilities.update_fill_by_tag(canvas, 'cloud4', color='#5c5c5c')

            # update gui
            utilities.update_fill_by_tag(canvas, tag, night_color)
            gui.update()
            continue

        # night to morning
        elif setting == 'night' and time_elapsed == duration:
            # reset conditionals
            start = time.time()
            setting = 'morning'

            # change cloud colors
            utilities.update_fill_by_tag(canvas, 'cloud1', color='#ffffff')
            utilities.update_fill_by_tag(canvas, 'cloud2', color='#ffffff')
            utilities.update_fill_by_tag(canvas, 'cloud3', color='#ffffff')
            utilities.update_fill_by_tag(canvas, 'cloud4', color='#ffffff')

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
