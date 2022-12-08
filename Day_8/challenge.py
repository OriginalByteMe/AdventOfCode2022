# Props to @hyper-neutrino for the all() function in python to check for iterable conditions

import re
from pprint import pprint 
def create_grid():
  f = open("grid.txt", "r")
  grid = []
  for line in f:
    digits = [int(x) for x in line.replace('\n', '')]
    grid.append(digits)
  
  pprint(grid)
  return grid

def count_visible():
  grid = create_grid()
  num_visible = 0
  
  # Count visible trees on edges
  # top and bottom row
  # num_visible += len(grid[0]) * 2
  # left and right column
  # num_visible += len(grid) * 2
  # print(grid[:2][3])
  # All items in the middle
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      current_tree = grid[i][j]
      # visible = False
      # up, down, left, right = [], [], [], []
      if all(grid[i][x] < current_tree for x in range(j)):
        num_visible += 1
        continue

      if all(grid[i][x] < current_tree for x in range(j + 1, len(grid[i]))):
        num_visible += 1
        continue

      if all(grid[x][j] < current_tree for x in range(i)):
        num_visible += 1
        continue
      
      if all(grid[x][j] < current_tree for x in range(i + 1, len(grid))):
        num_visible += 1
        continue
      
  return num_visible
      
  

def main():
  print(count_visible())
  pass

if __name__ == "__main__":
  main()