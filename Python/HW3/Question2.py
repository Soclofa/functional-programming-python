#%%
#Question2.py 
def sumDigits1_recursive(n):
    def decompose_number_recursive(n):
        if n == 0:
            return []
        else:
            return decompose_number_recursive(n // 10) + [n % 10]
    
    digits = decompose_number_recursive(n)
    return sum(digits)

def sumDigits2_recursive(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits2_recursive(n // 10)

def sumDigits1_tail_recursive(n):
    def decompose_number_tail_recursive(n, acc):
        if n == 0:
            return acc
        else:
            return decompose_number_tail_recursive(n // 10, [n % 10] + acc)
    
    digits = decompose_number_tail_recursive(n, [])
    return sum(digits)

def sumDigits2_tail_recursive(n):
    def helper(n, acc):
        if n == 0:
            return acc
        else:
            return helper(n // 10, acc + (n % 10))
    
    return helper(n, 0)


def main():
    n = int(input("Enter a natural number: "))
    print(f"sumDigits1_recursive({n}) = {sumDigits1_recursive(n)}")
    print(f"sumDigits2_recursive({n}) = {sumDigits2_recursive(n)}")
    print(f"sumDigits1_tail_recursive({n}) = {sumDigits1_tail_recursive(n)}")
    print(f"sumDigits2_tail_recursive({n}) = {sumDigits2_tail_recursive(n)}")


if __name__ == "__main__":
    main()
# %%
