import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def plot_circle(xc,yc,x,y):
	glVertex2f(xc+x,yc+y)
	glVertex2f(xc-x,yc+y)
	glVertex2f(xc+x,yc-y)
	glVertex2f(xc-x,yc-y)
	glVertex2f(xc+y,yc+x)
	glVertex2f(xc-y,yc+x)
	glVertex2f(xc+y,yc-x)
	glVertex2f(xc-y,yc-x)
def draw(xc,yc,r):
        x=0
        y=r
        p=1-r
        glBegin(GL_POINTS)
        while x<=y:
                plot_circle(xc,yc,x,y)
                x+=1
                if p<0:
                        p+=2*x+1
                else:
                        y-=1
                        p+=2*(x-y)+1
        glEnd()
def display():
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        draw(0,0,50)
        glFlush()
def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(100,100)
        glutCreateWindow(b"Midpoint Circle Drawing")
        glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(-100,100,-100,100)
        glutDisplayFunc(display)
        glutMainLoop()
main()



