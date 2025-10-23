#yoyo animation
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys,math
angle=0
y=0
dir=.01
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-1,1,-1,1)
def draw_line():
    glBegin(GL_LINES)
    glVertex2f(0,.9)
    glVertex2f(0,y)
    glEnd()
def draw_circle(xc,yc,r):
    glBegin(GL_POLYGON)
    for i in range (0,360,5):
        a=math.radians(i)
        x=xc+r*math.cos(a)
        y=yc+r*math.sin(a)
        glVertex2f(x,y)
    glEnd()
def draw_spokes(xc, yc, r):
    glColor3f(1, 1, 0)  # yellow spokes
    glBegin(GL_LINES)

    # vertical spoke
    glVertex2f(xc,yc-r)
    glVertex2f(xc,yc+r)

    # hori spoke
    glVertex2f(xc-r,yc)
    glVertex2f(xc-r,yc)
   # diagonal top-left to bottom-right
    glVertex2f(xc - r*0.7, yc - r*0.7)
    glVertex2f(xc + r*0.7, yc + r*0.7)
    
    # diagonal top-right to bottom-left
    glVertex2f(xc - r*0.7, yc + r*0.7)
    glVertex2f(xc + r*0.7, yc - r*0.7)
    
    glEnd()
def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(0,0,0)
    draw_line()

    glColor3f(0,0,1)
    glPushMatrix()
    glTranslatef(0,y,0)
    glRotatef(angle,0,0,1)
    draw_circle(0,0,.1)
    draw_spokes(0,0,.1)
    glPopMatrix()
    glutSwapBuffers()
def update(v):
    global angle,y,dir
    angle+=5
    if angle>360:
        angle-=360
    y += dir 
    if y >= .7 or y <= -.7:
        dir *= -1
    glutPostRedisplay()
    glutTimerFunc(16,update,0)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"yoyo animation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()
main()