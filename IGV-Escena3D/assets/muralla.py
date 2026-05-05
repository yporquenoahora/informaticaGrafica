from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from utils.draw_utils import *
from utils.igv_utils import *
import utils.colors as colors

def muralla():
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    # Cuerpo principal de la muralla
    color = colors.grey_balanced_mid_range
    empty_pipe_y(180, 30, 5, color)
    
    # Borde izquierdo (más oscuro)
    glPushMatrix()
    glTranslatef(0, 0, 0)
    color_borde = colors.grey_balanced_dark_range
    empty_pipe_y(5, 32, 5, color_borde)
    glPopMatrix()
    
    # Borde derecho (más oscuro)
    glPushMatrix()
    glTranslatef(175, 0, 0)
    empty_pipe_y(5, 32, 5, color_borde)
    glPopMatrix()
    
    # Franja superior (más oscura)
    glPushMatrix()
    glTranslatef(0, 28, 0)
    color_top = colors.grey_strong_dark_range
    solid_ortho(180, 2, 5, color_top)
    glPopMatrix()
    
    # Almenas encima
    glPushMatrix()
    color_almenas = colors.grey_dark_range
    glTranslatef(5, 30, 0)
    for i in range(0, 170, 15):
        glPushMatrix()
        glTranslatef(i, 0, 0)
        solid_ortho(7, 5, 5, color_almenas)
        glPopMatrix()
    glPopMatrix()

    glPopMatrix()