from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

angle_fan = 0.0
speed = 0.2
tx = 2
cloud_offset = 0
cloud_dir = 1

def init():
    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300,300,-300,300)

def draw_pole():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2f(10,-500)
    glVertex2f(-10,-500)
    glVertex2f(-10,0)
    glVertex2f(10,0)
    glEnd()

def draw_clouds(radius, x_offset, y_level):
    glColor3f(0.8,0.8,0.9)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        theta = math.radians(i)
        x = x_offset + radius * math.cos(theta)
        y = y_level + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    
def draw_blades():
    global angle_fan , tx ,cloud_offset
    #draw_clouds()
    glPushMatrix()
    #glTranslatef(tx,0,0)
    draw_clouds(15,cloud_offset+10,150)
    draw_clouds(20,cloud_offset+20,150)
    draw_clouds(25 ,cloud_offset+45,150)
    draw_clouds(25,cloud_offset+50,250)
    draw_clouds(30,cloud_offset+60,250)
    draw_clouds(32 ,cloud_offset+75,250)
    glPopMatrix()
    draw_pole()
    glPushMatrix()
    glRotatef(angle_fan,0,0,1)
    glColor3f(0.3,0.5,0.6)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(0,0)
    for i in range (0,361):
        theta = math.radians(i)
        glVertex2f(15*math.cos(theta),15*math.sin(theta))
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(20,100)
    glVertex2f(-20,100)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(20,-100)
    glVertex2f(-20,-100)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(100,20)
    glVertex2f(100,-20)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(-100,20)
    glVertex2f(-100,-20)
    glEnd()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_blades()
    glutSwapBuffers()

def update(value):
    global angle_fan,speed,tx, cloud_offset , cloud_dir
    if speed < 10:
        speed += 0.01
    elif speed > 10:
        speed -= 0.01
    
    angle_fan += speed
    if angle_fan > 360:
        angle_fan = -360
    tx =- 3
    if tx >= 600:
        tx -= 1.5
    elif tx <= -600:
        tx += 2
    cloud_offset += cloud_dir*0.5
    if cloud_offset < -300 or cloud_offset > 300:
        cloud_dir *= -1
  
    
    glutPostRedisplay()
    glutTimerFunc(16,update,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700,700)
    glutCreateWindow(b"Windmill")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()
main()