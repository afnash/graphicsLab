from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


angle_orbit = 0.0
angle_spin = 0.0
speed = 0.2

def init():
    glClearColor(0,0,0,1) #backgroundColor
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300,300,-300,300)
    glMatrixMode(GL_MODELVIEW)

def circle(radius):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361):
        theta = math.radians(i)
        glVertex2f(radius*math.cos(theta),radius*math.sin(theta))
    glEnd()

def draw_orbits(radius):
    glColor3f(1,1,1)
    glBegin(GL_LINE_LOOP)
    for i in range(0,361):
        theta = math.radians(i)
        glVertex(radius*math.cos(theta),radius*math.sin(theta))
    glEnd()

def draw_sun():
    glColor3f(0.7,0.9,0.6)
    circle(50)

def draw_planets():
    global angle_orbit,angle_spin
    draw_orbits(100)
    draw_orbits(150)
    glPushMatrix()
    glRotatef(angle_orbit,0,0,1) #revolve
    glTranslatef(100,0,0)
    glRotatef(angle_spin,0,0,1) #rotate
    glColor3f(0.2,0.5,1.0)
    circle(20)
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(20,0)
    glVertex2f(0,0)
    glVertex2f(0,20)
    glVertex2f(0,0)
    glVertex2f(-20,0)
    glVertex2f(0,0)
    glVertex2f(0,-20)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(angle_orbit*0.7,0,0,1) #revolve
    glTranslatef(150,0,0)
    glRotatef(angle_spin*1.5,0,0,1) #rotate
    glColor3f(0.4,0.7,0.0)
    circle(10)
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(10,0)
    glVertex2f(0,0)
    glVertex2f(0,10)
    glVertex2f(0,0)
    glVertex2f(-10,0)
    glVertex2f(0,0)
    glVertex2f(0,-10)
    glEnd()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_sun()
    draw_planets()
    glutSwapBuffers()

def update(value):
    global angle_orbit,angle_spin
    angle_orbit += speed
    if angle_orbit > 360 :
        angle_orbit = -360
    angle_spin += speed*5
    if angle_spin > 360 :
        angle_spin = -360
    glutPostRedisplay()
    glutTimerFunc(16,update,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutCreateWindow(b"solar system")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()





    