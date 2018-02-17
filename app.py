class color:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

list = ["Clean the house", "Play WoW", "Go to Work"]

def print_list(x):
  print(color.BOLD + color.UNDERLINE + "To Do List" + color.END)
  for items in x:
    print(color.BLUE + items + color.END)

# Creates function for 
def listandask():
  new_item = input("Add a new item to the to do list: ")
  if len(new_item) is 0:
    print("Please enter an item!")
    listandask()
  elif len(new_item) < 3:
    print("Please enter valid words!")
    listandask()
  else:    
    list.append(new_item)
    print("\n")
    print_list(list)
    startapp()
  
def startapp():
	listandask()  

print_list(list)
startapp()