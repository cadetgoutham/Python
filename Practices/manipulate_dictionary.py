"""
Dictionary Inversion and Key Extraction Utility

Description:
    A Python script that demonstrates fundamental dictionary operations:
    1. Printing an initial word-frequency style dictionary.
    2. Inverting the dictionary (swapping keys and values) using a dictionary comprehension.
    3. Accessing values from the inverted dictionary.
    4. Iterating through keys to print formatted pairs and collecting keys into a list.

Output Preview:
    Original Dictionary: {'the': 2, 'a': 645, 'c': 789}
    Inverted Dictionary: {2: 'the', 645: 'a', 789: 'c'}
    Value at key 2 in inverted dict: the
    the : 2
    a : 645
    c : 789
    List of original keys: ['the', 'a', 'c']

How to Run:
    Command Line / Terminal:
    $ python dict_manipulation.py
"""

def manipulate_dictionary():
    # Define the initial word count/frequency data
    word_counts = {'the': 2, 'a': 645, 'c': 789}
    print("Original Dictionary:", word_counts)
    
    # Invert the dictionary (swap keys and values) using a dictionary comprehension
    # Original -> key: value | Inverted -> value: key
    inverted_word_counts = {count: word for word, count in word_counts.items()}
    print("Inverted Dictionary:", inverted_word_counts)
    
    # Look up the original word using its count as the key in the inverted dictionary
    print("Value at key 2 in inverted dict:", inverted_word_counts[2])
    
    # Initialize an empty list to store the dictionary keys
    original_keys_list = []
    
    # Loop through the keys of the original dictionary
    for word in word_counts.keys():
        original_keys_list.append(word)
        print(f'{word} : {word_counts[word]}')

    # Print the final collected list of keys
    print("List of original keys:", original_keys_list)


if __name__ == "__main__":
    # Ensures the script runs automatically when executed directly,
    # but remains safe to import as a module elsewhere.
    manipulate_dictionary()