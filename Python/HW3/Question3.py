#%%
#Question3.py
def reverseNum1(n):
    return int(str(n)[::-1])

def decompose_number(n):
    if n == 0:
        return []
    else:
        return decompose_number(n // 10) + [n % 10]

def reverseNum2(n):
    digits = decompose_number(n)
    reversed_digits = list(reversed(digits))
    reversed_number = 0
    for digit in reversed_digits:
        reversed_number = reversed_number * 10 + digit
    return reversed_number

def reverseNum_recursive(n):
    def helper(n, result):
        if n == 0:
            return result
        else:
            return helper(n // 10, result * 10 + n % 10)
    return helper(n, 0)

def reverseNum_tail_recursive(n):
    def helper(n, result):
        if n == 0:
            return result
        else:
            return helper(n // 10, result * 10 + n % 10)
    return helper(n, 0)

def main():
    n = int(input("Enter a natural number: "))
    print(f"reverseNum1({n}) = {reverseNum1(n)}")
    print(f"reverseNum2({n}) = {reverseNum2(n)}")
    print(f"reverseNum_recursive({n}) = {reverseNum_recursive(n)}")
    print(f"reverseNum_tail_recursive({n}) = {reverseNum_tail_recursive(n)}")

if __name__ == "__main__":
    main()
# %%
