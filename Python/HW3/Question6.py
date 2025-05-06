#%%
#Question6.py 

def pi_non_tail(n):
    def helper(i):
        if i > n:
            return 0
        return ((-1) ** (i + 1)) / (2 * i - 1) + helper(i + 1)
    
    return 4 * helper(1)

def pi_tail(n):
    def helper(i, acc):
        if i > n:
            return acc
        return helper(i + 1, acc + ((-1) ** (i + 1)) / (2 * i - 1))
    
    return 4 * helper(1, 0)

def main():
    n = int(input("Enter a natural number: "))
    print(f"Approximation of pi using non-tail recursion with {n} terms: {pi_non_tail(n)}")
    print(f"Approximation of pi using tail recursion with {n} terms: {pi_tail(n)}")

if __name__ == "__main__":
    main()




