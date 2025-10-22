from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# --- Ball motion params ---
x = -200           # start at left edge
y = 0
vx = 2.5           # horizontal speed along slope
loss = 0.98        # speed loss factor per frame

# --- Pit geometry ---
pit_left = -250
pit_right = 250
pit_bottom = -150

def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300, 300, -300, 300)

def draw_pit():
    glColor3f(0.3, 0.5, 0.7)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-250, 0)
    glVertex2f(-50, pit_bottom)
    glVertex2f(-50,pit_bottom)
    glVertex2f(50,pit_bottom)
    glVertex2f(50, pit_bottom)
    glVertex2f(250, 0)
    glEnd()

def draw_ball():
    glColor3f(0.9, 0.3, 0.1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        theta = math.radians(i)
        glVertex2f(15 * math.cos(theta), 15 * math.sin(theta))
    glEnd()

'''def pit_surface_y(x):
    if x < 0:
        return (pit_bottom / 250) * (x + 250)
    else:
        return (pit_bottom / -250) * (x - 250)'''

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_pit()
    
    # Draw ball
    glPushMatrix()
    glTranslatef(x,y+15, 0)
    draw_ball()
    glPopMatrix()

    glutSwapBuffers()

def update(value):
    global x,y, vx,vy

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Simple Pit Ball")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()
