from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


# jilebi shape = a+b(theta)


"""
1.aadyam trace cheyyane points set akka,
2.ooro pointilum circle varakka
3.points listilekk store akka, update akka
"""
points = []
a = 0
b = 0.5 #coefficient of jilebi shape.
speed, angle_rotate = 0.3,0
radius = 0

def init():
    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300,300,-300,300)
    
def circle(r):
    glColor3f(0.2,0.4,1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (1,361):
        theta = math.radians(i)
        glVertex2f(r*math.cos(theta),r*math.sin(theta))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.9,0.8,0.7)
    glBegin(GL_LINE_STRIP)
    for px,py in points:
        glVertex2f(px,py)
    glEnd()
    if points:
        px,py = points[-1]
        glPushMatrix()
        glTranslatef(px, py, 0)
        glRotatef(angle_rotate * 5, 0, 0, 1)  # spin around its own axis
        glColor3f(0.9, 0.7, 0.6)
        circle(20)

        glColor3f(1,1,1)
        glBegin(GL_LINES)
        glVertex2f(0,0)
        glVertex2f(10,0)
        glVertex2f(0,0)
        glVertex2f(-10,0)
        glEnd()
        glPopMatrix()
    glutSwapBuffers()

def update(value):
    global angle_rotate,radius,points
    
    
    angle_rotate += speed*5
    if angle_rotate > 360:
        angle_rotate = -360
   

    radius += b
    if radius>300:
        radius = 10
        points.clear()

    x=radius*math.cos(math.radians(angle_rotate))
    y=radius*math.sin(math.radians(angle_rotate))
    points.append((x,y))
       
    
    glutPostRedisplay()
    glutTimerFunc(16,update,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700,700)
    glutCreateWindow(b"jilebi")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()
        


