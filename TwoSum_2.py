def two_sum(nums, target):
    """
    Finds two numbers in a list that add up to a specific target.

    Args:
        nums (list): A list of integers (e.g., [7, 1, 5, 2, 4]).
        target (int): The target sum we want to reach (e.g., 9).

    Returns:
        list: A list containing the indices of the two numbers.
        None: If no pairs match the target.
    """
    # Initialize two pointers at the absolute ends of the sorted list
    left = 0
    right = len(nums) - 1

    # Keep narrowing the window until the pointers meet
    while left < right:
        # Calculate the sum of the elements at the current pointer positions
        total = nums[left] + nums[right]

        # Scenario 1: We found the exact target match
        if total == target:
            # Return 1-based indices by adding 1 to the 0-based Python indices
            return [left + 1, right + 1]

        # Scenario 2: The sum is too small
        # Because the list is sorted, moving the left pointer rightward increases the total
        elif total < target:
            left += 1

        # Scenario 3: The sum is too large
        # Moving the right pointer leftward decreases the total
        else:
            right -= 1
            
    # Return None if the pointers cross without finding a matching pair
    return None

if __name__ == "__main__":
    # --- Example Usage ---
    # The list MUST be sorted for this two-pointer logic to work.
    # The target is 9. 2 (index 1) and 7 (index 4) add up to 9.
    numbers_list = [1, 2, 4, 5, 7]
    target_sum = 9

    result = two_sum(numbers_list, target_sum)
    
    # Expected output: [2, 5] (due to the 1-based indexing conversion)
    print(f"Indices of the two numbers: {result}")