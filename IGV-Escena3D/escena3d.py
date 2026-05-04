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

def draw_scene():
    
    width_grass = 110
    tile = 5
    altura_terreno = tile 
    
    # Dibujar terreno pixelado con varios tonos
    glPushMatrix()

    for x in range(-width_grass, width_grass, tile):
        for z in range(-width_grass, width_grass, tile):

            selector = ((x // tile) * 3 + (z // tile) * 5) % 5

            if selector == 0:
                color_cesped = [draw.green_3]
            elif selector == 1:
                color_cesped = [draw.green_4]
            elif selector == 2:
                color_cesped = [draw.green_5]
            elif selector == 3:
                color_cesped = [draw.grey_1]
            else:
                color_cesped = [draw.green_2]

            if ((x // tile) + (z // tile)) % 2 == 0:
                color_tierra = [draw.brown_5]
            else:
                color_tierra = [draw.brown_4]

            # Bloque de tierra: baja desde y=-tile hasta y=0
            glPushMatrix()
            glTranslatef(x, -altura_terreno, z)
            draw.solid_ortho(tile, altura_terreno, tile, color_tierra)
            glPopMatrix()

            # Capa de césped encima
            glPushMatrix()
            glTranslatef(x, 0, z)
            draw.solid_ortho(tile, 1, tile, color_cesped)
            glPopMatrix()

    glPopMatrix()

    # Dibujar torre central
    
    glPushMatrix()
    glTranslate(-40,0,-40)
    #glScalef(1.5,1.5,1.5)
    central_tower()
    glPopMatrix()
    glPushMatrix()
    glTranslate(0,91,0)
    glScalef(1.5,1.5,1.5)
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
    glTranslatef(0,51,0)
    bandera()
    glTranslatef(200, -51, 0)
    tower()
    glTranslatef(0,51,0)
    bandera()
    glTranslatef(0, -51, 200)
    tower()
    glTranslatef(0,51,0)
    bandera()
    glTranslatef(-200, -51, 0)
    tower()
    glTranslatef(0,51,0)
    bandera()
    glPopMatrix()



def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    axes_length = 150
    xMin = yMin = zMin = -axes_length
    xMax = yMax = zMax = axes_length
    dNear = -zMax
    dFar = -zMin

    vp.config_viewports(widthWindow, heightWindow, 4, 2)

    vp.set_viewport(1)
    vp.viewport_cabinet(xMin, xMax, yMin, yMax, dNear, dFar)
    draw_scene()

    vp.set_viewport(2)
    vp.viewport_ortho_top(xMin, xMax, yMin, yMax, dNear, dFar)
    draw_scene()

    vp.set_viewport(3)
    vp.viewport_ortho_front(xMin, xMax, yMin, yMax, dNear, dFar)
    draw_scene()

    glutSwapBuffers()

def main():
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()    # Deja la ventana abierta a la espera de eventos
    

main()
