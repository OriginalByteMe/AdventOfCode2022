def stack_mover():
  f = open("input.txt", "r")
  # create 9 stacks from the first 8 lines of the input file
  stack_1 = ['R', 'P', 'C', 'D', 'B', 'G']
  stack_2 = ['H', 'V', 'G']
  stack_3 = ['N', 'S', 'Q', 'D', 'J', 'P', 'M']
  stack_4 = ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M']
  stack_5 = ['J', 'B', 'N', 'C', 'P', 'F','L','S']
  stack_6 = ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S']
  stack_7 = ['B', 'Z','M', 'H', 'F', 'T', 'Q']
  stack_8 = ['C', 'M', 'D','B', 'F']
  stack_9 = ['F','C','Q','G']
  
  stack_dict = {1: stack_1, 2: stack_2, 3: stack_3, 4: stack_4, 5: stack_5, 6: stack_6, 7: stack_7, 8: stack_8, 9: stack_9}
  
  for i, line in enumerate(f):
    if i > 9:
      numbers = []
      for t in line.split():
        try:
          numbers.append(int(t))
        except ValueError:
          pass
      num_move = numbers[0]
      crate_origin_num = numbers[1]
      crate_target_num = numbers[2]
      
      # move the crate from the origin stack to the target stack
      for j in range(num_move):
        crate = stack_dict[crate_origin_num].pop()
        stack_dict[crate_target_num].append(crate)
  top_crates = []
  # get the top crates from each stack
  for i in range(9):
    top_crates.append(stack_dict[i+1][-1])
  
  # print("Task 1", stack_dict)
  return top_crates

def crateMover_9001():
  f = open("input.txt", "r")
  # create 9 stacks from the first 8 lines of the input file
  stack_1 = ['R', 'P', 'C', 'D', 'B', 'G']
  stack_2 = ['H', 'V', 'G']
  stack_3 = ['N', 'S', 'Q', 'D', 'J', 'P', 'M']
  stack_4 = ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M']
  stack_5 = ['J', 'B', 'N', 'C', 'P', 'F','L','S']
  stack_6 = ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S']
  stack_7 = ['B', 'Z','M', 'H', 'F', 'T', 'Q']
  stack_8 = ['C', 'M', 'D','B', 'F']
  stack_9 = ['F','C','Q','G']
  
  stack_dict = {1: stack_1, 2: stack_2, 3: stack_3, 4: stack_4, 5: stack_5, 6: stack_6, 7: stack_7, 8: stack_8, 9: stack_9}
  for i, line in enumerate(f):
    if i > 9:
      numbers = []
      for t in line.split():
        try:
          numbers.append(int(t))
        except ValueError:
          pass
      num_move = numbers[0]
      crate_origin_num = numbers[1]
      crate_target_num = numbers[2]
      items_to_move = stack_dict[crate_origin_num][-num_move:]
      del stack_dict[crate_origin_num][-num_move:]
      stack_dict[crate_target_num] += items_to_move

  top_crates = []
  # get the top crates from each stack
  for i in range(9):
    top_crates.append(stack_dict[i+1][-1])
    
  return top_crates

def main():
  
  print("Task 1",stack_mover())
  print("Task 2",crateMover_9001())
  crateMover_9001()
  pass


if __name__ == "__main__":
  main()