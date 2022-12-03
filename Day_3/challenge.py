from string import ascii_lowercase
from string import ascii_uppercase
from collections import Counter 

def assign_priority(upper, lower):
  for i in range(26):
    lower_letter = {
      "letter": ascii_lowercase[i],
      "priority": i + 1
    }
    upper_letter = {
      "letter": ascii_uppercase[i],
      "priority": i + 27
    }
    lower.append(lower_letter)
    upper.append(upper_letter)

def get_upper_priority(upper, letter):
  return upper[ascii_uppercase.index(letter)]["priority"]

def get_lower_priority(lower, letter):
  return lower[ascii_lowercase.index(letter)]["priority"]

def sort_priority(upper, lower):
  f = open("input.txt", "r")
  total_priorities = 0
  for line in f:
    compartment_size = len(line) // 2
    compartment_1 = list(set(line[:compartment_size]))
    compartment_2 = list(set(line[compartment_size:]))
    
    for i in range(len(compartment_1)):
      if compartment_1[i] in compartment_2:
        if compartment_1[i].islower():
          total_priorities += get_lower_priority(lower, compartment_1[i])
        else:
          total_priorities += get_upper_priority(upper, compartment_1[i])
  f.close()
  return total_priorities

def get_unique_only(set1):
  set1.discard("\n")
  print("Set1 = ", set1)
  string = str(set1)
  string = string.translate( {ord(c): None for c in "{',} " } )
  return string


      

def group_badge_priority(upper, lower):
  f = open("input.txt", "r")
  
  # Find badge every 3 lines
  line_count = 0
  with open("input.txt") as f:
    badge_group = []
    total_priorities = 0
    for i, line in enumerate(f):
      badge_group.append(line)
      if (i + 1) % 3 == 0:
        for i in range(len(badge_group)):
          badge_group[i] = badge_group[i].replace("\n", "")
          
        print("Group: ", badge_group)
        for i in badge_group[0]:
          if i in badge_group[1] and i in badge_group[2]:
            if i.islower():
              total_priorities += get_lower_priority(lower, i)
              break
            else:
              total_priorities += get_upper_priority(upper, i)
              break
        
        # if most_common[0][0].islower():
        #   total_priorities += get_lower_priority(lower, most_common[0][0])
        # else:
        #   total_priorities += get_upper_priority(upper, most_common[0][0])
        badge_group = []
  f.close()
  return total_priorities


def main():
  upper_priority = []
  lower_priority = []
  assign_priority(upper_priority, lower_priority)
  
  print(sort_priority(upper_priority, lower_priority))
  print(group_badge_priority(upper_priority, lower_priority))
    

if __name__ == "__main__":
    main()