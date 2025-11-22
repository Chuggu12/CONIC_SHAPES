# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 23:17:06 2025

@author: ANKIT ANAND
"""

"""
ULTRA SIMPLE CONIC SHAPES - EXTENDED VERSION
Run each shape in complete isolation with many new shapes
"""

import os
import subprocess
import sys

def draw_shape_simple(shape_code):
    """Create and run a simple turtle script"""
    script = f
import turtle
import math

# Setup
screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("white")
screen.tracer(0, 0)  # Turn off animation for instant drawing

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

{shape_code}

screen.update()
turtle.exitonclick()
"""
    
    # Write to temporary file
    with open("temp_shape.py", "w") as f:
        f.write(script)
    
    # Run in separate process
    subprocess.run([sys.executable, "temp_shape.py"])
    
    # Clean up
    os.remove("temp_shape.py")

# BASIC CONIC SECTIONS
def ellipse(a, b, h=0, k=0, color="black"):
    """Draw ellipse: x = a*cos(t), y = b*sin(t)"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(73):
    angle = i * 5 * math.pi / 180
    x = {h} + {a} * math.cos(angle)
    y = {k} + {b} * math.sin(angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

def circle(radius, h=0, k=0, color="black"):
    """Draw circle (special ellipse)"""
    ellipse(radius, radius, h, k, color)

def parabola(a, h=0, k=0, color="black", orientation='y'):
    """Draw parabola: y = a*x² or x = a*y²"""
    if orientation == 'y':
        code = f"""
t.color("{color}")
t.penup()
for x in range(-100, 101, 2):
    y_val = {a} * x * x
    t.goto({h} + x, {k} + y_val)
    if x == -100:
        t.pendown()
"""
    else:
        code = f"""
t.color("{color}")
t.penup()
for y in range(-100, 101, 2):
    x_val = {a} * y * y
    t.goto({h} + x_val, {k} + y)
    if y == -100:
        t.pendown()
"""
    draw_shape_simple(code)

def hyperbola(a, b, h=0, k=0, color="black"):
    """Draw hyperbola: x = a*sec(t), y = b*tan(t)"""
    code = f"""
t.color("{color}")
# Right branch
t.penup()
for i in range(-25, 26):
    t_param = i * 0.2
    try:
        x = {h} + {a} / math.cos(t_param)
        y = {k} + {b} * math.tan(t_param)
        if abs(x) < 500 and abs(y) < 500:
            t.goto(x, y)
            if i == -25:
                t.pendown()
    except:
        t.penup()

# Left branch
t.penup()
for i in range(-25, 26):
    t_param = i * 0.2
    try:
        x = {h} - {a} / math.cos(t_param)
        y = {k} + {b} * math.tan(t_param)
        if abs(x) < 500 and abs(y) < 500:
            t.goto(x, y)
            if i == -25:
                t.pendown()
    except:
        t.penup()
