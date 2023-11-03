# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()

#Functions

def LinearSearch(array, item):
    for i in range(len(array)):
       if array[i] == item:
          return i 
    
    return -1

def BinarySearch(array,item):
  lowIndex = 0
  upperIndex = len(array) - 1
  while lowIndex <= upperIndex:
     midIndex = (upperIndex + lowIndex) // 2
     if item == array[midIndex]:
        return midIndex
     elif item < array[midIndex]:
        upperIndex = midIndex -1
     else:
        lowIndex = midIndex + 1

  return -1

import time
# Main Program Loop
loop = True
while loop:
  # Main Menu
  print("\n***MAIN MENU*** ")
  print("1. Spell Check a Word(Linear Search)")
  print("2. Spell check a Word(Binary Search)")
  print("3. Spell Check in Alice In Wonderland(Linear Search)")
  print("4. Spell Check in Alice in Wonerland(Binary Search)")
  print("5. Exit")
  

  # Get Menu Selection from User
  option = input("Enter Selection (1-6): \n")

  # Take Action Based on Menu Selection
  # Option 1

  if option == "1":
    #PRINT LIST
    print("Spell Check a Word(Linear Search)")
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    word = input("Please Enter a Word: ")
    startTime = time.time()
    index = LinearSearch(dictionary,word)
    endTime = time.time()
    if index == -1:
      print(f"{word} is NOT in Dictionary.({endTime - startTime}) seconds")
    else:
      print(f"{word} is IN the Dictionary at postition {LinearSearch(dictionary,word)}. ({endTime - startTime}) seconds")


  # Option 2
  elif option == "2":
    #ADD ITEM TO END
    print("Spell check a Word(Binary Search)")
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    word = input("Please Enter a Word: ")
    startTime = time.time()
    index = BinarySearch(dictionary, word)
    endTime = time.time()
    if index == -1:
      print(f"{word} is NOT in Dictionary. ({endTime - startTime}) seconds")
    else:
      print(f"{word} is IN the Dictionary at postition {BinarySearch(dictionary,word)}. ({endTime - startTime}) seconds")


  # Option 3
  elif option == "3":
    # REMOVE LAST ITEM
    print(" Spell Check in Alice In Wonderland(Linear Search)")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    dictionary = loadWordsFromFile("data-files/dictionary.txt") 
    countWord = 0

    startTime = time.time()  
    for word in aliceWords:
      index = LinearSearch(dictionary,word.lower())
      if index == -1:
        countWord = countWord + 1
    endTime = time.time()
    print(f"Number of words not found in dictionary: {countWord}. ({endTime - startTime}) seconds ")


  # Option 4
  elif option == "4":
    #INSERT AT POSITION
    print("Spell Check in Alice in Wonerland(Binary Search)")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    countWord = 0
    startTime = time.time()
    for word in aliceWords:
      index = BinarySearch(dictionary,word.lower())
      if index == -1:
        countWord = countWord + 1
    endTime = time.time()

    print(f"Number of words not found in dictionary: {countWord}. ({endTime - startTime}) seconds")

  # Option 5
  elif option == "8":
    print("EXIT")
    loop = False
