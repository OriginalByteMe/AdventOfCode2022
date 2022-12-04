
def get_overlap():
  f = open("input.txt", "r")
  for i, line in enumerate(f):
    group = line.split(",")
    first = group[0]
    second = group[1].replace('\n', '')
    print(second)
    


def main():
    # Your code here
    print(get_overlap())
    pass
  
if __name__ == "__main__":
    main()