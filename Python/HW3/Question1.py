#%%

#Question1.py
def pentaNumRange_tail(n1, n2, acc=[]):
    getPentaNum = lambda n: n*(3*n - 1) // 2
    if n1 >= n2:
        return acc
    else:
        return pentaNumRange_tail(n1+1, n2, acc + [getPentaNum(n1)])

def pentaNumRange_nonTail(n1, n2):
    getPentaNum = lambda n: n*(3*n - 1) // 2
    if n1 >= n2:
        return []
    else:
        return [getPentaNum(n1)] + pentaNumRange_nonTail(n1+1, n2)

def main():
    n1 = int(input("Enter the first natural number (n1): "))
    n2 = int(input("Enter the second natural number (n2, n1 < n2): "))
    
    if n1 < n2:
        print(pentaNumRange_nonTail(n1,n2))
        print(pentaNumRange_tail(n1,n2))

    else:
        print("Error: n1 should be less than n2")


if __name__ == "__main__":
    main()
# %%
