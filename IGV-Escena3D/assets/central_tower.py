

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from utils.draw_utils import *
from utils.igv_utils import *

from . import ornamentos


light_grey_range2 = [grey_2, grey_3]

def central_tower():
    # Castillo Central
    # --- Base del Castillo ---
    glPushMatrix()
    # Dibujamos el suelo/base
    solid_face_xz(80, 80, [grey_1])
    glTranslate(5,1,5)
    solid_face_xz(70, 70, [grey_2])
    glTranslate(5,1,5)
    solid_face_xz(60, 60, [grey_3])
    glTranslate(5,1,5)
    solid_face_xz(50, 50, [grey_4])
    glTranslate(5,1,5)
    solid_face_xz(40, 40, [grey_5])
    # --- Estructura de la Torre ---
    # Nos movemos para centrar la torre de 40x40 sobre la base de 80x80
    glTranslatef(0,1,0)
    empty_ortho(40, 80, 40, light_grey_range2)

    # Ornamentación añadida: puertas, ventanas y antorchas
    glPushMatrix()
    ornamentos.ornamentacion_torre_central()
    glPopMatrix()


    glPopMatrix()
    glPushMatrix()
    #Cara derecha de torre a X=60
    glTranslatef(60.1, 55,35)
    solid_face_yz(12, 8, [black_5])
    glPopMatrix()
    #Techo
    glPushMatrix()
    glTranslatef(20,85.1,20)
    solid_face_xz(40, 40, [grey_2])
    glPopMatrix() # Cierra el techo
    #Torretas
    #primera
    glPushMatrix()
    glTranslatef(15,86,15)
    empty_ortho(15, 10, 15, dark_grey_range)
    glTranslatef(0,10,0)
    pyramid2(15, [red_4])    
    glPopMatrix() # Fin primera
    #segunda
    glPushMatrix()
    glTranslatef(50,86,15)
    empty_ortho(15, 10, 15, dark_grey_range)
    glTranslatef(0,10,0)
    pyramid2(15, [red_4])    
    glPopMatrix() # Fin segunda
    #tercera
    glPushMatrix()
    glTranslatef(15,86,50)
    empty_ortho(15, 10, 15, dark_grey_range)
    glTranslatef(0,10,0)
    pyramid2(15, [red_4])    
    glPopMatrix() # Fin tercera
    #cuarta
    glPushMatrix()
    glTranslatef(50,86,50)
    empty_ortho(15, 10, 15, dark_grey_range)
    glTranslatef(0,10,0)
    pyramid2(15, [red_4])    
    glPopMatrix() # Fin cuarta
    
def bandera():
    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()

    solid_face_xz(9, 9, [grey_4])

    glTranslatef(3, 1, 3)
    empty_pipe_y(3, 30, 3, [grey_4])

    glTranslatef(0, 20, 0)

    glRotatef(90, 0, 0, 1)
    pyramid2(6, [blue_3])

    glPopMatrix()
    

def pyramid2(size, colors, height_step=2):
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    current_size = size
    h = 0

    while current_size >= 1:
        glPushMatrix()

        offset = (size - current_size) / 2.0
        glTranslatef(offset, h, offset)

        for i in range(current_size):
            for j in range(current_size):
                glPushMatrix()
                glTranslatef(i, 0, j)
                color = colors[randint(0, len(colors)-1)]
                color_cube(color)
                glPopMatrix()

        glPopMatrix()

        h += 1

        if h % height_step == 0:
            current_size -= 1

    glPopMatrix()
    
    