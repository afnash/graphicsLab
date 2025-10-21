import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
X = -200
Y = 0
def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-300,300,-300,300)

def plot():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(40/255,0/255,200/255)
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	for i in range (0,360,1):
		glVertex2f(50*math.cos(math.pi*i/180),50*math.sin(math.pi*i/180))
	glEnd()
	glFlush()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("CIRCLE")
	glutDisplayFunc(lambda:plot())
	init()
	glutMainLoop()
main()	

	
