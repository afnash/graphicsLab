from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time, math

def draw_circle(xc, yc, r):
    glBegin(GL_POINTS)
    for theta in range(0, 360):
        x = int(r*math.cos(math.radians(theta)))
        y = int(r*math.sin(math.radians(theta)))
        glVertex2i(xc+x, yc+y)
    glEnd()

def draw_hand(length, angle):
    glBegin(GL_LINES)
    glVertex2i(250, 250)
    glVertex2i(250 + int(length*math.cos(math.radians(angle))),
               250 + int(length*math.sin(math.radians(angle))))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    draw_circle(250, 250, 120)

    t = time.localtime()
    sec_angle = 90 - (t.tm_sec * 6)
    min_angle = 90 - (t.tm_min * 6)
    hr_angle = 90 - ((t.tm_hour % 12) * 30 + t.tm_min * 0.5)

    glColor3f(0.8, 0.5, 0.3)
    draw_hand(100, sec_angle)
    glColor3f(0.3, 1, 0.7)
    draw_hand(80, min_angle)
    glColor3f(0.6, 0.7, 1)
    draw_hand(50, hr_angle)

    glFlush()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(1000, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Clock Animation")
    gluOrtho2D(0, 500, 0, 500)
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

