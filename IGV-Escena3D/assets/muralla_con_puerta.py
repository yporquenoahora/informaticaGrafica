from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from utils.draw_utils import *
from utils.igv_utils import *
import utils.colors as colors

def muralla_con_puerta():
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    color = colors.grey_balanced_mid_range
    color_borde = colors.grey_almost_black_range
    color_arco = colors.grey_almost_black_range
    color_madera = colors.brown_dark_range

    ancho_puerta = 20
    alto_puerta = 20
    mitad = 80

    # Mitad izquierda
    glPushMatrix()
    empty_pipe_y(mitad, 30, 5, color)
    glPopMatrix()

    # Mitad derecha
    glPushMatrix()
    glTranslatef(mitad + ancho_puerta, 0, 0)
    empty_pipe_y(mitad, 30, 5, color)
    glPopMatrix()

    # Dintel encima de la puerta
    glPushMatrix()
    glTranslatef(mitad, alto_puerta, 0)
    empty_pipe_y(ancho_puerta, 30 - alto_puerta, 5, color)
    glPopMatrix()

    # Marco izquierdo
    glPushMatrix()
    glTranslatef(mitad - 3, 0, 0)
    empty_pipe_y(3, alto_puerta + 2, 5, color_borde)
    glPopMatrix()

    # Marco derecho
    glPushMatrix()
    glTranslatef(mitad + ancho_puerta, 0, 0)
    empty_pipe_y(3, alto_puerta + 2, 5, color_borde)
    glPopMatrix()

    # Dintel oscuro
    glPushMatrix()
    glTranslatef(mitad, alto_puerta, 0)
    empty_pipe_y(ancho_puerta, 3, 5, color_borde)
    glPopMatrix()

    # Arco de piedra
    glPushMatrix()
    glTranslatef(mitad, alto_puerta, 0)
    empty_pipe_y(ancho_puerta, 3, 6, color_arco)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(mitad + 3, alto_puerta + 3, 0)
    empty_pipe_y(ancho_puerta - 6, 3, 6, color_arco)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(mitad + 6, alto_puerta + 6, 0)
    empty_pipe_y(ancho_puerta - 12, 3, 6, color_arco)
    glPopMatrix()

    # Hoja izquierda de la puerta
    glPushMatrix()
    glTranslatef(mitad, 0, 1)
    empty_pipe_y(ancho_puerta // 2, alto_puerta, 3, color_madera)
    glPopMatrix()

    # Hoja derecha de la puerta
    glPushMatrix()
    glTranslatef(mitad + ancho_puerta // 2, 0, 1)
    empty_pipe_y(ancho_puerta // 2, alto_puerta, 3, color_madera)
    glPopMatrix()

    # Almenas lado izquierdo
    for i in range(5, mitad, 15):
        glPushMatrix()
        glTranslatef(i, 30, 0)
        empty_pipe_y(7, 5, 6, color_borde)
        glPopMatrix()

    # Almenas lado derecho
    for i in range(mitad + ancho_puerta + 5, 180, 15):
        glPushMatrix()
        glTranslatef(i, 30, 0)
        empty_pipe_y(7, 5, 6, color_borde)
        glPopMatrix()

    glPopMatrix()  # cierre principal