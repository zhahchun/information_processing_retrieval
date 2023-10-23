from turtle import *

post = {'name': 'Ying Chang',
         'content': '恭喜我們友誼的小船十年了還沒翻',
         'hashtag': '#friendship',
         'date': 'Oct. 16, 2023'}

def draw_post(post):
    for v in post.values():
        pendown()
        write(v, font = 20)
        penup()
        setheading(270)
        forward(30)

draw_post(post)
done()
