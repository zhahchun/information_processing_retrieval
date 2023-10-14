import turtle

# # right-angled triangle
# turtle.forward(200)
# turtle.left(90)
# turtle.forward(200)
# turtle.left(135)
# c = ((200**2) + (200**2))** 0.5
# turtle.forward(c)

# # square
# for i in range(4):
#     turtle.forward(200)
#     turtle.left(90)

# # rectangle
# def rectangle(width, height):
#     for i in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)   

# rectangle(300, 150)

# # circle
# def circle(width):
#     for i in range(360):
#         turtle.forward(width)
#         turtle.left(1)

# circle(2)

# # star: inner angle 為所對弧長 基本180/n角 隨著所對弧長增加 增加內角
# def star(width, angle, n):
#     for i in range(n):
#         turtle.forward(width)
#         turtle.left(180 - angle)

# # basic正五邊形 180/5
# star(200, 180/5, 5)

# # exercise 03
# count = 0
# while(count < 180):
#     turtle.forward(2)
#     turtle.right(1)
#     count = count + 1
# turtle.right(45)
# turtle.forward(300)
# turtle.left(90)
# turtle.back(150)
# turtle.right(45)
# turtle.back(250)

# # exercise 04
# big_line = 100
# little_line = 50
# angle = 90
# turtle.left(angle)
# turtle.forward(big_line)
# count = 0
# while count < 4:
#     turtle.right(angle//2)
#     if count != 3:
#         turtle.forward(little_line)
#     else:
#         turtle.forward(big_line)
#     count = count + 1
# turtle.right(90)
# turtle.forward(130)

