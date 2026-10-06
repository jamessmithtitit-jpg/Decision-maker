string = input("string:")
sub_string = input("sub_string:")
first = sub_string[0] # First string to check from where we gotta check the string
state : list[str] = [] # Makes a list to append 
# absolute code ends 
# dynamic code starts 
while True: 
  try:
    #print(string)
    index = string.index(first) # matching the first char with the whole string to start check 
    word_check = string[index:index + len(sub_string)] # making a word to check with the substring do they match or not 
    #print(index) # Printing to check whether our assumption is right 
    if word_check == sub_string: # Using the word now to check whether the thing is right or not 
      #print("True")
      state.append("True")
      #print("flase")
   # """Now after doing the first check now the string = string[index + 1 : len(string)]"""
    string = string[index + 1 : len(string)]
  except ValueError:
    print(len(state))
    break 
