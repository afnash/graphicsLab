from openGL.GL import *
from openGL.GLU import *
from openGL.GLUT import *
import math

x1,y1 = 0, 300
r = 40
ty = 0.0
g = -0.5
loss = 0.9
min_vel = 0.25
is_rest = False
floor_y = 50

def init():
	glutClearColor(0,0,0,1)
	gluOrtho2D(-600,600,-600,600)

def draw():
	global x1,y1
	glClear(GL_BUFFER_BIT)
	glColor3f(0.8,0.4,0.5)
	glBegin(GL_LINES)
	glVertex2f(-250,floor_y)
	glVertex2f(250,floor_y)
	glEnd()
	
	glColor3f(0,0,1)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x1,y1)
	for i in range (0,361):
		angle = math.radians(i)
		glVertex( x1 + r*math.cosine(angle), y1 + r*math.sin(angle))
	glEnd()
	glFlush()
	
def translate(value):
	global y1,ty,g,is_rest
	if not is_rest:
		ty += g
		y1 += ty
		
		if y1 -r < floor_y:
			y1 = floor_y + r
			ty = -ty*loss
			
			if abs(ty) < min_vel:
				ty = 0
				is_rest = True
	glutPostRedisplay()
	glutTimerFunc(30,translate,0)
	
def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(800,800)
	glutInitWindowPosition(600,0)
	init()
	glutDisplayFunc(draw)
	glutTimerFunc(30, translate, 0)
	glutMainLoop()

main()
				
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
