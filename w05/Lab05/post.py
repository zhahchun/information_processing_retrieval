import pprint

post1 = {'name': 'Ying Chang',
         'content': '恭喜我們友誼的小船十年了還沒翻',
         'hashtag': '',
         'date': 'Oct. 16, 2023'}

post2 = {'name': 'cindy821011',
         'content': '【曼谷🇹🇭231008 Day③】',
         'hashtag': '#泰國 #曼谷',
         'date': 'Oct. 14, 2023'}

post3 = {'name': 'vivian07103',
         'content': '不用早起也能玩超過癮的東京9天紀錄🇯🇵',
         'hashtag': '',
         'date': 'Oct. 15, 2023'}
 
post4 = {'name': 'suntsaihsuan',
         'content': 'Can’t believe I bought this anyway!!! Shout out to Sara Betts',
         'hashtag': '#aiyearbook',
         'date': 'Oct. 14, 2023'}

def print_post(post):
    pprint.pprint(post)
    print()

print_post(post1)
print_post(post2)
print_post(post3)
print_post(post4)
