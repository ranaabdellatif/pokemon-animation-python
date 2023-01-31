import dudraw
dudraw.set_canvas_size(500,500)
dudraw.clear(dudraw.LIGHT_GRAY)


#defines function that draws the scaleable pokeball 
def pokeball(x_pos, y_pos, x_scale, y_scale):

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
   

pokeball(0,0,1,1)
dudraw.show(float('inf'))
