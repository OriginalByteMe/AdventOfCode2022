def isUniqueChars(st):
 
    # String length cannot be more than
    # 256.
    if len(st) > 256:
        return False
 
    # Initialize occurrences of all characters
    char_set = [False] * 128
 
    # For every character, check if it exists
    # in char_set
    for i in range(0, len(st)):
 
        # Find ASCII value and check if it
        # exists in set.
        val = ord(st[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True

def find_start_of_packet_4_chars():
  packet = open("input.txt", "r")
  
  for line in packet:
    packet_start = ""
    for char in line:
      if (len(packet_start) > 3):
        packet_start = packet_start[1:]
      packet_start += char
      
      if (len(packet_start) == 4 and isUniqueChars(packet_start)):
        print(packet_start)
        num_count = line.find(packet_start)
        # +4 to account for the length of the packet_start
        return num_count + 4

def find_start_of_packet_14_chars():
  packet = open("input.txt", "r")
  
  for line in packet:
    packet_start = ""
    for char in line:
      if (len(packet_start) > 13):
        packet_start = packet_start[1:]
      packet_start += char
      
      if (len(packet_start) == 14 and isUniqueChars(packet_start)):
        print(packet_start)
        num_count = line.find(packet_start)
        # +4 to account for the length of the packet_start
        return num_count + 14


def main():
  print("Num chars till start (4): ",find_start_of_packet_4_chars())
  print("Num chars till start (14): ",find_start_of_packet_14_chars())
  pass

if __name__ == "__main__":
  main()