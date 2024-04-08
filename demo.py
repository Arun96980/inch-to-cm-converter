
import turtle as t
import random

t.speed("fastest")

t.colormode(255)
def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color = (r,g,b)
  return color

def d_spirograph(sz):
  for i in range(int(360/sz)):
    t.color(random_color())
    t.circle(100)
    t.setheading(t.heading()+ sz)


d_spirograph(8)
t.exitonclick()