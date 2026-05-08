from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils.draw_utils import *
from utils.igv_utils import *

import utils.colors as colors


def vigia_humano():
    glPushMatrix()

    # Colores humano
    color_piel = [253 / 255, 209 / 255, 180 / 255]
    color_armadura = colors.armadura
    color_botas = colors.grey_14
    color_casco = colors.grey_11
    color_lanza = colors.brown_2

    # --- PIERNAS (2 unidades de ancho cada una) ---
    glPushMatrix()
    # Pierna izquierda
    solid_ortho(2, 6, 2, [color_botas])
    # Pierna derecha
    glTranslatef(3, 0, 0)
    solid_ortho(2, 6, 2, [color_botas])
    glPopMatrix()

    # --- CUERPO ---
    glPushMatrix()
    glTranslatef(-1, 6, -1)  # Centramos un poco respecto a las piernas
    solid_ortho(7, 9, 4, [color_armadura])
    glPopMatrix()

    # --- CABEZA Y CASCO ---
    glPushMatrix()
    glTranslatef(1, 15, 0)
    solid_ortho(3, 3, 3, [color_piel])  # Cabeza
    glTranslatef(-1, 2, -1)
    solid_ortho(5, 2, 5, [color_casco])  # Casco
    glPopMatrix()

    # --- BRAZO Y LANZA ---
    glPushMatrix()
    glTranslatef(6, 7, 1)
    solid_ortho(2, 6, 2, [color_armadura])  # Brazo derecho
    # La Lanza (Palo largo)
    glTranslatef(0, -3, 0)
    solid_ortho(1, 22, 1, [color_lanza])
    # Punta de la lanza
    glTranslatef(0, 22, 0)
    solid_ortho(1, 2, 1, [colors.grey_3])
    glPopMatrix()

    glPopMatrix()
