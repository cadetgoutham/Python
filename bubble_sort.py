"""
Bubble Sort Optimization (Descending Order)

Description:
    A robust Python script implementing the Bubble Sort algorithm to rearrange 
    an array of integers in descending order (highest to lowest). It uses a 
    standard __main__ entry point and self-contained documentation.

Output Preview:
    Before sorting: [1, 20, 22, 0, 4, 77, 13, 200, 8]
    After sorting:  [200, 77, 22, 20, 13, 8, 4, 1, 0]

How It Works:
    1. Outer Loop: Tracks the pass number. For an array of size N, it runs 
       N - 1 times to guarantee every element settles into position.
    2. Inner Loop: Compares adjacent indices (j and j + 1). By subtracting the 
       pass index (i), it prevents comparing already-sorted elements at the 
       tail end of the list, improving efficiency.
    3. Element Swap: Uses Python's tuple unpacking to swap values instantly 
       if the left element is strictly less than the right element.

How to Run:
    Command Line / Terminal:
    $ python bubble_sort.py
"""

def bubble_sort(array):
    """
    Sorts an array in-place in descending order using the Bubble Sort algorithm.
    """
    array_length = len(array)
    
    # Outer loop dictates how many passes we make through the array
    for pass_index in range(array_length - 1):
        
        # Inner loop performs adjacent comparisons.
        # 'array_length - 1 - pass_index' optimizes the check by skipping 
        # the elements that have already bubbled down to the end.
        for element_index in range(array_length - 1 - pass_index):
            
            # Swap if the current element is less than the next element
            if array[element_index] < array[element_index + 1]:
                array[element_index], array[element_index + 1] = (
                    array[element_index + 1], array[element_index]
                )


if __name__ == "__main__":
    # Test array to demonstrate the sorting process
    sample_array = [1, 20, 22, 0, 4, 77, 13, 200, 8]

    print("Before sorting:", sample_array)

    bubble_sort(sample_array)

    print("After sorting: ", sample_array)