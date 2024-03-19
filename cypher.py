from grid import Grid

grid = Grid("grid_02.json")
grid.print()

for i in range(4):
    grid.rotate()
    grid.print()
    print(4)