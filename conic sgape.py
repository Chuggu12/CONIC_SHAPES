import turtle
import math


class ConicDrawer:
    def __init__(self):
        self.screen = None
        self.turtles = []  # Keep references to all turtles
        
    def setup_screen(self, title="Conic Sections", width=800, height=600):
        """Set up the turtle screen once."""
        if self.screen is None:
            self.screen = turtle.Screen()
            self.screen.title(title)
            self.screen.setup(width, height)
            self.screen.tracer(0)  # Turn off animation for faster drawing
        return self.screen
    
    def create_turtle(self):
        """Create and configure a new turtle."""
        t = turtle.Turtle()
        t.speed(0)  # Fastest
        t.hideturtle()
        self.turtles.append(t)  # Keep reference to prevent garbage collection
        return t
    
    def ellipse(self, a, b, h=0, k=0, angle=360, angle_unit='d', color="black"):
        """Draw an ellipse with given parameters."""
        self.setup_screen()
        t = self.create_turtle()
        t.color(color)
        
        # Convert angle based on unit
        if angle_unit == 'r':  # radians
            total_angle = angle
        else:  # degrees (default)
            total_angle = math.radians(angle)
        
        # Calculate number of points for smooth curve
        circumference = math.pi * (3*(a + b) - math.sqrt((3*a + b)*(a + 3*b)))
        num_points = max(50, int(circumference / 10))
        
        t.up()
        for i in range(num_points + 1):
            theta = (i / num_points) * total_angle
            x = h + a * math.cos(theta)
            y = k + b * math.sin(theta)
            
            if i == 0:
                t.up()
                t.goto(x, y)
                t.down()
            else:
                t.goto(x, y)
        
        self.screen.update()
        return t
    
    def parabola(self, a, t_range, orientation, h=0, k=0, color="black"):
        """Draw a parabola with given parameters."""
        self.setup_screen()
        t = self.create_turtle()
        t.color(color)
        
        step = t_range / 100  # Adaptive step size
        
        t.up()
        if orientation == 'x':
            # x = a*y^2 form
            for i in range(-100, 101):
                y = i * step
                x = h + a * y * y
                y_pos = k + y
                
                if i == -100:
                    t.up()
                    t.goto(x, y_pos)
                    t.down()
                else:
                    t.goto(x, y_pos)
                    
        elif orientation == 'y':
            # y = a*x^2 form
            for i in range(-100, 101):
                x = i * step
                y = k + a * x * x
                x_pos = h + x
                
                if i == -100:
                    t.up()
                    t.goto(x_pos, y)
                    t.down()
                else:
                    t.goto(x_pos, y)
        
        self.screen.update()
        return t
    
    def hyperbola(self, a, b, h=0, k=0, color="black", draw_both_branches=True):
        """Draw a hyperbola with given parameters."""
        self.setup_screen()
        t = self.create_turtle()
        t.color(color)
        
        # Parametric equations for hyperbola: x = a*sec(t), y = b*tan(t)
        t.up()
        
        # Right branch
        for i in range(-80, 80):
            param = i * 0.1
            try:
                x = h + a / math.cos(param)
                y = k + b * math.tan(param)
                
                if abs(x) > 10000 or abs(y) > 10000:  # Skip asymptote regions
                    t.up()
                    continue
                    
                if i == -80:
                    t.up()
                    t.goto(x, y)
                    t.down()
                else:
                    t.goto(x, y)
            except (ValueError, ZeroDivisionError):
                t.up()
                continue
        
        if draw_both_branches:
            # Left branch
            t.up()
            for i in range(-80, 80):
                param = i * 0.1
                try:
                    x = h - a / math.cos(param)
                    y = k + b * math.tan(param)
                    
                    if abs(x) > 10000 or abs(y) > 10000:  # Skip asymptote regions
                        t.up()
                        continue
                        
                    if i == -80:
                        t.up()
                        t.goto(x, y)
                        t.down()
                    else:
                        t.goto(x, y)
                except (ValueError, ZeroDivisionError):
                    t.up()
                    continue
        
        self.screen.update()
        return t
    
    def rectangular_hyperbola(self, a, h=0, k=0, color="black", pen_size=2):
        """Draw a rectangular hyperbola (special case where a = b)."""
        return self.hyperbola(a, a, h, k, color, True, pen_size)
    
    def cardioid(self, a, h=0, k=0, color="black", pen_size=2):
        """Draw a cardioid curve."""
        self.setup_screen()
        t = self.create_turtle(color, pen_size)
        
        num_points = 100
        t.up()
        
        for i in range(num_points + 1):
            theta = (i / num_points) * 2 * math.pi
            r = a * (1 + math.cos(theta))
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
    
    def rose_curve(self, a, n, d=0, h=0, k=0, color="black", pen_size=2):
        """Draw a rose curve: r = a*cos(n*theta + d)."""
        self.setup_screen()
        t = self.create_turtle(color, pen_size)
        
        # Determine number of petals
        if n % 1 == 0:  # n is integer
            petals = n if n % 2 == 0 else n
            range_multiplier = 1 if n % 2 == 0 else 2
        else:  # n is rational
            petals = abs(n)
            range_multiplier = 2
        
        num_points = 200
        t.up()
        
        for i in range(num_points + 1):
            theta = (i / num_points) * range_multiplier * math.pi
            r = a * math.cos(n * theta + d)
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
    
    def spiral(self, a, b, h=0, k=0, revolutions=3, color="black", pen_size=2):
        """Draw an Archimedean spiral: r = a + b*theta."""
        self.setup_screen()
        t = self.create_turtle(color, pen_size)
        
        num_points = 200
        t.up()
        
        for i in range(num_points + 1):
            theta = (i / num_points) * revolutions * 2 * math.pi
            r = a + b * theta
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
    
    def astroid(self, a, h=0, k=0, color="black", pen_size=2):
        """Draw an astroid curve."""
        self.setup_screen()
        t = self.create_turtle(color, pen_size)
        
        num_points = 100
        t.up()
        
        for i in range(num_points + 1):
            theta = (i / num_points) * 2 * math.pi
            x = h + a * math.cos(theta) ** 3
            y = k + a * math.sin(theta) ** 3
            
            if i == 0:
                t.up()
                t.goto(x, y)
                t.down()
            else:
                t.goto(x, y)
        
        self.screen.update()
        return t
    
    def cycloid(self, a, h=0, k=0, revolutions=2, color="black", pen_size=2):
        """Draw a cycloid curve."""
        self.setup_screen()
        t = self.create_turtle(color, pen_size)
        
        num_points = 200
        t.up()
        
        for i in range(num_points + 1):
            theta = (i / num_points) * revolutions * 2 * math.pi
            x = h + a * (theta - math.sin(theta))
            y = k + a * (1 - math.cos(theta))
            
            if i == 0:
                t.up()
                t.goto(x, y)
                t.down()
            else:
                t.goto(x, y)
        
        self.screen.update()
        return t
    
    def draw_axes(self, color="gray", pen_size=1):
        """Draw coordinate axes for reference."""
        self.setup_screen()
        t = self.create_turtle(color, pen_size)
        
        # X-axis
        t.up()
        t.goto(-400, 0)
        t.down()
        t.goto(400, 0)
        
        # Y-axis
        t.up()
        t.goto(0, -300)
        t.down()
        t.goto(0, 300)
        
        self.screen.update()
        return t
    
    def clear(self):
        """Clear all drawings."""
        for t in self.turtles:
            t.clear()
        self.turtles.clear()
    
    def reset(self):
        """Reset everything."""
        self.clear()
        if self.screen:
            self.screen.clear()
        self.turtles = []
    
    def keep_open(self):
        """Keep the window open until clicked."""
        if self.screen:
            self.screen.exitonclick()


