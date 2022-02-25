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

def make_creature(canvas, center, size=100, tag='untagged', primary_color='#654321', secondary_color='#e6cc8c', ):
    # make ears
    left_ear_position = (center[0]-size, center[1]-size/5)
    right_ear_position = (center[0]+size, center[1]-size/5)
    ear_size = size/2
    utilities.make_circle(canvas, left_ear_position, ear_size, primary_color, tag=tag)
    utilities.make_circle(canvas, right_ear_position, ear_size, primary_color, tag=tag)

    # make head
    utilities.make_circle(canvas, center, size, primary_color, tag=tag)

    # make face
    left_eye_position = (center[0]-size/5, center[1]-size/10)
    right_eye_position = (center[0]+size/5, center[1]-size/10)
    lower_skin_position = (center[0], center[1]+size/2)
    skin_size = size/2
    utilities.make_circle(canvas, left_eye_position, skin_size, secondary_color, tag=tag)
    utilities.make_circle(canvas, right_eye_position, skin_size, secondary_color, tag=tag)
    utilities.make_circle(canvas, lower_skin_position, skin_size, secondary_color, tag=tag)

    # make eyes
    eye_size = size/6
    pupil_size = size/30
    utilities.make_circle(canvas, left_eye_position, eye_size, '#ffffff', tag=tag)
    utilities.make_circle(canvas, left_eye_position, pupil_size, '#000000', tag=tag)
    utilities.make_circle(canvas, right_eye_position, eye_size, '#ffffff', tag=tag)
    utilities.make_circle(canvas, right_eye_position, pupil_size, '#000000', tag=tag)

    # make mouth
    mouth_position = (center[0]+size/5, center[1]+size*0.66)
    mouth_size = size/18
    utilities.make_circle(canvas, mouth_position, mouth_size, '#000000', tag=tag)

def make_landscape_object(canvas, center, size=100, tag='untagged', bark_color='#d4b863', leaves_color='#3b912c'):
    '''Makes a tree'''
    # make trunk
    # utilities.make_rectangle(canvas, )

    # make leaves

def make_world(canvas, morning_color='#4beff2', night_color='#3b46c4', tag='sky', duration=5):
    '''Makes a color changing sky'''
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

            # update gui
            utilities.update_fill_by_tag(canvas, tag, night_color)
            gui.update()
            continue

        # night to morning
        elif setting == 'night' and time_elapsed == duration:
            # reset conditionals
            start = time.time()
            setting = 'morning'

            # update gui
            utilities.update_fill_by_tag(canvas, tag, morning_color)
            gui.update()
            continue

# main
make_world(canvas)

# canvas.bind('<b-Button-1>', click_handle) # this doesnt work
# while True:


########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
