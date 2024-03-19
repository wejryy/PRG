import random

w, h = 10, 5
mine_cnt = 16

# gene field
field = [[0 for y in range(h)] for x in range(w)]

# put mine on random position
if mine_cnt > w*h:
    mine_cnt = 0
    print("Too many mines!")
for i in range(mine_cnt):
    while True:
        rx = random.randint(0, w - 1)
        ry = random.randint(0, h - 1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            break
# print field
for y in range(h):
    for x in range(w):
        print(field[rx][ry], end="")
    print()