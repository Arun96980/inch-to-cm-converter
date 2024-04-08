import turtle as t
import random

t.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

vibrant_colors = [
   (255, 0, 255),  # Bright magenta
   (50, 205, 50),  # Energetic green
  (0, 229, 238),  # Tropical blue-green
   (125, 180, 230),  # Shocking blue
   (255, 105, 180),  # Bold pink
  (255, 215, 0),  # Cheerful yellow
   (255, 165, 0),  # Zesty orange
 (150, 0, 24),  # Deep, vibrant red
   (135, 60, 225),  # Rich purple
]

t.setheading(225)
t.forward(300)
t.setheading(0)
n_dots = 100

for i in range(1,n_dots+1):
    t.dot(20,random.choice(vibrant_colors))
    t.forward(50)

    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


t.Screen()
t.exitonclick()