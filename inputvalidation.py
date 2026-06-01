"""
Dictionary Builder and Input Validator

Description:
    A self-contained script demonstrating interactive dictionary generation 
    from runtime user inputs combined with type-specific exception handling 
    during modifying actions.

Output Preview:
    Enter number of entries - 2
    enter key - id
    enter value - 101
    ...
    Created dictionary: {'id': '101'}

How to Run:
    $ python dict_validator.py
"""

def create_dictionary():
    """
    Prompts the user for a size parameter with continuous input validation,
    then aggregates key-value strings into a new dictionary object.
    """
    user_data = {}
    entry_count = 0

    # Loop persists until a valid base-10 integer is captured
    while True:
        try:
            entry_count = int(input("Enter number of entries - "))
            break
        except ValueError:
            print("Invalid format. Please supply a valid whole number integer.")

    # Populate data mappings sequentially
    for index in range(entry_count):
        dict_key = input("enter key - ")
        dict_value = input("enter value - ")
        user_data[dict_key] = dict_value

    return user_data


def modify_dictionary_key(target_dict):
    """
    Updates the value of an existing key within a given dictionary,
    safely handling instances where the target key is missing.
    """
    search_key = input("Enter the key of the dictionary to update - ")

    # Check for presence explicitly to guide flow without forcing artificial try/catch blocks
    if search_key in target_dict:
        updated_value = input("Enter the new value for this key - ")
        target_dict[search_key] = updated_value
    else:
        print(f"Caught Error: Key '{search_key}' is missing from the dictionary mapping.")

    return target_dict


def main():
    # Phase 1: Initialize and construct the map object
    configured_dict = create_dictionary()
    print("Created dictionary:", configured_dict)

    # Phase 2: Alter value states safely
    configured_dict = modify_dictionary_key(configured_dict)
    print("Modified dictionary:", configured_dict)


if __name__ == "__main__":
    main()