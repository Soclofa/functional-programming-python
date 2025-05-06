import random

#%%
#Question 1

# Define a function to check if three lengths can form a triangle
def is_triangle(a, b, c):
    # A triangle is valid if the sum of lengths of any two sides is greater than the length of the third side
    return a + b > c and a + c > b and b + c > a

# Get the lengths of the sides from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if the entered lengths can form a triangle using the is_triangle function
if is_triangle(a, b, c):
    # If they can form a triangle, print a success message
    print("They are correct triangle sides' lengths")
else:
    # If they can't form a triangle, print an error message
    print("They are in error")


# %%
    #
#  Question 2
#
import math
from myboolfuncs import *
#
# Area calculation program  
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return

def sphereVolume(r): 
    return 4/3 * math.pi * r**3

def coneVolume(r, h): 
    return 1/3 * math.pi * r**2 * h

def squarePyramidVolume(a, h):
    return 1/3 * a**2 * h

#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")  
# Print out the menu
shapes = ("Rectangle", "Circle", "Sphere", "Cone", "Square Pyramid")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes) 
    # Get the user's choice: 
    shape = input("> ")
    # Calculate the area: 
    if shape == "1":
         height = getNumber("Please enter the height: ")    
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":
        r = float(input("Enter the radius of the sphere: "))
        print("The volume of the sphere is", sphereVolume(r))
        continue
    elif shape == "4":
        r = float(input("Enter the radius of the cone: "))
        h = float(input("Enter the height of the cone: "))
        print("The volume of the cone is", coneVolume(r, h))
        continue
    elif shape == "5":
        a = float(input("Enter the base edge length of the square pyramid: "))
        h = float(input("Enter the height of the square pyramid: "))
        print("The volume of the square pyramid is", squarePyramidVolume(a, h))
        continue
    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")
#%%
         
# Question 3 Part A Version 1
         
numbers = []
while len(numbers) < 4:
    try:
        number = float(input("Enter a number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

numbers.sort()
print(numbers[1:3])

# %%

# Question 3 Part A Version 2
numbers = []
while len(numbers) < 4:
    try:
        number = float(input("Enter a number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

numbers.remove(max(numbers))
numbers.remove(min(numbers))

if numbers[0] > numbers[1]: 
    numbers.reverse()

print(numbers)


# %%

# Question 3 Part B Version 1






#%%

#Question 4

def shiftL(binNr, n): 
    return binNr[n:] + '0' * n

def shiftR(binNr, n): 
    return '0' * n + binNr[:-n]

def shiftCL(binNr, n): 
    return binNr[n:] + binNr[:n]

def shiftCR(binNr, n): 
    return binNr[-n:] + binNr[:-n]

### Needs Input 


# %%

#Question 5

def get_elements_from_tuples(lst):
    result = []
    for element in lst:
        if isinstance(element, tuple):
            result.extend(element)
    return result

def get_elements_from_lists(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(element)
    return tuple(result)

def get_numbers_not_nested(lst):
    result = []
    for element in lst:
        if isinstance(element, int) and not isinstance(element, str):
            result.append(element)
    return tuple(result)

def get_strings_not_nested(lst):
    result = []
    for element in lst:
        if isinstance(element, str):
            result.append(element)
    return result

input_list = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e']

elements_from_tuples = get_elements_from_tuples(input_list)
print(f"Elements from tuples: {elements_from_tuples}")

elements_from_lists = get_elements_from_lists(input_list)
print(f"Elements from lists: {elements_from_lists}")

strings_not_nested = get_strings_not_nested(input_list)
print(f"Strings not nested: {strings_not_nested}")

numbers_not_nested = get_numbers_not_nested(input_list)
print(f"Numbers not nested: {numbers_not_nested}")

# %%

#Question 7

import string

def count_words(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = line.split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    for word, count in word_counts.items():
        if (count > 20000):
            print(f"{word}: {count}")

filename = "shakespeare.txt"
count_words(filename)
# %%

#Question 8

import random

def create_tuple(N):
    return tuple(random.randint(1, 9) for _ in range(N))

def guessTest(random_tuple, guess):
    return tuple(guess[i] if guess[i] == random_tuple[i] else "X" for i in range(len(guess)))

N = int(input("Enter a number between 3 and 9: "))
random_tuple = create_tuple(N)
print(random_tuple)

guess = tuple(int(input(f"Enter guess number {i+1}: ")) for i in range(N))

correct_guesses = guessTest(random_tuple, guess)
print(f"Correctly guessed numbers in their correct positions: {correct_guesses}")






# %%
