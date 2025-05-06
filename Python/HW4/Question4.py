import random

# Global variables with lists of words
peopleNames = ["Iosi", "Ety", "Alex", "Jordan", "Sam"]
verbs = ["sees", "plays", "sings", "jumps", "runs"]
adjectives = ["tall", "small", "red", "black", "blue"]
adverbs = ["slowly", "tomorrow", "now", "soon", "suddenly"]
animateObjects = ["flowers", "oranges", "birds", "cats", "dogs"]
inanimateObjects = ["a stone", "a chair", "a book", "a car", "a phone"]

def random_choice(word_list):
    """Returns a random choice from the given list."""
    return random.choice(word_list)

def generate_sentence():
    """Generates a random syntactically correct English sentence."""
    return f"{random_choice(peopleNames)} {random_choice(verbs)} {random_choice(adverbs)} {random_choice(adjectives)} {random_choice(animateObjects) if random.random() > 0.5 else random_choice(inanimateObjects)}"

def crPoem(N):
    """Generates a list of N random syntactically correct English sentences."""
    return [generate_sentence() for _ in range(N)]

def theHumbletPoet(N):
    """Prints a random poem of N lines."""
    poem = crPoem(N)
    for line in poem:
        print(line)

def main():
    N = int(input("Enter the number of lines for the random poem: "))
    theHumbletPoet(N)

if __name__ == "__main__":
    main()
