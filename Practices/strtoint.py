'''
Convert a numeric string to an integer without using built-in int().
Raises an error if the string contains non-numeric or decimal characters.
'''

if __name__ == "__main__":
    # Mapping of digit characters to their integer values
    digit_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                 '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    input_string = '10jhbjc0'
    place_value = 0   # Tracks the current power of 10 (units, tens, hundreds, ...)
    result = 0        # Accumulates the final integer value

    try:
        # Iterate over the string in reverse to process from least significant digit
        for char in input_string[::-1]:
            if char == '.':
                # Decimal point means the input is not a pure integer
                raise ValueError("Given input is not an integer (contains decimal point).")
            elif char in digit_map:
                # Multiply digit by its positional value and add to result
                result += digit_map[char] * (10 ** place_value)
                place_value += 1
            else:
                # Non-numeric character found
                raise KeyError(f"Given input is not a number (invalid character: '{char}').")

        print(isinstance(result, int))  # Should print True
        print(result)
    except Exception as error:
        print(error)