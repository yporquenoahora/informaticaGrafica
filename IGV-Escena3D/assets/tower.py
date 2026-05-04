from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils.draw_utils import *
from utils.igv_utils import *

import utils.colors as colors


def tower():
    glMatrixMode(GL_MODELVIEW)
        
    # Cuerpo de la torre
    glPushMatrix()
    
    color = colors.grey_balanced_mid_range
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
    color = colors.grey_dark_range
    glTranslatef(-5,53,-5)
    empty_ortho(10, 10, 10, color)

    glTranslatef(0,0,20)
    empty_ortho(10, 10, 10, color)

    glTranslatef(20,0,0)
    empty_ortho(10, 10, 10, color)

    glTranslatef(0,0,-20)
    empty_ortho(10, 10, 10, color)

    glPopMatrix()

    

    
    

    