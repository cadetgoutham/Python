"""
Similar String Cluster Counter

Description:
    A self-contained Python script that counts how many distinct groups of 
    "similar" strings exist within an array. Two strings are considered 
    similar if they are composed of the exact same set of unique characters, 
    ignoring duplicates and character order.

Output Preview:
    Input Array: ['good', 'god', 'bac', 'aabc']
    Number of unique similar groups: 2

How It Works:
    1. It iterates through the input array and converts each word into a 
       frozenset of its unique characters (e.g., 'good' -> frozenset({'g', 'o', 'd'})).
    2. A 'frozenset' is used because it is immutable and can be added to a Python set.
    3. By adding these character sets into a master tracking set, duplicate 
       character patterns collapse automatically.
    4. The total number of unique patterns represents the number of groups.

How to Run:
    $ python similar_strings.py
"""

def count_similar_string_groups(string_array):
    """
    Groups strings by their unique character sets and returns the 
    total number of distinct similar clusters.
    """
    unique_groups = set()

    for word in string_array:
        # 1. Normalize to lowercase
        normalized_word = word.lower()
        
        # 2. Extract only the unique characters as an immutable frozenset
        # Example: 'aabc' -> frozenset({'a', 'b', 'c'})
        character_set = frozenset(normalized_word)
        
        # 3. Add to our master set tracking unique character combinations
        unique_groups.add(character_set)

    # The size of the master set tells us how many distinct clusters exist
    return len(unique_groups)


def main():
    # Test dataset
    sample_strings = ['good', 'god', 'bac', 'aabc']
    print("Input Array:", sample_strings)
    
    # Calculate group count
    total_groups = count_similar_string_groups(sample_strings)
    
    print("Number of unique similar groups:", total_groups)


if __name__ == "__main__":
    # Standard script execution hook
    main()