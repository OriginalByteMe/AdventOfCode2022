
def get_complete_overlap():
  f = open("input.txt", "r")
  num_fully_contained = 0
  for i, line in enumerate(f):
    group = line.split(",")
    first = [int(x) for x in group[0].split("-")]
    second = [int(x) for x in group[1].replace('\n', '').split("-")]
    first_range = range(first[0], first[1] + 1) # +1 because range is exclusive
    second_range = range(second[0], second[1] + 1)
    
    if set(first_range).issubset(second_range) or set(second_range).issubset(first_range):
      num_fully_contained += 1
    
  return num_fully_contained

def get_overlap():
  f = open("input.txt", "r")
  num_overlapped = 0
  for i, line in enumerate(f):
    group = line.split(",")
    first = [int(x) for x in group[0].split("-")]
    second = [int(x) for x in group[1].replace('\n', '').split("-")]
    first_range = range(first[0], first[1] + 1) # +1 because range is exclusive
    second_range = range(second[0], second[1] + 1)
    
    if len(set(first_range).intersection(second_range)) > 0:
      num_overlapped += 1
    
  return num_overlapped  


def main():
    # Your code here
    print("Fully contained", get_complete_overlap())
    print("Overlapped", get_overlap())
    pass
  
if __name__ == "__main__":
    main()