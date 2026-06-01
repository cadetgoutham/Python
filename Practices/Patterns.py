'''
Print a diagonal number pattern based on a given value n.
Example for n=6:
1 7 12 16 19 21
2 8 13 17 20
3 9 14 18
4 10 15
5 11
6
'''

if __name__ == "__main__":
    n = 6

    # Outer loop: each row starts from i
    for row in range(1, n + 1):
        step = n          # Step size decreases as we move right in each row
        current = row     # Current value to print; starts at the row number

        # Inner loop: print values across the current row
        for col in range(row, n + 1):
            print(f'{current} ', end="")

            if col != row:
                # Decrease the step size after the first element in the row
                step -= 1

            # Advance current value by the current step
            current += step

        print()  # Move to the next line after each row