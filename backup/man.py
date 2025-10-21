from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
 glClearColor(0.67,0.76,0.85,1)
 glOrtho(-10,10,-10,10,-1,1)
def Circle():
 glClear(GL_COLOR_BUFFER_BIT)
 glColor3f(1,0.66,0.24)
 radius = 1.5
 segments = 100
 cx=-3
 cy=-4.7
 sides = 3
 rp = 5
 angle_step = 2*math.pi/sides
 
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  angle=2*math.pi*i/segments
  x=cx+radius*math.cos(angle)
  y=cy+radius*math.sin(angle)
  glVertex2f(x,y)
 glEnd()
 glColor3f(0,0.5,0)
 glTranslatef(-6,-8,0)
 glRotatef(90,0,0,1)
 scale=1.4 
 glBegin(GL_POLYGON)
 for i in range(sides):
  angle=i*angle_step
  x=rp*math.cos(angle)
  y=rp*math.sin(angle)
  glVertex2f(x*scale,y*scale)
 glEnd()
 
 glColor3f(0,0.2,0.6)
 glRotatef(90,0,0,1) 
 glTranslatef(-11,8,0)
 glBegin(GL_QUADS)
 glVertex2f(-8,-8)
 glVertex2f(-8,-6)
 glVertex2f(8,-8)
 glVertex2f(8,-6)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r1 = 1
 cx1=9
 cy1=-23
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a1=2*math.pi*i/segments
  x1=cx1+r1*math.cos(a1)
  y1=cy1+r1*math.sin(a1)
  glVertex2f(x1,y1)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r2 = 1
 cx2=7.5
 cy2=-22.5
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a2=2*math.pi*i/segments
  x2=cx2+r2*math.cos(a2)
  y2=cy2+r2*math.sin(a2)
  glVertex2f(x2,y2)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r3 = 1
 cx3=8
 cy3=-21.5
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a3=2*math.pi*i/segments
  x3=cx3+r3*math.cos(a3)
  y3=cy3+r3*math.sin(a3)
  glVertex2f(x3,y3)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r4 = 1
 cx4=9
 cy4=-21.3
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a4=2*math.pi*i/segments
  x4=cx4+r4*math.cos(a4)
  y4=cy4+r4*math.sin(a4)
  glVertex2f(x4,y4)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r5 = 1
 cx5=10
 cy5=-22
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a5=2*math.pi*i/segments
  x5=cx5+r5*math.cos(a5)
  y5=cy5+r5*math.sin(a5)
  glVertex2f(x5,y5)
 glEnd()
 
 
 glColor3f(0.78,0.77,0.75)
 r1b = 1
 cx1b=5.8
 cy1b=-23
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a1b=2*math.pi*i/segments
  x1b=cx1b+r1b*math.cos(a1b)
  y1b=cy1b+r1b*math.sin(a1b)
  glVertex2f(x1b,y1b)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r2b = 1
 cx2b=4
 cy2b=-22.5
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a2b=2*math.pi*i/segments
  x2b=cx2b+r2b*math.cos(a2b)
  y2b=cy2b+r2b*math.sin(a2b)
  glVertex2f(x2b,y2b)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r3b = 1
 cx3b=4.5
 cy3b=-21.5
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a3b=2*math.pi*i/segments
  x3b=cx3b+r3b*math.cos(a3b)
  y3b=cy3b+r3b*math.sin(a3b)
  glVertex2f(x3b,y3b)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r4b = 1
 cx4b=5.5
 cy4b=-21.3
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a4b=2*math.pi*i/segments
  x4b=cx4b+r4b*math.cos(a4b)
  y4b=cy4b+r4b*math.sin(a4b)
  glVertex2f(x4b,y4b)
 glEnd()
 glColor3f(0.78,0.77,0.75)
 r5b = 1
 cx5b=6.5
 cy5b=-22
 glBegin(GL_TRIANGLE_FAN)
 for i in range(segments+1):
  a5b=2*math.pi*i/segments
  x5b=cx5b+r5b*math.cos(a5b)
  y5b=cy5b+r5b*math.sin(a5b)
  glVertex2f(x5b,y5b)
 glEnd()
 glColor3f(0,0.5,0)
 glTranslatef(5,-8,0)
 glRotatef(30,0,0,1)
 scale=1.4 
 glBegin(GL_POLYGON)
 for i in range(sides):
  angle=i*angle_step
  x=rp*math.cos(angle)
  y=rp*math.sin(angle)
  glVertex2f(x*scale,y*scale)
 glEnd()
 
 glFlush()
def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_RGB)
 glutInitWindowSize(5000,5000)
 glutInitWindowPosition(0,0)
 glutCreateWindow(b"TIME PASS")
 glutDisplayFunc(Circle)
 init()
 glutMainLoop()
main()   
