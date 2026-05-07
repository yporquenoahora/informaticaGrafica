from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils.draw_utils import *
from utils.igv_utils import *

import utils.colors as colors

def flag_shield():
    def shield_part():
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        
        color_symbol = [yellow_4]
        solid_ortho(4, 1, 1, color_symbol)
        glTranslatef(2,1,0)
        solid_ortho(1, 1, 1, color_symbol) 
        glTranslatef(0,-2,0)
        solid_ortho(1, 1, 1, color_symbol) 
        glTranslatef(-1,1,0)
        solid_ortho(1, 1, 1, color_symbol)    

        glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    
    #cruz derecha
    glPushMatrix()
    glTranslatef(1, 0, 0)
    shield_part()
    glPopMatrix()

    #Cruz superior
    glPushMatrix()
    glTranslatef(0, 1, 0)
    glRotatef(90, 0, 0, 1)
    shield_part()
    glPopMatrix()
    
    #Cruz izquierda
    glPushMatrix()
    glTranslatef(-1, 0, 0)
    glRotatef(180, 0, 0, 1)
    shield_part()
    glPopMatrix()
    
    #Cruz inferior
    glPushMatrix()
    glTranslatef(0, -1, 0)
    glRotatef(270, 0, 0, 1)
    shield_part()
    glPopMatrix()


def blue_flag():
    glMatrixMode(GL_MODELVIEW)
    
    # Mástil
    color_pole = [colors.grey_14]
    
    glPushMatrix()
    solid_ortho(1, 30, 1, color_pole)
    glPopMatrix()

    # Tela de la bandera
    color_flag = [blue_4]
    glPushMatrix()
    glTranslatef(0, 19, 0)
    solid_face_xy(18, 10, color_flag)
    glPopMatrix()

    glPushMatrix()

    glTranslatef(9, 24, 1) 
    flag_shield()

    glPopMatrix()

def tower():
    glMatrixMode(GL_MODELVIEW)
        
    # Cuerpo de la torre
    glPushMatrix()
    
    color = colors.tower_base
    empty_pipe_y(20, 50, 20, color)
    
    # Parte superior de la torre
    color = colors.grey_balanced_mid_range
    glTranslatef(-5,50,-5)
    solid_face_xz(30, 30, color)

    color = colors.grey_dark_range
    
    for i in range(5):
        glTranslatef(0,1,0)
        empty_face_xz(30, 30, color)
    glPopMatrix()

    #Almenas
    glPushMatrix()
    color = colors.grey_deep_dark_range
    glTranslatef(-5,53,-5)
    empty_ortho(10, 10, 10, color)

    glTranslatef(0,0,20)
    empty_ortho(10, 10, 10, color)

    glTranslatef(20,0,0)
    empty_ortho(10, 10, 10, color)

    glTranslatef(0,0,-20)
    empty_ortho(10, 10, 10, color)

    glPopMatrix()

    #Mastil con bandera
    glPushMatrix()
    glTranslatef(10,53,10)  # Posicionar el mástil en el centro de la torre
    blue_flag()
    glPopMatrix()
    
    

    
    

    