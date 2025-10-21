from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angle = 0.0
speed = 3
tx = -20
#dirt = 1
move =2

def init():
	glClearColor(0,0,0,1)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-300, 300, -300, 300)
	glMatrixMode(GL_MODELVIEW)
	

def draw_triangle():
	glBegin(GL_TRIANGLES)
	glVertex2f(0,0)
	glVertex2f(45,90)
	glVertex2f(0,30)
	glEnd()

def display():
	global tx,angle
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	glPushMatrix()
	glTranslatef(tx,0,0)
	
	#glTranslatef(0,0,0)
	glRotatef(angle,0,0,1)
	#glTranslatef(0,0,0)
	
	draw_triangle()
	glPopMatrix()
	glFlush()


def update(value):
	global angle,tx
	
	angle += speed
	if angle >= 360:
		angle =0
	tx += move
	if tx> 200 :
		tx = -100
	
	glutPostRedisplay()
	glutTimerFunc(30,update,0)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(100,100)
	glutCreateWindow(b"tri")
	init()
	glutDisplayFunc(display)
	glutTimerFunc(30,update,0)
	glutMainLoop()
main()


















