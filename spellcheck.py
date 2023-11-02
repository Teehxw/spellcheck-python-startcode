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
    if LinearSearch(dictionary,word)== -1:
      print(f"{word} is NOT in Dictionary")
    else:
      print(f"{word} is IN the Dictionary at postition {LinearSearch(dictionary,word)}")


  # Option 2
  elif option == "2":
    #ADD ITEM TO END
    print("Spell check a Word(Binary Search)")
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    word = input("Please Enter a Word: ")
    
    index = BinarySearch(dictionary, word)
    
    if index == -1:
      print(f"{word} is NOT in Dictionary")
    else:
      print(f"{word} is IN the Dictionary at postition {BinarySearch(dictionary,word)}")


  # Option 3
  elif option == "3":
    # REMOVE LAST ITEM
    print(" Spell Check in Alice In Wonderland(Linear Search)")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    word = input("Please Enter a Word: ")
    if LinearSearch(aliceWords,word)== -1:
      print(f"{word} is NOT in Dictionary")
    else:
      print(f"{word} is IN the Dictionary at postition {LinearSearch(aliceWords,word)}")


  # Option 4
  elif option == "4":
    #INSERT AT POSITION
    print("Spell Check in Alice in Wonerland(Binary Search)")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    word = input("Please Enter a Word: ")
    if BinarySearch(aliceWords,word)== -1:
      print(f"{word} is NOT in Dictionary")
    else:
      print(f"{word} is IN the Dictionary at postition {BinarySearch(aliceWords,word)}")

  # Option 5
  elif option == "8":
    print("EXIT")
    loop = False

# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
#startTime = time.time()
#insertionSort(randomData)

#endTime = time.time()
#print(f"Insertion Sort Random Data: {endTime - startTime} seconds")