import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
r=40
x=-250
y=190
xc=2
m=((-250)-190)/(200-(-250))
def init():
    glClearColor(1, 1, 1,0)
    gluOrtho2D(-300, 300, -300, 300)
def circle():
	glColor3f(0,0,0.9)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0,361):
		glVertex2f(x+r*math.cos(math.pi*i/180),y+r*math.sin(math.pi*i/180))
	glEnd()  
def slope():
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(-250,190)
    glVertex2f(200,-250)
    glEnd() 
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    slope()
    
    glFlush()  
def animate(value):
    global x, y, m, xc
    x += xc  # move right each frame
 # reset to start
    if x>=300:
         x=-250
    y = m * (x - (-250)) + 190  # calculate y on line
    glutPostRedisplay()
    glutTimerFunc(40, animate, 0)



      
                
  
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Single buffer
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Rotating Pacman")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(40,animate,0)
    glutMainLoop()

main()