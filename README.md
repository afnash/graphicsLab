# graphicsLab

S5 Computer Graphics lab code and exam items.

## Description

This repository contains the lab programs for the Computer Graphics course (S5). All code is written in Python. Exam-related programs and test/assessment items are placed inside the `test` folder.

## Repository layout

- `test/` — Exam items and test programs (these are the files you will find during practicals/exams).
- Other Python scripts — Lab exercises and example implementations using OpenGL.

## Requirements

- Python 3.8+ (or latest stable Python 3.x)
- PyOpenGL for OpenGL bindings:
  - PyOpenGL
  - (optional but recommended) PyOpenGL_accelerate
- A window/context provider for OpenGL (varies by script). Common options:
  - freeglut/GLUT (used by many simple PyOpenGL examples)
  - GLFW
  - SDL2 (via pysdl2) — only if a script requires it
- Pillow (optional, for image handling, if used by specific scripts)

Install common dependencies with:
pip install PyOpenGL PyOpenGL_accelerate Pillow

Note: Some systems require a native OpenGL/windowing library (for example freeglut or GLFW). Refer to your OS package manager or the individual script headers for specific setup instructions.

## How to run

1. Clone the repository:
   git clone https://github.com/afnash/graphicsLab.git
2. Change into the project directory:
   cd graphicsLab
3. Run a lab script or a test file with Python:
   python path/to/script.py

Example:
python test/your_exam_program.py

If a script opens an OpenGL window, make sure your environment supports GUI windows (desktop or appropriate virtual display). Check the top of each script for required imports and any notes about which window/context library it needs.

## Notes about the `test` folder

- The `test` folder contains exam items and solutions used for practical assessments.
- File names typically indicate the exercise number or topic. Open the files to see usage notes and any sample inputs.
- Use the test files to practice typical exam problems and to validate implementations from the lab exercises.



## Contact

Repository owner: [afnash](https://github.com/afnash)
