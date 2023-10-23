

def next_color(current_color):
    if current_color == 'red':
        return 'black'
    elif current_color == 'black':
        return 'red'


### Do not edit below this line

col = "red"
print("The current color is", col)
col = next_color(col)
print("The current color is", col)
col = next_color(col)
print("The current color is", col)
col = next_color(col)
print("The current color is", col)
col = next_color(col)
print("The current color is", col)
