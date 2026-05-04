from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils.draw_utils import *
from utils.igv_utils import *



def pyramid(size, colors):
    
    # Comprobar size
    if (size < 3):
        print("Error en los parámetros de pyramid")
        return

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    # Si el lado es par se le suma 1 para hacerlo impar y hacer que la cúspide sea un cubo
    if (size % 2) == 0:
        actual_size = size + 1
    else:
        actual_size = size
        
    current_size = actual_size   # current_size es el lado del piso actual
    i = 0
    while (current_size >= 3):  
        color =  [dark_yellow_range[i % len(dark_yellow_range)]]
        empty_face_xz(current_size, current_size, color)
        glTranslatef(1,1,1)
        current_size -= 2
        i = i + 1

    # Cubo correspodiente a la cúspide de la pirámide
    color = colors[randint(0, len(colors)-1)]  # Generar el color
    igv_utils.color_cube(color)

    
    glPopMatrix()

def bench():

    # colores
    leg_colors = [black_5]
    bench_colors = dark_brown_range
    
    # medidas de las patas
    leg_width = 1      # ancho de la pata
    leg_height = 8     # alto de la pata
    
    # medidas del asiento
    seat_length = 40
    seat_width = 10
    seat_height = 2
    
    # medidas del respaldo
    back_width = 2
    back_height = 4
    back_gap = 2
    
    # medidas de las barras
    bar_length = 2
    bar_width = 1    
    
    
    def legs():
        
        glPushMatrix()
        
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata trasera izquierda
        
        glTranslatef(0, 0, seat_width-leg_width)
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata delantera izquierda
        
        glTranslatef(seat_length-leg_width, 0, 0)
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata delantera derecha
        
        glTranslatef(0, 0, -(seat_width-leg_width))
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata trasera derecha
        
        glPopMatrix()
        
    def seat():

        glPushMatrix()
        
        glTranslatef(0, leg_height, 0)
        solid_ortho(seat_length, seat_height, seat_width, bench_colors)
        
        glPopMatrix()
        
    def back():

        glPushMatrix()
        
        glTranslatef(0, leg_height+ seat_height+back_gap, 0) 
        solid_ortho(seat_length, back_height, back_width, bench_colors)
        
        glTranslatef(0, back_height+back_gap, 0)
        solid_ortho(seat_length, back_height, back_width, bench_colors)
        
        glTranslatef(int(seat_length*0.2), -(back_height+2*back_gap+seat_height), -1)
        solid_ortho(bar_length, 2*back_height+2*back_gap+seat_height +1, bar_width, leg_colors)
        
        glTranslatef(int(seat_length*0.6), 0, 0)
        solid_ortho(bar_length, 2*back_height+2*back_gap+seat_height +1, bar_width, leg_colors)  
        
        glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    legs()
    seat()
    back()