""" HIT137 Assignment 2 Group 74 """
####
# Group 74

# STUDENT NAME: MD AL AMIN SARKER
# STUDENT NUMBER: S361035

# STUDENT NAME: SHIVA GUPTA
# STUDENT NUMBER: S361033

# Youtube link: https://youtu.be/A9fN7cfdNp8
####

from turtle import*  # importing turtle library
import random       # importing random to generate stars


def setup_drawing_board():
    """ Setting up screen/window """

    setup(1000, 700)  # screen or window size width=1000, height=700
    speed(0)        # speed of the turtle | (‘fastest’ :  0), range 0-10
    bgcolor("black")  # background color for window
    title("Starry Night On The Mountain") # title for trutle window


def draw_land():
    """ Drawing land in th bottom portion of the graphics window """

    penup()  # penup for moving the turtle without drawing
    goto(-500, -100)   # moving to the position x=-500, y=-100 
    pendown()   # pendown so that we can start drawing
    color("#786c5e")    # setting turtle color with color code similer to soil
    # drawing shape to be filled
    begin_fill() 
    for i in range(2):
        forward(1000)   # move turtle forward with distance 1000 in the direction of head of turtle
        right(90)   # changing direction by 90 degrees to the right (clock wise)
        forward(300)    # move turtle forward with distance 300
        right(90)   # changing direction by 90 degrees to the right (clock wise)
    end_fill()
    # shape filled end


def draw_star():
    """ Drawing a star """

    color("yellow") #stting turtle color to yellow
    # drawing shape to be filled with turtle color
    begin_fill()
    # loop to draw star
    for i in range(5):
        forward(10)  # moving forward with distance 10
        right(144)  # changing direction by 144 degrees to the right (clock wise)
    end_fill()
    # shape filled end after star drawing finished


def draw_random_star(number_of_star):
    """ Drawing stars in random locations """

    # loop to draw number of stars given in parameter
    for i in range(number_of_star):
        x = random.randint(-500, 500)   # getting random x coordinates from -500 to 500
        y = random.randint(50, 300)      # getting random y coordinates from 50 to 300
        penup() # penup to move the turtle without drawing
        goto(x, y)  # moving turtle to the position selected randomly
        pendown()  # pendown so that we can draw
        draw_star()  # calling draw_star() function to draw a star on our selected location


def draw_mountain(x, y, move_forward, move_left):
    """Drawing mountain"""

    penup() # penup so that we can move the turtle without drawing
    goto(x, y)  # moving turtle to the position given in parameter
    pendown()   # pendown so that we can draw 
    color("dimgray")    # setting color for mountain
    # shape to be filled with turtle color for mountain
    begin_fill()
    for i in range(3):  # looping 3 times for triangle
        forward(move_forward)   # moving forward with distance given in parameter
        left(move_left)     # change the direction of turtle by given degrees in parameter to the left (anti clock)
    end_fill()
    # shape filled end


def middle_mountain_ice_cap():
    """ Drawing middle mountain ice cap """

    penup()  # penup so that we can move the turtle without drawing
    goto(-35, 120)  # moving turtle to the position x=-35, y=120 
    pendown() # pendown for start drawing
    color("white") # setting color for ice cap
    # begin to fill ice cap with white color
    begin_fill() 
    left(35)    # change the direction of turtle by 35 degrees to the left (anti clock wise)
    forward(60) # moving forward with distance 60
    right(90)   # changing direction by 90 degrees to the right (clock wise)
    forward(30) # moving forward with distance 30
    left(100)   # changing direction of turtle by 100 degrees to the left (anti clock)
    forward(45) # moving forward with distance 45
    right(85)   # changing direction by 85 degrees to the right (clock wise)
    forward(65) # moving forward with distance 65
    left(160)   # changing direction by 160 degrees to the left (anti clock)
    forward(150) # moving forward with distance 150
    end_fill()  # shape filled end

