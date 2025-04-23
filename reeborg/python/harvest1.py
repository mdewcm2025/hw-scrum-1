def move_and_pick():
    while object_here():
        take()
    move()

def harvest_row():
    for _ in range(5):
        move_and_pick()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def move_to_next_row():
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    elif left_is_clear():
        turn_left()
        move()
        turn_left()

# Main program
for _ in range(3):  # There are 3 rows to harvest
    harvest_row()
    move_to_next_row()

harvest_row()  # Harvest the last row