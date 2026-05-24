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
    # Dictionary to keep track of numbers we've already checked.
    # Key: The number itself, Value: Its index in the list.
    seen = {}

    # Loop through the list, getting both the index (i) and the value (num)
    for i, num in enumerate(nums):
        # Calculate what number we need to reach the target sum
        diff = target - num

        # Check if that required number is already in our dictionary
        if diff in seen:
            # If found, return the index of the required number and current index
            return [seen[diff], i]

        # If not found, store the current number and its index for future lookups
        seen[num] = i

    # Return None if no pair is found after checking the entire list
    return None

if __name__ == "__main__":
    # --- Example Usage ---
    # The target is 9. In this list, 7 (index 0) and 2 (index 3) add up to 9.
    numbers_list = [7, 1, 5, 2, 4]
    target_sum = 9

    result = two_sum(numbers_list, target_sum)
    print(f"Indices of the two numbers: {result}")