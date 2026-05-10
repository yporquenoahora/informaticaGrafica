from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import utils.draw_utils as draw
import utils.igv_utils as igv_utils
import utils.viewports as vp
from assets.vigia import vigia_humano
from assets.tower import tower
from assets.central_tower import central_tower, bandera
from assets.muralla import muralla
from assets.muralla_con_puerta import muralla_con_puerta

import assets.extras_escena as extras
import utils.colors as colors

from assets.antorcha import antorcha

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
    width_grass = 130
    tile = 2

    palette = [
        draw.green_2,
        draw.green_3,
        draw.green_4,
        draw.green_5,
        draw.grey_1
    ]

    glPushMatrix()

    offset = -5
    glTranslatef(offset, 0, 0)
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
    glTranslatef(-width_grass + offset, -2, width_grass - 1)
    draw.solid_ortho(2 * width_grass, 2, 1, borde_color)
    glPopMatrix()

    # Trasero
    glPushMatrix()
    glTranslatef(-width_grass + offset, -2, -width_grass)
    draw.solid_ortho(2 * width_grass, 2, 1, borde_color)
    glPopMatrix()

    # Izquierdo
    glPushMatrix()
    glTranslatef(-width_grass + offset, -2, -width_grass)
    draw.solid_ortho(1, 2, 2 * width_grass, borde_color)
    glPopMatrix()

    # Derecho
    glPushMatrix()
    glTranslatef(width_grass - 1 + offset, -2, -width_grass)
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
    glTranslatef(0, 86, 0)
    bandera()
    glPopMatrix()

    # Extras decorativos
    glPushMatrix()
    extras.extras_escena()
    glPopMatrix()

    # Dibujar torres en las esquinas
    # Torre esquina Frontal-Derecha
    glPushMatrix()
    glTranslatef(90, 0, 90)
    tower()
    glTranslated(10,52,12)
    vigia_humano()
    glPopMatrix()
    
    # Torre esquina Trasera-Derecha
    glPushMatrix()
    glTranslatef(90, 0, -115)  
    tower()
    glPopMatrix()
        
    # Torre esquina Frontal-Izquierda
    glPushMatrix()
    glTranslatef(-120, 0, 90)
    tower()
    glTranslated(2,52,12)
    vigia_humano()
    glPopMatrix()

    # Torre esquina Trasera-Izquierda
    glPushMatrix()
    glTranslatef(-120, 0, -115)
    tower()
    glPopMatrix()
    
    # Soldado Muralla 1
    glPushMatrix()
    glTranslatef(30, 25, 87)
    vigia_humano()
    glPopMatrix()

    # Soldado Muralla 2
    glPushMatrix()
    glTranslatef(-33, 25, 87)
    vigia_humano()
    glPopMatrix()

    # Muralla - 4 tramos independientes
    # Muralla trasera CON PUERTA
    glPushMatrix()
    glTranslatef(-100, 0, -110)
    muralla_con_puerta()
    glPopMatrix()

    # Tramo frontal
    glPushMatrix()
    glTranslatef(-100, 0, 90)
    muralla_con_puerta()
    glPopMatrix()

    # Tramo izquierdo
    glPushMatrix()
    glTranslatef(-110, 0, -90)
    glRotatef(-90, 0, 1, 0)
    muralla()
    glPopMatrix()

    # Tramo derecho
    glPushMatrix()
    glTranslatef(100, 0, -100)
    glRotatef(-90, 0, 1, 0)
    muralla()
    glPopMatrix()

    # Foso delante de la muralla frontal
    glPushMatrix()
    glTranslatef(-100, -1, 105)
    draw.solid_ortho(190, 2, 50, colors.water_range)
    glPopMatrix()

    # Puente/pasarela sobre el foso (centrado en la puerta trasera)
    glPushMatrix()
    glTranslatef(-10, 2, 105)
    draw.solid_ortho(20, 3, 50, colors.stone_range)
    glPopMatrix()

    # Antorchas en el puente - lado izquierdo
    glPushMatrix()
    glTranslatef(-15, 2, 107)
    antorcha()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-15, 2, 148)
    antorcha()
    glPopMatrix()

    # Antorchas en el puente - lado derecho
    glPushMatrix()
    glTranslatef(12, 2, 107)
    antorcha()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(12, 2, 148)
    antorcha()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    axes_length = 190
    xMin = yMin = zMin = -axes_length
    xMax = yMax = zMax = axes_length
    dNear = -zMax
    dFar = -zMin
    
    # Compilamos la escena una vez para mejorar el rendimiento al dibujarla en cada viewport
    scene_compile = glGenLists(1)
    glNewList(scene_compile, GL_COMPILE)
    draw_scene()
    glEndList()

    # Configuramos los 4 viewports
    vp.config_viewports(widthWindow, heightWindow, 4, 2)

    vp.set_viewport(1)
    vp.viewport_cabinet(xMin, xMax, yMin, yMax, dNear, dFar)
    glCallList(scene_compile)

    vp.set_viewport(2)
    vp.viewport_ortho_left(xMin, xMax, yMin, yMax, dNear, dFar)
    glCallList(scene_compile)

    vp.set_viewport(3)
    vp.viewport_ortho_front(xMin, xMax, yMin, yMax, dNear, dFar)
    glCallList(scene_compile)

    vp.set_viewport(4)
    vp.viewport_perspective_sym_local( widthWindow, heightWindow )
    glCallList(scene_compile)

    glutSwapBuffers()

def main():
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()    # Deja la ventana abierta a la espera de eventos
    

main()
