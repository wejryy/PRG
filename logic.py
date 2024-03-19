import random
color = {
    "r": "red",
    "g": "green",
    "b": "blue",
    "c": "cyan",
    "m": "magenta",
    "y": "yellow",
    "k": "black",
    "w": "white"
}
key = []
for code in color:
    key.append(code)
rnd = random.randint(0, 7)
print(color[key[rnd]])

secret = []
cnt_field = 3
cnt_color = 5


