import turtle
import copy

base = []
turtleID = []
block_size = 20         # can modify - block size
width = 900             # can modify - screen width
no_of_col = int((width - 100)/block_size)
height = 900            # can modify - screen height
no_of_row = int((height - 100)/block_size)
turtle.setup(width, height)
turtle.tracer(0)
refresh_period = 200    # can modify - refresh period (in ms)
stop = True


def main_loop():
    global base, stop
    if not stop:
        temp_base = copy.deepcopy(base)
        for row in range(no_of_row):
            for col in range(no_of_col):
                sum = 0
                for i in range(3):
                    for j in range(3):
                        if 0 <= row - 1 + i < no_of_row:
                            if 0 <= col - 1 + j < no_of_col:
                                if i == 1 and j == 1:
                                    continue
                                else:
                                    sum = sum + base[row - 1 + i][col - 1 + j]
                if sum == 3:
                    temp_base[row][col] = 1
                elif sum == 2:
                    pass
                    temp_base[row][col] = base[row][col]
                else:
                    temp_base[row][col] = 0
        base = temp_base
        for row in range(no_of_row):
            for col in range(no_of_col):
                if base[row][col] == 0:
                    turtleID[row][col].fillcolor("")
                else:
                    turtleID[row][col].fillcolor("grey")
    turtle.ontimer(main_loop, refresh_period)
    turtle.update()


def pause_program():
    global stop
    stop = not stop
    print(stop)
    turtle.update()


def update_state(x, y):
    pass


def clear():
    global base
    for row in range(no_of_row):
        for col in range(no_of_col):
            base[row][col] = 0
            turtleID[row][col].fillcolor("")
    turtle.update()


def change_state(x, y):
    global base
    row = - 1 - round((y - int(height-100)/2)/block_size - 0.5)
    col = round((x + int(width-100)/2)/block_size - 0.5)
    if turtleID[row][col].fillcolor() == "":
        turtleID[row][col].fillcolor("grey")
        base[row][col] = 1
    else:
        turtleID[row][col].fillcolor("")
        base[row][col] = 0
    turtle.update()


for row in range(no_of_row):
    base.append([])
    turtleID.append([])
    for col in range(no_of_col):
        base[row].append(0)
        new_turtle = turtle.Turtle()
        new_turtle.shape("square")
        new_turtle.shapesize(block_size/20, block_size/20)
        new_turtle.fillcolor("")
        new_turtle.up()
        new_turtle.goto(-(width-100)/2 + block_size * (col + 0.5), (height-100)/2 - block_size * (row + 0.5))
        new_turtle.onclick(change_state)
        turtleID[row].append(new_turtle)

# if not stop:
#     turtle.onkeypress(main_loop, "space")
# else:
#     turtle.onkeypress(stop_program(), "space")

main_loop()

turtle.onkeypress(pause_program, "space")
turtle.onkeypress(clear, "Delete")
turtle.listen()

turtle.update()

turtle.done()
