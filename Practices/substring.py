# Check if one string is a substring of another without using built-in methods

def isSubstring(main_string, sub_string):
    # A longer string cannot be a substring of a shorter one
    if len(sub_string) > len(main_string):
        return False

    main_len = len(main_string)
    sub_len = len(sub_string)

    # Slide a window of sub_len across main_string
    for start in range(0, (main_len - sub_len) + 1):
        match = True

        # Compare each character of sub_string with the current window
        for offset in range(0, sub_len):
            if main_string[start + offset] != sub_string[offset]:
                match = False
                break  # Mismatch found, no need to check further

        if match:
            return True  # All characters matched

    return False  # No matching window found


if __name__ == "__main__":
    main_string = "helloworld"
    sub_string = "world"

    print(isSubstring(main_string, sub_string))

