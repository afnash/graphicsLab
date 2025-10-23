from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, math

angle = 0.0
petal_count = 0
total_petals = 5

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)
    glMatrixMode(GL_MODELVIEW)

def draw_circle_outline(radius):
    glBegin(GL_LINE_LOOP)  # draw outline instead of filled circle
    for i in range(0, 360, 5):
        a = math.radians(i)
        x = radius * math.cos(a)
        y = radius * math.sin(a)
        glVertex2f(x, y)
    glEnd()

def draw_flower():
    petal_radius = 20
    step_angle = 360 / total_petals
    petal_distance = 30  # reduce distance so petals overlap

    for i in range(petal_count):
        glPushMatrix()
        glRotatef(i * step_angle, 0, 0, 1)
        glColor3f(1, 0, 0)  # red outline petals
        glTranslatef(0, petal_distance, 0)
        draw_circle_outline(petal_radius)
        glPopMatrix()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glPushMatrix()
    glRotatef(angle, 0, 0, 1)    # rotate whole flower
    draw_flower()
    glPopMatrix()

    glutSwapBuffers()

def update(value):
    global angle, petal_count
    angle += 1
    if angle > 360:
        angle -= 360

    # Bloom effect: add petals one by one
    if petal_count < total_petals:
        petal_count += 1

    glutPostRedisplay()
    glutTimerFunc(500, update, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotating Flower with Outline Circular Petals")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()