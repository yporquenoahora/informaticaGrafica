from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from utils.draw_utils import *
from utils.igv_utils import *
import utils.colors as colors

def antorcha():
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    # Palo de madera
    color_palo = colors.brown_dark_range
    glPushMatrix()
    empty_pipe_y(3, 10, 3, color_palo)
    glPopMatrix()

    # Soporte superior (más ancho)
    color_soporte = colors.brown_range
    glPushMatrix()
    glTranslatef(-1, 9, -1)
    empty_pipe_y(5, 3, 5, color_soporte)
    glPopMatrix()

    # Llama (naranja/rojo)
    color_llama_base = [colors.firebrick, colors.tomato_red, colors.coral_red]
    glPushMatrix()
    glTranslatef(0, 12, 0)
    empty_pipe_y(3, 4, 3, color_llama_base)
    glPopMatrix()

    # Punta de la llama (más estrecha)
    color_llama_punta = [colors.tomato_red, colors.coral_red]
    glPushMatrix()
    glTranslatef(1, 16, 1)
    empty_pipe_y(3, 3, 3, color_llama_punta)
    glPopMatrix()

    glPopMatrix()