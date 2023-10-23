import random
heads = 0
number = input('Please give me a number: ')
number = int(number)

for i in range(number):
  num = random.randint(1,2)
  if (num == 1):
    heads = heads + 1

print('heads: ', heads, ' tails: ', number-heads)
