from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import utils.draw_utils as draw
import utils.igv_utils as igv_utils
import utils.viewports as vp
import assets.varios as varios
from assets.tower import tower
from assets.central_tower import central_tower, bandera

import assets.extras_escena as extras

widthWindow = 1200
heightWindow = 900


def init_gl():
    glutInit()                                     # Inicializa la librería GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)    # Único frame buffer y modo de color RGB y buffer de prof
    glutInitWindowSize(widthWindow, heightWindow)                   # (width, height)
    glutInitWindowPosition(100, 10)               # (x pos, y pos)
    glutCreateWindow(b'PROYECCION 3D')             # Creación de la ventana (si no se pone b da error)
    glClearColor(1.0, 1.0, 1.0, 1.0);              # Color del buffer

    glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS)

    glEnable(GL_DEPTH_TEST)                        # HABILITA COMPROBACIÓN DE PROFUNDIDAD EN EL DIBUJO           


def draw_ground():
    width_grass = 110
    tile = 2

    palette = [
        draw.green_2,
        draw.green_3,
        draw.green_4,
        draw.green_5,
        draw.grey_1
    ]

    glPushMatrix()

    for x in range(-width_grass, width_grass, tile):
        for z in range(-width_grass, width_grass, tile):

            # Patrón pseudoaleatorio estable, no aleatorio real
            selector = abs((x * 17 + z * 31 + x * z * 7)) % len(palette)
            color_cesped = [palette[selector]]

            glPushMatrix()
            glTranslatef(x, -0.1, z)
            draw.solid_face_xz(tile, tile, color_cesped)
            glPopMatrix()

    glPopMatrix()

    # Borde marrón fino para que parezca una plataforma
    borde_color = [draw.brown_4]

    # Frontal
    glPushMatrix()
    glTranslatef(-width_grass, -2, width_grass - 1)
    draw.solid_ortho(2 * width_grass, 2, 1, borde_color)
    glPopMatrix()

    # Trasero
    glPushMatrix()
    glTranslatef(-width_grass, -2, -width_grass)
    draw.solid_ortho(2 * width_grass, 2, 1, borde_color)
    glPopMatrix()

    # Izquierdo
    glPushMatrix()
    glTranslatef(-width_grass, -2, -width_grass)
    draw.solid_ortho(1, 2, 2 * width_grass, borde_color)
    glPopMatrix()

    # Derecho
    glPushMatrix()
    glTranslatef(width_grass - 1, -2, -width_grass)
    draw.solid_ortho(1, 2, 2 * width_grass, borde_color)
    glPopMatrix()

def draw_scene():

    draw_ground()

    # Dibujar torre central
    glPushMatrix()
    glTranslatef(-40, 0, -40)
    central_tower()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 91, 0)
    bandera()
    glPopMatrix()

    # Extras decorativos
    glPushMatrix()
    extras.extras_escena()
    glPopMatrix()

    # Dibujar torres en las esquinas
    glPushMatrix()
    glTranslatef(-100, 0, -100)
    tower()
    glTranslatef(0, 51, 0)
    bandera()

    glTranslatef(200, -51, 0)
    tower()
    glTranslatef(0, 51, 0)
    bandera()

    glTranslatef(0, -51, 200)
    tower()
    glTranslatef(0, 51, 0)
    bandera()

    glTranslatef(-200, -51, 0)
    tower()
    glTranslatef(0, 51, 0)
    bandera()
    glPopMatrix()



def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    axes_length = 170
    xMin = yMin = zMin = -axes_length
    xMax = yMax = zMax = axes_length
    dNear = -zMax
    dFar = -zMin

    vp.config_viewports(widthWindow, heightWindow, 4, 2)

    vp.set_viewport(1)
    vp.viewport_cabinet(xMin, xMax, yMin, yMax, dNear, dFar)
    draw_scene()

    vp.set_viewport(2)
    vp.viewport_ortho_left(xMin, xMax, yMin, yMax, dNear, dFar)
    draw_scene()

    vp.set_viewport(3)
    vp.viewport_ortho_front(xMin, xMax, yMin, yMax, dNear, dFar)
    draw_scene()

    vp.set_viewport(4)
    vp.viewport_perspective_sym_local( widthWindow, heightWindow )
    draw_scene()

    glutSwapBuffers()

def main():
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()    # Deja la ventana abierta a la espera de eventos
    

main()
