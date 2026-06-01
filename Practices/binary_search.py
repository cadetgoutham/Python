"""
Binary Search Algorithm Implementation

Description:
    A self-contained Python script implementing a Binary Search algorithm 
    to efficiently locate a target integer within a pre-sorted list.

Output Preview:
    enter the number: 60
    key is present  60

How It Works:
    1. It establishes two pointers: 'low_index' at the start (0) and 'high_index' at the end (len - 1).
    2. In each iteration, it calculates the midpoint ('mid_index').
    3. If the target matches the midpoint value, the search succeeds and breaks out.
    4. If the target is larger than the midpoint value, the lower half is discarded by moving 'low_index'.
    5. If the target is smaller, the upper half is discarded by moving 'high_index'.
    6. This divide-and-conquer strategy cuts the search space in half each time ($O(\log n)$ complexity).

How to Run:
    Command Line / Terminal:
    $ python binary_search.py
"""

def perform_binary_search():
    # Pre-sorted list required for binary search to function correctly
    sorted_numbers = [10, 20, 30, 40, 50, 60, 70, 80]
    
    low_index = 0
    high_index = len(sorted_numbers) - 1
    
    try:
        target_key = int(input('enter the number: '))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Loop runs as long as the search space contains elements
    while low_index <= high_index:
        # Calculate the middle index using floor division
        mid_index = (low_index + high_index) // 2
        
        # Check if the target is found at the midpoint
        if target_key == sorted_numbers[mid_index]:
            print('key is present ', target_key)
            break
        # If target is larger, shift the lower bound past the midpoint
        elif target_key > sorted_numbers[mid_index]:
            low_index = mid_index + 1
        # If target is smaller, shift the upper bound below the midpoint
        else:
            high_index = mid_index - 1
    else:
        # Executes only if the while loop completes naturally without hitting 'break'
        print('number is not present')


if __name__ == "__main__":
    # Ensures the search function runs automatically when executed directly
    perform_binary_search()