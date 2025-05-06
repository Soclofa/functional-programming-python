#%%
#Question8.py 

shared_keys = lambda d1, d2, d3: set(d1.keys()) & set(d2.keys()) & set(d3.keys())
non_shared_keys = lambda d1, d2, d3: (set(d1.keys()) | set(d2.keys()) | set(d3.keys())) - shared_keys(d1, d2, d3)

def add3dicts_non_tail(d1, d2, d3):
    def combine_values(v1, v2, v3):
        return tuple(set([v1, v2, v3]))
    
    result = {}
    shared = shared_keys(d1, d2, d3)
    non_shared = non_shared_keys(d1, d2, d3)

    def add_shared_keys(keys):
        if not keys:
            return
        key = keys[0]
        result[key] = combine_values(d1[key], d2[key], d3[key])
        add_shared_keys(keys[1:])

    def add_non_shared_keys(keys):
        if not keys:
            return
        key = keys[0]
        if key in d1:
            result[key] = d1[key]
        elif key in d2:
            result[key] = d2[key]
        else:
            result[key] = d3[key]
        add_non_shared_keys(keys[1:])

    add_shared_keys(list(shared))
    add_non_shared_keys(list(non_shared))
    return result

def add3dicts_tail(d1, d2, d3):
    def combine_values(v1, v2, v3):
        return tuple(set([v1, v2, v3]))
    
    result = {}
    shared = shared_keys(d1, d2, d3)
    non_shared = non_shared_keys(d1, d2, d3)

    def add_shared_keys(keys, acc):
        if not keys:
            return acc
        key = keys[0]
        acc[key] = combine_values(d1[key], d2[key], d3[key])
        return add_shared_keys(keys[1:], acc)

    def add_non_shared_keys(keys, acc):
        if not keys:
            return acc
        key = keys[0]
        if key in d1:
            acc[key] = d1[key]
        elif key in d2:
            acc[key] = d2[key]
        else:
            acc[key] = d3[key]
        return add_non_shared_keys(keys[1:], acc)

    result = add_shared_keys(list(shared), result)
    result = add_non_shared_keys(list(non_shared), result)
    return result

def main():
    import ast

    d1 = ast.literal_eval(input("Enter the first dictionary: "))
    d2 = ast.literal_eval(input("Enter the second dictionary: "))
    d3 = ast.literal_eval(input("Enter the third dictionary: "))

    print("Result using non-tail recursion:")
    print(add3dicts_non_tail(d1, d2, d3))

    print("\nResult using tail recursion:")
    print(add3dicts_tail(d1, d2, d3))

if __name__ == "__main__":
    main()




