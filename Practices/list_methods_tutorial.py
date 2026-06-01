"""
Comprehensive Python List Methods Tutorial

Description:
    An interactive, educational script demonstrating every primary built-in 
    list method in Python. It provides clear, real-world examples of how to 
    mutate, inspect, and organize data arrays.

Output Preview:
    --- 1. Adding Elements ---
    Initial List: ['Apple', 'Banana']
    After .append(): ['Apple', 'Banana', 'Cherry']
    ...

How It Works:
    The script runs through isolated blocks representing:
    1. Creation & Addition (`append`, `extend`, `insert`)
    2. Removal (`remove`, `pop`, `clear`)
    3. Inspection & Search (`index`, `count`)
    4. Reordering (`sort`, `reverse`, `copy`)

How to Run:
    $ python list_methods_tutorial.py
"""

def demonstrate_list_methods():
    # =========================================================================
    # 1. ADDING ELEMENTS
    # =========================================================================
    print("--- 1. Adding Elements ---")
    fruits = ["Apple", "Banana"]
    print("Initial List:", fruits)

    # .append(element) - Adds an item to the end of the list
    fruits.append("Cherry")
    print("After .append('Cherry'):", fruits)

    # .insert(index, element) - Inserts an item at a specific position
    fruits.insert(1, "Mango")
    print("After .insert(1, 'Mango'):", fruits)

    # .extend(iterable) - Appends elements from another iterable to the end
    tropical_fruits = ["Papaya", "Pineapple"]
    fruits.extend(tropical_fruits)
    print("After .extend(tropical_fruits):", fruits)
    print("\n" + "="*40 + "\n")

    # =========================================================================
    # 2. REMOVING ELEMENTS
    # =========================================================================
    print("--- 2. Removing Elements ---")
    
    # .remove(value) - Removes the first occurrence of a specific value
    fruits.remove("Banana")
    print("After .remove('Banana'):", fruits)

    # .pop(index) - Removes and RETURNS the item at the given index (defaults to last item)
    popped_fruit = fruits.pop(2)
    print(f"Popped item at index 2 ('{popped_fruit}'):", fruits)
    
    last_fruit = fruits.pop()
    print(f"Popped last item ('{last_fruit}'):", fruits)
    print("\n" + "="*40 + "\n")

    # =========================================================================
    # 3. SEARCHING AND INSPECTING
    # =========================================================================
    print("--- 3. Searching and Inspecting ---")
    # Let's add some duplicates for demonstration
    fruits.extend(["Apple", "Mango", "Apple"])
    print("Current List:", fruits)

    # .count(value) - Returns the number of times a value appears
    apple_count = fruits.count("Apple")
    print(f"Number of times 'Apple' appears: {apple_count}")

    # .index(value) - Returns the index of the first occurrence of a value
    mango_index = fruits.index("Mango")
    print(f"First index of 'Mango': {mango_index}")
    print("\n" + "="*40 + "\n")

    # =========================================================================
    # 4. ORDERING AND REVERSING
    # =========================================================================
    print("--- 4. Ordering and Reversing ---")
    
    # .reverse() - Reverses the elements of the list in-place
    fruits.reverse()
    print("After .reverse():", fruits)

    # .sort() - Sorts the items of the list in-place (alphabetically/numerically)
    fruits.sort()
    print("After .sort() (Ascending):", fruits)

    # Sorting in descending order using the 'reverse=True' parameter
    fruits.sort(reverse=True)
    print("After .sort(reverse=True) (Descending):", fruits)
    print("\n" + "="*40 + "\n")

    # =========================================================================
    # 5. COPYING AND CLEARING
    # =========================================================================
    print("--- 5. Copying and Clearing ---")
    
    # .copy() - Returns a shallow copy of the list
    fruits_backup = fruits.copy()
    print("Backup copy created:", fruits_backup)

    # .clear() - Removes all items from the list
    fruits.clear()
    print("After .clear():", fruits)
    print("Backup remains untouched:", fruits_backup)


if __name__ == "__main__":
    demonstrate_list_methods()