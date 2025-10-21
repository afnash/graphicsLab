from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# -----------------------------
# Global Variables
# -----------------------------
angle = 0.0        # rotation angle
speed = 2.0        # rotation speed
tx = -200.0        # initial translation (start from left)
direction = 1      # movement direction (1 → right, -1 → left)
move_speed = 2.0   # speed of horizontal motion

# -----------------------------
# Initialization
# -----------------------------
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)      # black background
    gluOrtho2D(-300, 300, -300, 300)      # 2D orthographic projection

# -----------------------------
# Function to Draw Triangle
# -----------------------------
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)        # pivot vertex (rotation point)
    glVertex2f(100, 0)      # bottom-right
    glVertex2f(50, 100)     # top vertex
    glEnd()

# -----------------------------
# Display Function
# -----------------------------
def display():
    global tx, angle

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)  # green triangle

    glPushMatrix()

    # Step 1: Move the whole triangle left ↔ right
    glTranslatef(tx, 0, 0)

    # Step 2: Rotate around its own vertex (pivot)
    glTranslatef(0, 0, 0)         # pivot position (0,0)
    glRotatef(angle, 0, 0, 1)
    glTranslatef(0, 0, 0)         # move back (pivot stays fixed in local frame)

    draw_triangle()

    glPopMatrix()
    glFlush()

# -----------------------------
# Timer Function
# -----------------------------
def update(value):
    global angle, tx, direction

    # Continuous rotation
    angle += speed
    if angle >= 360:
        angle = 0

    # Move left ↔ right
    tx += move_speed * direction

    # Reverse direction at boundaries
    if tx > 200 or tx < -200:
        direction *= -1

    glutPostRedisplay()
    glutTimerFunc(30, update, 0)

# -----------------------------
# Main Function
# -----------------------------
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangle Rotating w.r.t Vertex + Translating Left <-> Right")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(30, update, 0)
    glutMainLoop()

main()

