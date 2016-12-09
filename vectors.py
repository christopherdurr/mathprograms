from math import sqrt

def helpMenu() -> None:
  """Display available commands to the user"""
  helpDisplay = """ 
Here are the following commands you can use in the program:
  
* setvector vectorName num1 num2 num3 ...
  
setvector takes a vector name and any amount of numbers
  
EXAMPLE:
setvector x 3 5 1 
creates a vector x = [3, 5, 1]

* showvectors (all) (vector1) (vector2)...

arguments are either all or an arbitrary number of vectors
If argument given is all, all vectors defined will be shown. If specfic vectors are given as argument, then only those vectors will be displayed
  
* addvectors vector1 vector2 vector3 ...
You may use as many vectors as you wish for addvectors. addvectors will add all given vectors together into one vector
NOTE: STILL HASN'T BEEN PROPERLY IMPLEMENTED YET.

EXAMPLE:
addvectors x y 
Let's assume x = [1, 5] and y = [2, -3]
The program will display [3, 2]

  
* length vector 
Takes a single vector as an argument and gives the length of the vector.

EXAMPLE:
length x
assume x = [3, 4, 0]
this will display length: 5
  
* stop
This will stop the program entirely

* debugMode T/F
Will set debugMode on or off for developers. 

EXAMPLE:

debugMode T
Turns on debug mode
debugMode F
Turns off debug mode
  """
  print(helpDisplay)
def vectorAlreadyExists(vectorName) -> bool:
  """Checks to see if a given vector already exists"""
  vectorExists = False
  for name in vectors.keys():
    if vectorName == name:
      vectorExists = True
  return vectorExists
  
def setvector(arguments) -> None:
  """Sets a vector with a variable name and values"""
  vectorName = arguments[0]
  if vectorAlreadyExists(vectorName):
    print("Vector", vectorName, "already exists! Are you sure you wish to overwrite it? y/n")
    userInput = input().lower()
    if userInput == 'n' or userInput == 'no':
      print("Keeping original vector")
      return
    elif userInput == 'y' or userInput == 'yes':
      print("Overwriting vector", vectorName)
  values = arguments[1:]
  values = list(map(int, values))
  vectors[vectorName] = values
  print("vector", vectorName, "set")
  return

def displayVectors(arguments) -> None:
  if arguments[0] == 'all':
    for vectorName, values in vectors.items():
      print(vectorName, "=")
      print(values)
  else:
    for vectorName in arguments:
        print(vectorName, "=")
        print(vectors[vectorName])
  return

def sameSize(arguments) -> bool:
  """Checks whether given vectors are the same size or not"""
  sameLength = True
  initialSize = len(vectors[arguments[0]])
  for vector in arguments:
    if len(vectors[vector]) != initialSize:
      sameLength = False
  return sameLength
    
def lengthVector(arguments) -> None:
  """Calculates the length of a vector"""
  length = 0
  for vector in arguments:
    for element in vectors[vector]:
      length += element**2
    length = sqrt(length)
  return round(length,3)
  
def sizeVector(arguments) -> None:
  """Displays in what dimension a vector is in"""
  for vector in arguments:
    vectorSize = len(vectors[vector])
    print(vector, "is in R^"+str(vectorSize))
  return
      
def addVectors(arguments) -> None:
  if sameSize(arguments):
    print("adding vectors")
    #ADD CODE TO ADD VECTORS HERE
  else:
    print("Can't add given vectors. They're not of equal length.")
  return


vectors = {}
def runProgram() -> None:
  continueProgram = True
  debugMode = False
  while continueProgram:
    print()
    print("What would you like to do?")
    print()
    text = input("")
    text = text.lower().split()
    command = text[0]
    arguments = text[1:]
    if debugMode:
      print("command:", command)
      print("arguments:", arguments)
    print()
    if command == 'help':
      helpMenu()
    if command == 'setvector':
      setvector(arguments)
    if (command == 'showvectors'):
      displayVectors(arguments)
    if (command == 'show'):
      displayVectors(arguments)
    if (command == 'addvectors') or (command == 'add'):
      addVectors(arguments)
    if command == 'length':
      print("Length:", lengthVector(arguments))
    if command == 'size':
      sizeVector(arguments)
    if command == 'stop':
      continueProgram = False
    if command == 'debugmode':
      if arguments[0] == 't' or  arguments[0] == 'true':
        debugMode = True
      elif arguments[0] == 'f' or arguments[0] == 'false':
        debugMode = False
      else:
        print("Can't understand argument given")
    else:
      print("That command doesn't exist!")
  
    
  
print("Welcome to the vector program!\nEnter 'help' for commands\nEnter 'about' for information about the program itself")

runProgram()
print("Thank you for using the program!")
  
