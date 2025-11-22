# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 21:58:46 2025

@author: ANKIT ANAND
"""

"""
CONIC SHAPES - ULTRA SIMPLE VERSION
Each shape runs in its own completely independent environment
"""

import math
import subprocess
import sys
import os

def create_standalone_script(shape_name, code):
    """Create a standalone Python file for each shape"""
    filename = f"draw_{shape_name}.py"
    with open(filename, 'w') as f:
        f.write(code)
    return filename

def run_standalone_script(filename):
    """Run a standalone script"""
    try:
        subprocess.run([sys.executable, filename], check=True)
        os.remove(filename)  # Clean up
        return True
    except:
        return False

# Template for standalone shape scripts
SHAPE_TEMPLATE = '''
import turtle
import math

# Setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color("{color}")

{drawing_code}

screen.update()
turtle.exitonclick()
'''

# Individual shape functions that create standalone scripts
def ellipse(a, b, h=0, k=0, color="black"):
    """Draw ellipse in standalone environment"""
    drawing_code = f'''
t.penup()
for i in range(73):
    angle = i * 5 * math.pi / 180
    x = {h} + {a} * math.cos(angle)
    y = {k} + {b} * math.sin(angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
'''
    script = SHAPE_TEMPLATE.format(color=color, drawing_code=drawing_code)
    filename = create_standalone_script("ellipse", script)
    run_standalone_script(filename)

def circle(radius, h=0, k=0, color="black"):
    """Draw circle in standalone environment"""
    drawing_code = f'''
t.penup()
t.goto({h} + {radius}, {k})
t.pendown()
t.circle({radius})
'''
    script = SHAPE_TEMPLATE.format(color=color, drawing_code=drawing_code)
    filename = create_standalone_script("circle", script)
    run_standalone_script(filename)

def cardioid(a, h=0, k=0, color="black"):
    """Draw cardioid in standalone environment"""
    drawing_code = f'''
t.penup()
for i in range(73):
    angle = i * 5 * math.pi / 180
    r = {a} * (1 + math.cos(angle))
    x = {h} + r * math.cos(angle)
    y = {k} + r * math.sin(angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
'''
    script = SHAPE_TEMPLATE.format(color=color, drawing_code=drawing_code)
    filename = create_standalone_script("cardioid", script)
    run_standalone_script(filename)

def parabola(a, h=0, k=0, color="black", orientation='y'):
    """Draw parabola in standalone environment"""
    if orientation == 'y':
        drawing_code = f'''
t.penup()
for x in range(-80, 81, 2):
    y_val = {a} * x * x
    t.goto({h} + x, {k} + y_val)
    if x == -80:
        t.pendown()
'''
    else:
        drawing_code = f'''
t.penup()
for y in range(-80, 81, 2):
    x_val = {a} * y * y
    t.goto({h} + x_val, {k} + y)
    if y == -80:
        t.pendown()
'''
    script = SHAPE_TEMPLATE.format(color=color, drawing_code=drawing_code)
    filename = create_standalone_script("parabola", script)
    run_standalone_script(filename)

def rose(a, n, h=0, k=0, color="black"):
    """Draw rose curve in standalone environment"""
    drawing_code = f'''
t.penup()
points = 144
for i in range(points + 1):
    angle = i * 2 * math.pi / points
    r = {a} * math.cos({n} * angle)
    x = {h} + r * math.cos(angle)
    y = {k} + r * math.sin(angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
'''
    script = SHAPE_TEMPLATE.format(color=color, drawing_code=drawing_code)
    filename = create_standalone_script("rose", script)
    run_standalone_script(filename)

# SIMPLE USAGE:
if __name__ == "__main__":
    # Test individual shapes - these will each open in their own window
    ellipse(23, 46)
    # circle(50)
    # cardioid(60)
    # parabola(0.01)
    # rose(60, 4)