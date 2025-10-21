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

def draw(cordinate_list):
	global X,Y
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(255/255,255/255,255/255)
	glLineWidth(20)
	glBegin(GL_POLYGON)
	for i in cordinate_list:
		glVertex2f(i[0],i[1])
	glEnd()
	glutSwapBuffers()
	
def main():
	sides=int(input("enter the no. of sides: "))
	sides_list = []
	for i in range (1,sides+1):
		x=float(input(f"enter the X coordinate of vertex {i} :"))
		y=float(input(f"enter the Y coordinate of vertex {i} :"))
		sides_list.append([x,y])
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("POLY")
	glutDisplayFunc(lambda:draw(sides_list))
	init()
	glutMainLoop()
main()	

	
