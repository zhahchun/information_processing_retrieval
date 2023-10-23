import curses, time
def main(screen):
    # pass
    curses.curs_set(0)  # hide the cursor
    screen.nodelay(True)  # don't block I/O cursor <-- cuased by getch()

    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1)
    }

    direction = directions[curses.KEY_RIGHT]
    snake = [(0, i) for i in reversed(range(20))]

    while True:
        screen.erase()
        # draw the snake
        screen.addstr(*snake[0], '@')
        for segment in snake[1:]:
            screen.addstr(*segment, '*')

        # move the snake
        snake.pop()  # default: -1
        snake.insert(0, tuple(map(sum, zip(snake[0], direction))))

        # change direction on arrow keystroke
        direction = directions.get(screen.getch(), direction)

        # list.pop(): A number specifying the position of the element you want to remove, 
        # default value is -1, which returns the last item
        # map(): executes a specified function for each item in an iterable. 
        # The item is sent to the function as a parameter.
        # zip(): returns a zip object, which is an iterator of tuples where the first item 
        # in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
        # If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
        # in my words:
        # -- zip(): value in the same position combined to a new tuple
        # -- sum(): values in the same tuple summed up to a total number
        # -- map(): repeat the function with variables
        # -- tuple(): convert the map into a tuple, for readability
        # dictionary.get(keyname, value): The keyname of the item you want to return the value from
        # A value to return if the specified key does not exist. Default value None

        screen.refresh()
        time.sleep(0.5)

if __name__ == '__main__':
    curses.wrapper(main)