"""
    draw_shape_simple(code)

# POLAR CURVES
def cardioid(a, h=0, k=0, color="black"):
    """Draw cardioid: r = a(1 + cos(θ))"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(73):
    angle = i * 5 * math.pi / 180
    r = {a} * (1 + math.cos(angle))
    x = {h} + r * math.cos(angle)
    y = {k} + r * math.sin(angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

def limacon(a, b, h=0, k=0, color="black"):
    """Draw limacon: r = a + b*cos(θ)"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(73):
    angle = i * 5 * math.pi / 180
    r = {a} + {b} * math.cos(angle)
    x = {h} + r * math.cos(angle)
    y = {k} + r * math.sin(angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

def rose_curve(a, n, h=0, k=0, color="black"):
    """Draw rose curve: r = a*cos(nθ)"""
    code = f"""
t.color("{color}")
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
"""
    draw_shape_simple(code)

def spiral(a, b, h=0, k=0, color="black", revolutions=3):
    """Draw Archimedean spiral: r = a + bθ"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(121):
    angle = i * {revolutions} * 2 * math.pi / 120
    r = {a} + {b} * angle
    x = {h} + r * math.cos(angle)
    y = {k} + r * math.sin(angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

# SPECIAL CURVES
def astroid(a, h=0, k=0, color="black"):
    """Draw astroid: x = a*cos³(t), y = a*sin³(t)"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(73):
    angle = i * 5 * math.pi / 180
    x = {h} + {a} * math.cos(angle) ** 3
    y = {k} + {a} * math.sin(angle) ** 3
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

def cycloid(a, h=0, k=0, color="black", revolutions=2):
    """Draw cycloid: x = a(t - sin(t)), y = a(1 - cos(t))"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(121):
    t_param = i * {revolutions} * 2 * math.pi / 120
    x = {h} + {a} * (t_param - math.sin(t_param))
    y = {k} + {a} * (1 - math.cos(t_param))
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

def epitrochoid(R, r, d, h=0, k=0, color="black"):
    """Draw epitrochoid"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(361):
    angle = math.radians(i)
    x = {h} + ({R} + {r}) * math.cos(angle) - {d} * math.cos(({R} + {r}) / {r} * angle)
    y = {k} + ({R} + {r}) * math.sin(angle) - {d} * math.sin(({R} + {r}) / {r} * angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

def hypotrochoid(R, r, d, h=0, k=0, color="black"):
    """Draw hypotrochoid"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(361):
    angle = math.radians(i)
    x = {h} + ({R} - {r}) * math.cos(angle) + {d} * math.cos(({R} - {r}) / {r} * angle)
    y = {k} + ({R} - {r}) * math.sin(angle) - {d} * math.sin(({R} - {r}) / {r} * angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

def lemniscate(a, h=0, k=0, color="black"):
    """Draw lemniscate of Bernoulli: r² = a²*cos(2θ)"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(361):
    angle = math.radians(i)
    try:
        r = {a} * math.sqrt(abs(math.cos(2 * angle)))
        x = {h} + r * math.cos(angle)
        y = {k} + r * math.sin(angle)
        t.goto(x, y)
        if i == 0:
            t.pendown()
    except:
        t.penup()
"""
    draw_shape_simple(code)

def cochleoid(a, h=0, k=0, color="black"):
    """Draw cochleoid: r = a*sin(θ)/θ"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(1, 361):
    angle = math.radians(i)
    try:
        r = {a} * math.sin(angle) / angle
        x = {h} + r * math.cos(angle)
        y = {k} + r * math.sin(angle)
        t.goto(x, y)
        if i == 1:
            t.pendown()
    except:
        t.penup()
"""
    draw_shape_simple(code)

def conchoid(a, b, h=0, k=0, color="black"):
    """Draw conchoid: r = a + b*sec(θ)"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(-60, 61):
    angle = i * 0.1
    try:
        r = {a} + {b} / math.cos(angle)
        x = {h} + r * math.cos(angle)
        y = {k} + r * math.sin(angle)
        t.goto(x, y)
        if i == -60:
            t.pendown()
    except:
        t.penup()
"""
    draw_shape_simple(code)

def cissoid(a, h=0, k=0, color="black"):
    """Draw cissoid of Diocles: y² = x³/(2a - x)"""
    code = f"""
t.color("{color}")
t.penup()
for x in range(1, 2*{a}*10, 1):
    x_val = x / 10.0
    try:
        y_val = math.sqrt(x_val**3 / (2*{a} - x_val))
        t.goto({h} + x_val, {k} + y_val)
        if x == 1:
            t.pendown()
    except:
        pass
        
t.penup()
for x in range(1, 2*{a}*10, 1):
    x_val = x / 10.0
    try:
        y_val = -math.sqrt(x_val**3 / (2*{a} - x_val))
        t.goto({h} + x_val, {k} + y_val)
        if x == 1:
            t.pendown()
    except:
        pass
"""
    draw_shape_simple(code)

def witch_of_agnesi(a, h=0, k=0, color="black"):
    """Draw Witch of Agnesi: y = 8a³/(x² + 4a²)"""
    code = f"""
t.color("{color}")
t.penup()
for x in range(-300, 301, 2):
    x_val = x
    y_val = (8 * {a}**3) / (x_val**2 + 4 * {a}**2)
    t.goto({h} + x_val, {k} + y_val)
    if x == -300:
        t.pendown()
"""
    draw_shape_simple(code)

# 3D PROJECTIONS
def sine_wave(amplitude, frequency, h=0, k=0, color="black"):
    """Draw sine wave: y = amplitude*sin(frequency*x)"""
    code = f"""
t.color("{color}")
t.penup()
for x in range(-200, 201, 2):
    y_val = {amplitude} * math.sin({frequency} * x * 0.05)
    t.goto({h} + x, {k} + y_val * 50)
    if x == -200:
        t.pendown()
"""
    draw_shape_simple(code)

def heart_curve(h=0, k=0, color="red"):
    """Draw mathematical heart curve"""
    code = f"""
t.color("{color}")
t.penup()
for i in range(361):
    angle = math.radians(i)
    x = {h} + 16 * math.sin(angle) ** 3
    y = {k} + 13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle)
    t.goto(x, y)
    if i == 0:
        t.pendown()
"""
    draw_shape_simple(code)

# DEMO FUNCTION
def demo():
    """Run a demo showing multiple shapes"""
    print("Running demo... Close each window to see the next shape.")
    
    shapes = [
        lambda: circle(50, color="red"),
        lambda: ellipse(80, 40, color="blue"),
        lambda: parabola(0.01, color="green"),
        lambda: cardioid(60, color="purple"),
        lambda: rose_curve(70, 3, color="orange"),
        lambda: spiral(10, 5, color="brown"),
        lambda: heart_curve(color="red"),
        lambda: astroid(50, color="cyan")
    ]
    
    for shape_func in shapes:
        shape_func()

# TEST INDIVIDUAL SHAPES
if __name__ == "__main__":
    # Test one shape at a time (uncomment one):
    
    # Basic conic sections
    ellipse(23, 46)                    # Ellipse
    # circle(50)                       # Circle
    # parabola(0.01)                   # Parabola
    # hyperbola(40, 30)                # Hyperbola
    
    # Polar curves
    # cardioid(60)                     # Cardioid
    # limacon(40, 30)                  # Limacon
    # rose_curve(70, 4)                # 4-petal rose
    # spiral(10, 5)                    # Spiral
    
    # Special curves
    # astroid(50)                      # Astroid
    # cycloid(20)                      # Cycloid
    # epitrochoid(90, 30, 15)          # Epitrochoid
    # hypotrochoid(90, 30, 15)         # Hypotrochoid
    # lemniscate(50)                   # Lemniscate
    # cochleoid(100)                   # Cochleoid
    # conchoid(20, 30)                 # Conchoid
    # cissoid(30)                      # Cissoid
    # witch_of_agnesi(30)              # Witch of Agnesi
    
    # Other curves
    # sine_wave(2, 3)                  # Sine wave
    # heart_curve()                    # Heart curve
    
    # Demo all shapes
    # demo()