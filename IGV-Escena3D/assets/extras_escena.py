from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils.draw_utils import *
from utils.igv_utils import *

# Colores RGB directos
AZUL_OSCURO = (0.10, 0.25, 0.75)
AZUL_MEDIO  = (0.20, 0.45, 0.95)
AZUL_CLARO  = (0.45, 0.75, 1.00)
ROSA_FUERTE = (1.00, 0.25, 0.70)
ROSA_CLARO  = (1.00, 0.60, 0.85)
MORADO      = (0.70, 0.30, 0.85)


def bloque(x, y, z, ancho, alto, fondo, color):
    """
    Dibuja un bloque ortoédrico construido con cubos unitarios.
    Las dimensiones se convierten a enteros para evitar errores con range().
    """
    glPushMatrix()
    glTranslatef(x, y, z)

    ancho = max(1, int(round(ancho)))
    alto = max(1, int(round(alto)))
    fondo = max(1, int(round(fondo)))

    solid_ortho(ancho, alto, fondo, [color])
    glPopMatrix()


def dragoncito_con_corbata():
    """
    Dragón low-poly más grande, azul y con fuego rosa.
    """
    glPushMatrix()

    # Cuerpo
    bloque(0, 0, 0, 12, 8, 6, AZUL_MEDIO)

    # Cabeza
    bloque(9, 5, 0, 7, 5, 6, AZUL_MEDIO)

    # Hocico
    bloque(15, 5, 1, 4, 3, 3, AZUL_CLARO)

    # Ojos
    bloque(15.8, 8, 4.8, 1, 1, 1, black_5)
    bloque(15.8, 8, 0.2, 1, 1, 1, black_5)

    # Cuernos
    bloque(11, 10, 0.2, 1, 2, 1, grey_3)
    bloque(11, 10, 4.8, 1, 2, 1, grey_3)

    # Patas
    bloque(1, -2, 0, 2, 2, 2, AZUL_OSCURO)
    bloque(5, -2, 0, 2, 2, 2, AZUL_OSCURO)
    bloque(1, -2, 4, 2, 2, 2, AZUL_OSCURO)
    bloque(5, -2, 4, 2, 2, 2, AZUL_OSCURO)

    # Cola
    bloque(-5, 2, 2, 5, 2, 2, AZUL_OSCURO)

    # Alas
    bloque(1, 6, -1.5, 5, 5, 1, AZUL_CLARO)
    bloque(1, 6, 6.5, 5, 5, 1, AZUL_CLARO)

    # Corbata
    bloque(10, 1.5, 2.4, 1, 1, 1, MORADO)   # nudo
    bloque(10, 0, 2.4, 1, 2, 1, MORADO)     # cuerpo
    bloque(9.5, -2, 2.4, 2, 2, 1, MORADO)   # punta

    # Fuego rosa saliendo de la boca
    bloque(19, 6, 2.0, 3, 2, 2, ROSA_FUERTE)
    bloque(22, 6.2, 2.1, 4, 2, 2, ROSA_CLARO)
    bloque(26, 6.4, 2.2, 5, 1.6, 1.6, ROSA_FUERTE)

    glPopMatrix()


def extras_escena():
    """
    Solo el dragón.
    """
    glPushMatrix()
    glTranslatef(60, 85, -60)
    glScalef(2.4, 2.4, 2.4)
    dragoncito_con_corbata()
    glPopMatrix()