import utilities

def make_creature(canvas, center, size=100, tag='untagged', primary_color='#654321', secondary_color='#e6cc8c', ):
    # make ears
    left_ear_position = (center[0]-size, center[1]-size/5)
    right_ear_position = (center[0]+size, center[1]-size/5)
    ear_size = size/2
    utilities.make_circle(canvas, left_ear_position, ear_size, primary_color, tag=tag, outline=primary_color)
    utilities.make_circle(canvas, right_ear_position, ear_size, primary_color, tag=tag, outline=primary_color)

    # make head
    utilities.make_circle(canvas, center, size, primary_color, tag=tag, outline=primary_color)

    # make face
    left_eye_position = (center[0]-size/5, center[1]-size/10)
    right_eye_position = (center[0]+size/5, center[1]-size/10)
    lower_skin_position = (center[0], center[1]+size/2)
    skin_size = size/2
    utilities.make_circle(canvas, left_eye_position, skin_size, secondary_color, tag=tag, outline=secondary_color)
    utilities.make_circle(canvas, right_eye_position, skin_size, secondary_color, tag=tag, outline=secondary_color)
    utilities.make_circle(canvas, lower_skin_position, skin_size, secondary_color, tag=tag, outline=secondary_color)

    # make eyes
    eye_size = size/6
    pupil_size = size/30
    utilities.make_circle(canvas, left_eye_position, eye_size, '#ffffff', tag=tag, outline='#ffffff')
    utilities.make_circle(canvas, left_eye_position, pupil_size, '#000000', tag=tag, outline='#000000')
    utilities.make_circle(canvas, right_eye_position, eye_size, '#ffffff', tag=tag, outline='#ffffff')
    utilities.make_circle(canvas, right_eye_position, pupil_size, '#000000', tag=tag, outline='#000000')

    # make mouth
    mouth_position = (center[0]+size/5, center[1]+size*0.66)
    mouth_size = size/18
    utilities.make_circle(canvas, mouth_position, mouth_size, '#000000', tag=tag, outline='#000000')

def make_landscape_object(canvas, center, size=75, tag='untagged', bark_color='#d4b863', leaves_color='#3b912c'):
    '''Makes a tree
    Changing the size changes the size of the leaves'''
    # make trunk
    utilities.make_rectangle(canvas, center, 50, 160, bark_color)

    # make leaves
    utilities.make_oval(canvas, (center[0]+0,center[1]+0), size, size/2, leaves_color, outline=leaves_color)
    utilities.make_oval(canvas, (center[0]+size/2,center[1]+0), size, size/2, leaves_color, outline=leaves_color)
    utilities.make_oval(canvas, (center[0]+size/3,center[1]-size/2), size, size/2, leaves_color, outline=leaves_color)

def make_cloud(canvas, center, speed=0, size=40, tag='untagged', color='#ffffff'):
    # make cloud
    utilities.make_oval(canvas, center, size, size/2, color, tag, outline=color)
    utilities.make_circle(canvas, (center[0], center[1]-size/2), size/2, color, tag, outline=color)

def make_sun(canvas, center, size=100, tag='sun', color="#e5ff00"):
    # make sun
    utilities.make_circle(canvas, center, size, color, tag, outline=color)

def make_moon(canvas, center, size=50, tag='moon', color="#ffffff"):
    # make moon
    utilities.make_circle(canvas, center, size, color, tag, outline=color)