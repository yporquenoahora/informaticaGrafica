from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys

import utils.draw_utils as draw
import assets.ornamentos as ornamentos
import assets.extras_escena as extras

widthWindow = 800
heightWindow = 600


def init_gl():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(widthWindow, heightWindow)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Test ornamentos")

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5, 45, -5, 85, -80, 80)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Vista frontal ligeramente separada
    gluLookAt(
        20, 40, 80,   # cámara
        20, 40, 0,    # mira al centro
        0, 1, 0       # eje vertical
    )

    # Pared de referencia, como si fuera la fachada de la torre
    glPushMatrix()
    glTranslatef(0, 0, 40)
    draw.solid_face_xy(41, 81, [draw.grey_3])
    glPopMatrix()

    # Tus ornamentos
    glPushMatrix()
    extras.logo_tecnocasa_torre()
    glPopMatrix()

    glutSwapBuffers()


def main():
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()