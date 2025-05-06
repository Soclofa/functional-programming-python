#%%
# Question9.py 

import Question1
import Question2
import Question3
import Question4
import Question5
import Question6
import Question7
import Question8


def menu():
    print("Select an option:")
    print("1: Check if a number is a palindrome")
    print("2: Calculate series sum")
    print("3: Approximate Pi")
    print("4: Add three dictionaries")
    print("5: Find twin primes")
    print("6: Function from Question6")
    print("7: Function from Question7")
    print("8: Function from Question8")
    print("0: Quit")

def main():
    options = {
        "1": Question1.main,
        "2": Question2.main,
        "3": Question3.main, 
        "4": Question4.main, 
        "5": Question5.main,
        "6": Question6.main, 
        "7": Question7.main, 
        "8": Question8.main, 
    }

    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice in options:
            result = options[choice]()
            print("Result:", result)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

# %%
