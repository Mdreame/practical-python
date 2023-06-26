# bounce.py
#
# Exercise 1.5

def init_bounce(height, times):
    which_time = 1
    while which_time <= times:
        height = round(height * 3 / 5, 4)
        print(which_time, height)
        which_time += 1

init_bounce(100, 10)
