from turtle import *
hideturtle()
penup()
left(180)
forward(150)
left(90)
forward(100)
pendown()

# flag
begin_fill()
color('blue')
for i in range(2):
    left(90)
    forward(300)
    left(90)
    forward(200)
end_fill()
left(90)
forward(300)
left(90)

# half circle
begin_fill()
color('yellow')
circle(radius=150, extent=180)
end_fill()


color('blue')
left(90)
forward(125)

left(90)
forward(100)
# triangle
begin_fill()
color('white')
right(30)
forward(50)
right(120)
forward(50)
right(120)
forward(50)
backward(50)
end_fill()
color('blue')
left(90)
forward(100)

# rectangle
begin_fill()
color('light blue')

for i in range(2):
    right(90)
    forward(50)
    right(90)
    forward(100)

end_fill()
color('blue')
right(90)
forward(50)
done()