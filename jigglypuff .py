import dudraw

dudraw.set_canvas_size(500,500)
dudraw.clear(dudraw.WHITE)


def jigglypuff(x_pos,y_pos,x_scale,y_scale):
    dudraw.set_pen_color_rgb(245, 157, 189)
    dudraw.filled_circle(x_scale*0.5+x_pos,y_scale*0.5+y_pos,0.25*x_scale)

    dudraw.filled_triangle(0.3,.65,.35, 0.85, 0.5, .68)
    dudraw.filled_triangle(0.7,.65,.65, 0.85, 0.5, .68)

    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.filled_triangle(0.32,.65,.35,.83,0.5,.68)

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

jigglypuff(0,0,1,1)
dudraw.show(float('inf'))