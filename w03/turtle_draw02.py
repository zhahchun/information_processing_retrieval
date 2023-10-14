import turtle as t
import time
### methods of turtle
# t.shape('turtle')
# t.hideturtle()
# t.showturtle()
# t.forward()
# t.backward()
# t.right()
# t.left()
# t.setheading()
# t.penup()
# t.pendown()
# t.setposition()  #t.setpos(), t.goto()
# t.clear() # clear drawing only
# t.reset() # + set turtle back to default
# t.circle()
# t.speed()
# t.tracer() + t.update()
# t.color()
# t.pensize() == t.width()
# t.bgcolor()
# t.begin_fill + t.end_fill

# for i in range(3):
#     t.fd(100 - i * 10)
#     t.left(90)

# t.reset()
# # t.clear()
# # t.penup()
# # t.setposition(100, -100)
# # t.pendown()
# t.right(90)
# t.forward(100)


# square
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

# square(60)
# square(100)
# square(200)

# t.reset()
# t.speed(1)
# t.tracer(0, 0)
# t.circle(100, extent = 180, steps = 5)
# t.reset()
# t.bgcolor('yellow')
# t.color('blue')
# t.pensize(5)
# t.circle(-100)
# # t.update()

# # draw circles
# t.reset()
# t.color('red')
# t.tracer(0, 0)
# for angle in range(0, 360, 15):
#     t.seth(angle)
#     t.circle(100)
# t.update()
# time.sleep(1)

# # draw maze
# colors = ["blue", "green", "purple", "cyan", "magenta", "violet", "yellow", "black"]
# t.reset()
# t.tracer(0, 0)
# for i in range(48):
#     t.color(colors[i % 8])
#     t.fd(2 + i * 5)
#     t.left(45)
#     t.width(i)

# t.update()
# time.sleep(3)

# # check fill color
# t.tracer(0, 0)
# t.reset()
# t.color('green')
# t.begin_fill()
# square(100)
# t.end_fill()
# t.update()
# time.sleep(1)

t.reset()
t.width(10)
t.begin_fill()
t.fd(100)
t.seth(45)
t.fd(100)
t.seth(90)
t.fd(100)
t.color('blue')
t.end_fill()
time.sleep(1)