# Simple function-based interface
_drawer = ConicDrawer()

# Original conic sections
def ellipse(a, b, h=0, k=0, angle=360, angle_unit='d', color="black", pen_size=2):
    return _drawer.ellipse(a, b, h, k, angle, angle_unit, color, pen_size)

def parabola(a, t_range, orientation, h=0, k=0, color="black", pen_size=2):
    return _drawer.parabola(a, t_range, orientation, h, k, color, pen_size)

def hyperbola(a, b, h=0, k=0, color="black", draw_both_branches=True, pen_size=2):
    return _drawer.hyperbola(a, b, h, k, color, draw_both_branches, pen_size)

# New conic shapes
def circle(radius, h=0, k=0, color="black", pen_size=2):
    return _drawer.circle(radius, h, k, color, pen_size)

def cardioid(a, h=0, k=0, color="black", pen_size=2):
    return _drawer.cardioid(a, h, k, color, pen_size)

def limacon(a, b, h=0, k=0, color="black", pen_size=2):
    return _drawer.limacon(a, b, h, k, color, pen_size)

def rose_curve(a, n, d=0, h=0, k=0, color="black", pen_size=2):
    return _drawer.rose_curve(a, n, d, h, k, color, pen_size)

def spiral(a, b, h=0, k=0, revolutions=3, color="black", pen_size=2):
    return _drawer.spiral(a, b, h, k, revolutions, color, pen_size)

def astroid(a, h=0, k=0, color="black", pen_size=2):
    return _drawer.astroid(a, h, k, color, pen_size)

def cycloid(a, h=0, k=0, revolutions=2, color="black", pen_size=2):
    return _drawer.cycloid(a, h, k, revolutions, color, pen_size)

def rectangular_hyperbola(a, h=0, k=0, color="black", pen_size=2):
    return _drawer.rectangular_hyperbola(a, h, k, color, pen_size)

# Utility functions
def draw_axes(color="gray", pen_size=1):
    return _drawer.draw_axes(color, pen_size)

def clear_drawing():
    _drawer.clear()


def demo():
    """Demonstrate all conic sections."""
    # Draw ellipse
    ellipse(50, 25, -200, 100, color="blue")
    
    # Draw parabola
    parabola(0.1, 40, 'y', 100, -100, color="red")
    
    # Draw hyperbola
    hyperbola(50, 30, 0, 0, color="green")
    
    # Keep window open
    _drawer.keep_open()
    