def left_mountain_ice_cap():
    """ Drawing left side mountain ice cap """

    penup() # penup for moving the turtle without drawing
    goto(-215, 100)  # moving turtle to the location x=-215, y=100 
    pendown()   # pendown for start drawing
    #color("white") # no need to set color as already color is white
    begin_fill()  # begin to fill ice cap with white color
    forward(70)  # moving trutle forward with distance 70
    left(120)   # change the direction of turtle by 120 degrees to the left (anti clock wise)
    forward(75) # moving forward with distance 75
    left(150)   # change the direction of turtle by 120 degrees anti clock wise
    forward(45) # moving forward with distance 45
    right(90)   # changing direction by 90 degrees to the right (clock wise)
    forward(45) # moving forward with distance 45
    left(120)   # anti clock wise 120 degrees
    end_fill()  # ending fill the shape


def right_mountain_ice_cap():
    """ Drawing right side mountain ice cap """
    penup() # penup for moving the turtle without drawing
    goto(203, 80) # moving turtle to the location x=103, y=80 to start drawing 
    pendown()   # pendown for start drawing
    begin_fill()  # begin to fill ice cap with white color, turtle color is white already
    forward(95) # moving forward with distance 95
    right(120)  # changing direction by 120 degrees to the right (clock wise)
    forward(80) # moving forward with distance 80
    right(150)  # changing turtle direction by 150 degrees clock wise
    forward(50) # moving forward with distance 50
    left(70)    # changing direction anti clock wise 120 degrees
    end_fill()  # shape filling end

def draw_moon():
    """ Drawing the moon """
    penup() # penup for moving the turtle without drawing
    goto(-420, 300)  # moving turtle to the location x=-420, y=300
    pendown()   # pendown for start drawing
    color("orange") #setting turtle color to orange
    begin_fill()    # start filling shape
    circle(70)  # drawing circle with radius 70
    end_fill()  # end filling shape with orange color

    #changing the moon sahpe to partial eclipse
    penup() # penup for moving the turtle without drawing
    goto(-410, 320) # moving turtle to the location x=-420, y=320
    color('black') # setting turtle color to black
    begin_fill()    # start filling the shape
    circle(70)   # drawing circle with radius 70
    end_fill()  # end of filling shape


def fractal_tree(branch_length):
    """ Drawing a frctal tree with recursion """

    if branch_length > 5:  # checking if branch_length is greater than 5 or not
        forward(branch_length)  # moving forward with branch length
        right(20)   # changing direction by 85 degrees to the right (clock wise)
        fractal_tree(branch_length-5)  # recursion call
        left(40)    # changing direction anti clock wise by 40 degrees
        fractal_tree(branch_length-5)  # recursion call for ther side
        right(20)   # changing direction by 20 degrees clock wise
        backward(branch_length)     # moving turtle backward with distance = branch_length

def draw_tree(x, y, pen_size, branch_len):
    """ Drawing tree with properties given in parameter """

    penup() # penup for moving the turtle without drawing
    goto(x, y)  # moving turtle to the coordinates where wants the tree 
    pendown()   # pendown for start drawing
    color("#023020") # setting color for trees to deep green color code
    pensize(pen_size)   # setting pen size for tree width
    fractal_tree(branch_len) # calling fractal_tree function to draw the fractal tree


# driver code
setup_drawing_board() # sttting up drawing window
draw_land() # drawing land
draw_random_star(30)    # drawing random star

draw_mountain(-400, -100, 300, 120) # drawing left mountain
draw_mountain(100, -100, 300, 120)  # drawing right mountain
draw_mountain(-160, -100, 400, 120) # drawing middle mountain

# drawing ice caps on mountains
middle_mountain_ice_cap()
left_mountain_ice_cap()
right_mountain_ice_cap()

draw_moon() # drawing moon

# drawing trees
right(130)  # changing turtle's direction by 130 degrees clock wise
draw_tree(-350, -270, 5.5, 40)    # tree1
draw_tree(-150, -200, 4.5, 30)    # tree 2
draw_tree(-50, -140, 3.5, 30)    # tree 3
draw_tree(100, -180, 4, 35)     # tree 4
draw_tree(320, -220, 4.5, 35)  # tree 5

hideturtle() # hidding turtle

delay = input("Press enter to finish.")
