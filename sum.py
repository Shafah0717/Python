import turtle

# Create the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Function to draw a single hexagon
def hexagon(t, length):
    """Draws a hexagon with the given side length."""
    for count in range(6):
        t.forward(length)
        t.left(60)

# Function to draw multiple hexagons in a circular pattern
def radialHexagons(t, n, length):
    """Draws a radial pattern of n hexagons with the given length."""
    for count in range(n):
        hexagon(t, length)
        t.left(90 / n)  # Rotate to place the next hexagon

# Call the function to draw 10 hexagons with side length 50
radialHexagons(t, 10, 50)

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
