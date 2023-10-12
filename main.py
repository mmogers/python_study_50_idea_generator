import os, time, random

def myInputPrint(text):  #prints user input text with green clolor 
  result = input(f"{text} \033[32m")
  print("\033[0m", end="")
  return result

def addIdea():
  idea = myInputPrint("Input your idea. > ").capitalize()
  if len(idea) == 0 : #empty list
    print("You didn't input anything.")
    time.sleep(1)
    os.system("clear")
    return
  else: 
    f = open("my.ideas" , "a+")
    f.write(f"{idea}\n")
    f.close()
    print("\nAdded")
    time.sleep(1)
    os.system("clear")
    return

def randomIdea():
  f = open("my.ideas" , "r")
  ideas = f.readlines() 
  if len(ideas) == 0: #the empty file
    print("You have no ideas.")
    time.sleep(2)
    os.system("clear")
    return
  f.close()
  index = random.randint(0 , len(ideas) - 1)
  print(f"\n{ideas[index]}")
  time.sleep(3)
  os.system("clear")
  return
    

while True: 
  os.system("clear")
  print("\033[1;32mIDEAS\033[0m\n")
  choice = int(myInputPrint("1 : Add an idea\n2 : Load up a random idea\n> "))
  if choice == 1:
    addIdea()
  elif choice == 2:
    randomIdea()
  else: 
    print("Wrong input, try again!")
    time.sleep(2)
    continue