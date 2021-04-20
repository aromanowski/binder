print("Opening and testing python files with Binder")

### Draw an ellipse
# Original source: https://www.geeksforgeeks.org/draw-ellipse-using-turtle-in-python/

# import library
import turtle
screen = turtle.Screen()
  
# function to draw an ellipse
def draw_ellipse(radius):
  for i in range(2):
    turtle.circle(radius,90)
    turtle.circle(radius//2,90)
  
################
# Main section #
################

# Set screen size and colour
screen.setup(500,500)
screen.bgcolor('black')

# tilt the shape to 45 degrees
turtle.seth(45)
  
# calling draw function
draw_ellipse(100)

