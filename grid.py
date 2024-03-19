import json

class Grid:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.grid = json.load(file)

    def print(self):
        for row in self.grid:
            print(row)

    def get(self, x, y):
        return self.grid[y][x]
    
    def set(self, x, y, value):
        self.grid[y][x] = value
    
    def size(self):
        return len(self.grid)
    
    def rotate(self):
        self.grid = list(map(list, zip(*self.grid[::-1])))
    