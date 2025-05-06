#%%
#Question5.py 

def build_values_list(n):
    return list(map(lambda i: i / (i + 1), range(1, n + 1)))

def m(n):
    values_list = build_values_list(n)
    return sum(values_list)

def print_series_non_tail(n):
    def helper(i):
        if i > n:
            return
        print(f"i: {i}, m(i): {m(i)}")
        helper(i + 1)
    
    helper(1)

def print_series_tail(n):
    def helper(i):
        if i > n:
            return
        print(f"i: {i}, m(i): {m(i)}")
        return helper(i + 1)
    
    return helper(1)

def main():
    n = int(input("Enter a natural number: "))
    print("Using non-tail recursion:")
    print_series_non_tail(n)
    print("\nUsing tail recursion:")
    print_series_tail(n)

if __name__ == "__main__":
    main()

# %%
