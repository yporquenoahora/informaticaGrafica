from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils.draw_utils import *
from utils.igv_utils import *


def pieza_fachada(x, y, z, ancho, alto, color):
    glPushMatrix()
    glTranslatef(x, y, z)
    solid_ortho(ancho, alto, 1, color)
    glPopMatrix()


def puerta_principal():
    pieza_fachada(12, 0, 40.8, 16, 26, [grey_5])
    pieza_fachada(15, 2, 41.5, 10, 22, [brown_5])
    pieza_fachada(20, 2, 42.2, 1, 22, [black_5])
    pieza_fachada(18, 12, 42.8, 1, 1, [grey_1])
    pieza_fachada(22, 12, 42.8, 1, 1, [grey_1])


def ventana_frontal(x, y):
    pieza_fachada(x, y, 40.9, 11, 11, [grey_5])
    pieza_fachada(x + 2, y + 2, 41.6, 7, 7, [black_5])
    pieza_fachada(x + 5, y + 2, 42.2, 1, 7, [grey_2])
    pieza_fachada(x + 2, y + 5, 42.2, 7, 1, [grey_2])


def antorcha_frontal(x, y):
    pieza_fachada(x, y, 42.5, 1, 8, [brown_5])
    pieza_fachada(x - 1, y + 8, 43.0, 3, 5, [red_4])
    pieza_fachada(x, y + 9, 43.5, 1, 3, [yellow_4])


def texto_stroke_negrita(texto):
    """
    Texto vectorial más visible que el bitmap.
    Se dibuja varias veces con pequeños desplazamientos para simular negrita.
    """
    for dx, dy in [(0, 0), (1.2, 0), (0, 1.2)]:
        glPushMatrix()
        glTranslatef(dx, dy, 0)
        for c in texto:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(c))
        glPopMatrix()


def logo_tecnocasa_torre():
    """
    Logo TECNOCASA en lo alto de la torre:
    fondo blanco, texto verde, un poco más ancho que la torre.
    """
    glPushMatrix()

    # Placa blanca: un poco más ancha que la torre central (40)
    glTranslatef(-5, 67, 42.8)
    solid_ortho(50, 9, 1, [grey_1])

    # Texto verde encima de la placa
    glTranslatef(5, 1.8, 1.4)
    glColor3f(0.0, 0.45, 0.18)
    glLineWidth(2.5)
    glScalef(0.018, 0.018, 0.018)

    texto_stroke_negrita("TECNOCASA")

    glColor3f(1.0, 1.0, 1.0)
    glPopMatrix()


def ornamentacion_torre_central():
    glPushMatrix()

    puerta_principal()

    ventana_frontal(5, 35)
    ventana_frontal(25, 35)
    ventana_frontal(5, 55)
    ventana_frontal(25, 55)

    antorcha_frontal(8, 10)
    antorcha_frontal(31, 10)

    logo_tecnocasa_torre()

    glPopMatrix()