from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0
blades = 4   # default number of blades

def draw_blade():
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(100, 20)
    glVertex2f(100, -20)
    glEnd()

def display():
    global angle, blades
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(250, 250, 0)
    glRotatef(angle, 0, 0, 1)
    glColor3f(0, 0, 0)
    for i in range(blades):
        draw_blade()
        glRotatef(360/blades, 0, 0, 1)

    glutSwapBuffers()

def update(value):
    global angle,speed,target_speed
    if speed<target_speed:
     speed+=0.1
    elif speed>target_speed:
     speed+=0.1 
    angle += speed
    if angle >= 360:
        angle = 0
    glutPostRedisplay()
    glutTimerFunc(30, update, 0)

def init():
    global target_speed
    target_speed =float(input("Enter fan speed(0-50):"))
    glClearColor(0.41, 0.5, 0.32, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)

    glMatrixMode(GL_MODELVIEW)

def main():
    global blades
    global speed
    blades = int(input("Enter number of fan blades: "))
    speed=0

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Fan Animation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

