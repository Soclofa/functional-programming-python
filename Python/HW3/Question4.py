#%%
#Question4.py 
def reverseNum(n):
    def helper(n, rev):
        if n == 0:
            return rev
        else:
            rev = rev * 10 + n % 10
            return helper(n // 10, rev)
    return helper(n, 0)

def isPalindrome(n):
    return n == reverseNum(n)

def reverseNumTail(n):
    def helper(n, rev):
        if n == 0:
            return rev
        return helper(n // 10, rev * 10 + n % 10)
    return helper(n, 0)

def isPalindromeTail(n):
    return n == reverseNumTail(n)

def main():
    n = int(input("Enter a natural number: "))
    if isPalindrome(n):
        print("It is a palindrome!!")
    else:
        print("It is not a palindrome")

    if isPalindromeTail(n):
        print("It is a palindrome (tail recursion)!")
    else:
        print("It is not a palindrome (tail recursion)")

if __name__ == "__main__":
    main()

# %%
