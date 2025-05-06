#%%
#Question7.py 

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def twinp(n):
    primes = sieve(n)
    twin_primes = {p: p+2 for p in primes if p+2 in primes}
    return twin_primes

def print_twin_primes_non_tail(twin_primes):
    keys = list(twin_primes.keys())
    
    def helper(index):
        if index >= len(keys):
            return
        p = keys[index]
        print(f"({p}, {twin_primes[p]})")
        helper(index + 1)
    
    helper(0)

def print_twin_primes_tail(twin_primes):
    keys = list(twin_primes.keys())
    
    def helper(index):
        if index >= len(keys):
            return
        p = keys[index]
        print(f"({p}, {twin_primes[p]})")
        return helper(index + 1)
    
    return helper(0)

def main():
    n = int(input("Enter a natural number: "))
    twin_primes = twinp(n)
    print("Twin primes using non-tail recursion:")
    print_twin_primes_non_tail(twin_primes)
    print("\nTwin primes using tail recursion:")
    print_twin_primes_tail(twin_primes)

if __name__ == "__main__":
    main()

# %%
