"""
CONIC SHAPES - 
ENVIRONMENT 


"""

import turtle
import math


def reset_turtle_environment():
    """Completely reset the turtle environment"""
    turtle.clearscreen()
    turtle.TurtleScreen._RUNNING = True  # Reset the internal state


def draw_ellipse(a, b, h=0, k=0, color="black"):
    """Draw an ellipse - standalone function"""
    reset_turtle_environment()

    # Create screen
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0, 0)  # No animation

    # Create turtle
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(color)
    t.penup()

    # Draw ellipse
    for i in range(73):
        angle = i * 5 * math.pi / 180
        x = h + a * math.cos(angle)
        y = k + b * math.sin(angle)
        t.goto(x, y)
        if i == 0:
            t.pendown()

    screen.update()
    return t, screen


def draw_circle(radius, h=0, k=0, color="black"):
    """Draw a circle"""
    return draw_ellipse(radius, radius, h, k, color)


def draw_parabola(a, h=0, k=0, color="black", orientation='y'):
    """Draw a parabola"""
    reset_turtle_environment()

    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(color)
    t.penup()

    if orientation == 'y':
        for x in range(-80, 81, 2):
            y_val = a * x * x
            t.goto(h + x, k + y_val)
            if x == -80:
                t.pendown()
    else:
        for y in range(-80, 81, 2):
            x_val = a * y * y
            t.goto(h + x_val, k + y)
            if y == -80:
                t.pendown()

    screen.update()
    return t, screen


def draw_cardioid(a, h=0, k=0, color="black"):
    """Draw a cardioid"""
    reset_turtle_environment()

    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(color)
    t.penup()

    for i in range(73):
        angle = i * 5 * math.pi / 180
        r = a * (1 + math.cos(angle))
        x = h + r * math.cos(angle)
        y = k + r * math.sin(angle)
        t.goto(x, y)
        if i == 0:
            t.pendown()

    screen.update()
    return t, screen


def draw_rose(a, n, h=0, k=0, color="black"):
    """Draw a rose curve"""
    reset_turtle_environment()

    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(color)
    t.penup()

    points = 144
    for i in range(points + 1):
        angle = i * 2 * math.pi / points
        r = a * math.cos(n * angle)
        x = h + r * math.cos(angle)
        y = k + r * math.sin(angle)
        t.goto(x, y)
        if i == 0:
            t.pendown()

    screen.update()
    return t, screen


def draw_spiral(a, b, h=0, k=0, color="black", revolutions=2):
    """Draw a spiral"""
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(color)
    t.penup()

    for i in range(61):
        angle = i * revolutions * 2 * math.pi / 60
        r = a + b * angle
        x = h + r * math.cos(angle)
        y = k + r * math.sin(angle)
        t.goto(x, y)
        if i == 0:
            t.pendown()

    return t

def limacon(self, a, b, h=0, k=0, color="black", pen_size=2):
     """Draw a limacon curve: r = a + b*cos(theta)."""
     self.setup_screen()
     t = self.create_turtle(color, pen_size)
     
     num_points = 100
     t.up()
     
     for i in range(num_points + 1):
         theta = (i / num_points) * 2 * math.pi
         r = a + b * math.cos(theta)
         x = h + r * math.cos(theta)
         y = k + r * math.sin(theta)
         
         if i == 0:
             t.up()
             t.goto(x, y)
             t.down()
         else:
             t.goto(x, y)
     
     self.screen.update()
     return t
 
def rectangular_hyperbola(self, a, h=0, k=0, color="black", pen_size=2):
        """Draw a rectangular hyperbola (special case where a = b)."""
        return self.hyperbola(a, a, h, k, color, True, pen_size)

def keep_open():
    """Keep window open - call this after drawing"""
    turtle.exitonclick()

def quick_ellipse(a, b):
    """Quick test function for ellipse"""
    draw_ellipse(a, b)
    keep_open()

def quick_circle(radius):
    """Quick test function for circle"""
    draw_circle(radius)
    keep_open()

def quick_cardioid(a):
    """Quick test function for cardioid"""
    draw_cardioid(a)
    keep_open()

# INDIVIDUAL SHAPE TESTING - Use these functions
def test_ellipse():
    """Test ellipse individually"""
    quick_ellipse(23, 46)

def test_circle():
    """Test circle individually"""
    quick_circle(50)

def test_cardioid():
    """Test cardioid individually"""
    quick_cardioid(60)

def test_rose():
    """Test rose individually"""
    draw_rose(60, 4)
    keep_open()

# Run individual tests - UNCOMMENT ONLY ONE LINE BELOW
if __name__ == "__main__":
    # TEST ONE SHAPE AT A TIME:
    
    test_ellipse()    # Test ellipse
    #test_circle()    # Test circle
    # test_cardioid() # Test cardioid
    # test_rose()     # Test rose