"""

In this project I will my understanding of animations.
I will attempt to create a pokeball that reveals a pokemon. 


File Name: Abdellatif_Project 4 Animation .py
Author: Rana Abdellatif
Date: 10/09/22
Course: COMP 1351
Assignment: Project 4 - Animation
Collaborators: None
Internet Source: None

"""

import dudraw
import math
dudraw.set_canvas_size(500,500)
dudraw.clear(dudraw.WHITE)


#defines functions that draw the pokeball and pokemon
def pokeball(x_pos,y_pos,x_scale,y_scale):

    r = 0.25
    dudraw.set_pen_color(dudraw.RED)

    dudraw.filled_elliptical_sector(x_scale*0.5+x_pos,y_scale*0.5+y_pos,x_scale*0.1,y_scale*0.1,0,180)
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_elliptical_sector(x_scale*0.5+x_pos,y_scale*0.5+y_pos,x_scale*0.1,y_scale*0.1,180,360)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.filled_circle(x_scale*0.5+x_pos,y_scale*0.5+y_pos,0.025*x_scale)
    dudraw.set_pen_width(0.005)
    dudraw.circle(x_scale*0.5+x_pos,y_scale*0.5+y_pos,0.1*x_scale)
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_circle(x_scale*0.5+x_pos,y_scale*0.5+y_pos,0.015*x_scale)

def jigglypuff(x_pos,y_pos,x_scale,y_scale):
    dudraw.set_pen_color_rgb(245, 157, 189)
    dudraw.filled_circle(x_scale*0.5+x_pos,y_scale*0.5+y_pos,0.25*x_scale)

    dudraw.filled_triangle(x_scale*0.3+x_pos,y_scale*.65+y_pos,x_scale*.35+x_pos, y_scale*0.85+y_pos, x_scale*0.5+x_pos, y_scale*.68+y_pos)
    dudraw.filled_triangle(x_scale*0.7+x_pos,y_scale*.65+y_pos,x_scale*.65+x_pos, y_scale*0.85+y_pos, x_scale*0.5+x_pos, y_scale*.68+y_pos)

    dudraw.set_pen_color(dudraw.BLACK)

    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_circle(x_scale*0.4+x_pos,y_scale*0.6+y_pos,0.05*x_scale)
    dudraw.filled_circle(x_scale*0.6+x_pos,y_scale*0.6+y_pos,0.05*x_scale)

    dudraw.set_pen_color_rgb(7, 136, 145)
    dudraw.filled_circle(x_scale*0.4+x_pos,y_scale*0.6+y_pos,0.035*x_scale)
    dudraw.filled_circle(x_scale*0.6+x_pos,y_scale*0.6+y_pos,0.035*x_scale)

    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_circle(x_scale*0.42+x_pos,y_scale*0.63+y_pos,0.015*x_scale)
    dudraw.filled_circle(x_scale*0.62+x_pos,y_scale*0.63+y_pos,0.015*x_scale)

    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(.01)
    dudraw.elliptical_arc(0.5*x_scale+x_pos,0.5*y_scale+y_pos,0.15*x_scale,0.06*y_scale,230,310)

#defining variables
cg = 5
g = 0
x1 = 0
x2 =0
y1 = 0 
y2 = 1
velocity = 0.025
pokeball_width = .5
pokeball_height = .5
jigglypuff_radius = 0.25

#loop that executes the animation
for i in range(1000):
    while True:
        dudraw.set_pen_width(.5)
        dudraw.set_pen_color_rgb(255,g,g)
        dudraw.line(x1,0,x2,1)  
        dudraw.show(50)
        g += cg
        if g == 255 or g == 0:
            cg *= -1

        x1 += velocity
        x2 += velocity
        #bounces off x = 0 and reveals the pokemon
        if x1 < 0 and x2 < 0:
            velocity *= -1
            jigglypuff(0.33,0.33,jigglypuff_radius,jigglypuff_radius)
        #bounces off x = 1 and brings back the pokeball
        if x1 > 1 and x2 > 1:
            pokeball_width = 0.5
            pokeball(0.25,0.25,pokeball_width,pokeball_height)
            velocity *= -1