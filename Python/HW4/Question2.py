#%%
import re

def treatline(lineNr, line):
    def is_letter(word):
        return all(char.isalpha() for char in word)
    
    def classify_characters(word):
        vowels = [char for char in word if char in 'aeiouAEIOU']
        b_m_consonants = [char for char in word if char in 'bcdefghijklmBCDEFGHIJKLM']
        n_z_consonants = [char for char in word if char in 'npqrstuvwxyzNPQRSTUVWXYZ']
        return vowels, b_m_consonants, n_z_consonants
    
    words = re.findall(r'\b\w+\b', line)
    
    if any(not is_letter(word) for word in words):
        return -1
    
    result = {word: classify_characters(word) for word in words}
    return lineNr, result

def treatxtfile(flname):
    with open(flname, 'r') as file:
        lines = file.readlines()
    
    processed_lines = map(lambda x: treatline(x[0] + 1, x[1]), enumerate(lines))
    valid_lines = filter(lambda x: x != -1, processed_lines)
    return dict(valid_lines)

def occursumary(fldict):
    def count_occurrences(line_data):
        vowels = sum(len(details[0]) for details in line_data.values())
        b_m_consonants = sum(len(details[1]) for details in line_data.values())
        n_z_consonants = sum(len(details[2]) for details in line_data.values())
        return vowels, b_m_consonants, n_z_consonants

    return {lineNr: count_occurrences(data) for lineNr, data in fldict.items()}

def main():
    import os

    flname = input("Enter the name (or full pathname) of a text file: ").strip()
    if not os.path.isfile(flname):
        print(f"File '{flname}' not found.")
        return

    fldict = treatxtfile(flname)
    summary_dict = occursumary(fldict)

    print(f"{'LineNr':^10} {'nr of vowels':^15} {'nr of b-m consonants':^25} {'nr of n-z consonants':^25}")
    total_vowels = total_b_m = total_n_z = 0

    for lineNr, counts in summary_dict.items():
        vowels, b_m_consonants, n_z_consonants = counts
        print(f"{lineNr:^10} {vowels:^15} {b_m_consonants:^25} {n_z_consonants:^25}")
        total_vowels += vowels
        total_b_m += b_m_consonants
        total_n_z += n_z_consonants

    print(f"{'Nr of Lines in text':^20} {'total nr of vowels':^20} {'total nr of b-m consonants':^30} {'total nr of n-z consonants':^30}")
    print(f"{len(summary_dict):^20} {total_vowels:^20} {total_b_m:^30} {total_n_z:^30}")

if __name__ == "__main__":
    main()
