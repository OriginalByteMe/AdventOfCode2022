# Credits to @sweemeng for the class structure idea with tree traversal
# Credits to @geethek for the idea of using a counter to store the size of the directories as well as the path library

import re
from pprint import pprint as print
from pathlib import Path
from collections import Counter
import copy

class Terminal:
  def __init__(self):
    self.cwd = Path('/')
    self.terminal_size = Counter()
  
  def cd(self, path):
    # CD will be responsible not only for menouvering between directories, but also for storing the directories in the terminal
    if path == "..":
      self.cwd = self.cwd.parent
    else: 
      self.cwd = self.cwd/path
    
  
  def ls(self, dirValue):
    # LS will be responsible for storing the files in the terminal, as well as the size of the files
    self.terminal_size[self.cwd] += int(dirValue)
    for key in self.cwd.parents:
      self.terminal_size[key] += int(dirValue)
  
  def parse(self, line):
    grouping = line.strip('\n').split()
    terminal = self.terminal_size
    dir = self.cwd
    if "$" in line:
      if grouping[1] == "cd":
        self.cd(grouping[2])
        
    elif grouping[0] != "dir":
      terminal[dir] += int(grouping[0])
      for x in dir.parents:
        terminal[x] += int(grouping[0])

def map_files():
  f = open("input.txt", "r")
  terminal = Terminal()
  for line in f:
    terminal.parse(line)
  return terminal.terminal_size

def main():
  terminal = map_files()
  terminal = sorted(terminal.values())

  sum_challenge_1 = 0
  sum_challenge_2 = 0
  space_for_update = 30000000 - (70000000 - terminal[-1])
  for i in terminal:
    # Challenge 1
    if i <= 100000:
      sum_challenge_1 += i
  
  # Challenge 2
  for j in terminal:
    if j <= space_for_update:
      continue
    else:
      sum_challenge_2 = j
      break
  
  
  
  # Challenge 2
  print(sum_challenge_1)
  print(sum_challenge_2)

  pass

if __name__ == "__main__":
  main()