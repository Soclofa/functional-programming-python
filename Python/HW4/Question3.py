def sortedzip(L):
    """Sort each sublist in ascending order and zip them together."""
    sorted_lists = [sorted(sublist) for sublist in L]
    return list(zip(*sorted_lists))

def reversedzip(L):
    """Reverse each sublist and zip them together."""
    reversed_lists = [list(reversed(sublist)) for sublist in L]
    return list(zip(*reversed_lists))

def funczip(func, L):
    """Apply the provided function to the list of lists."""
    return func(L)

def unzippy(L):
    """Unzip a list of tuples into a list of lists."""
    return [list(t) for t in zip(*L)]

def main():
    # User input for the list of lists
    N = int(input("Enter the number of sublists: "))
    L = []
    for i in range(N):
        sublist = input(f"Enter elements of sublist {i+1} separated by spaces: ").split()
        L.append(sublist)

    # Menu options
    options = {
        1: sortedzip,
        2: reversedzip
    }

    print("Choose an option:")
    print("1. Apply sortedzip")
    print("2. Apply reversedzip")

    choice = int(input("Enter the number of your choice: "))

    if choice in options:
        func = options[choice]
        result = funczip(func, L)
        print("Result of funczip:")
        print(result)
        unzipped_result = unzippy(result)
        print("Result of unzippy:")
        print(unzipped_result)
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
