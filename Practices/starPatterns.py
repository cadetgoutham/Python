"""
Inverted Number Triangle Pattern Generator

Description:
    A simple Python script that uses nested while loops to generate 
    a right-aligned, inverted triangle pattern of repeating numbers.

Output Preview:
    5   5   5   5   5   
      4   4   4   4   
        3   3   3   
          2   2   
            1   

How It Works:
    1. Outer Loop: Manages the row count, starting from the maximum number 
       and decrementing down to 1.
    2. First Inner Loop: Handles right-alignment by printing the 
       required leading spaces.
    3. Second Inner Loop: Prints the actual row number, repeating it 
       to match the current row's value.

How to Run:
    Command Line / Terminal:
    $ python pattern_generator.py
"""

def generate_pattern():
    # Define the total number of rows for the pattern
    total_rows = 5
    current_row = total_rows

    # Outer loop handles the rows, counting down from total_rows to 1
    while current_row >= 1:
        
        # 1. Print the leading spaces for right-alignment
        # The number of spaces increases as the row number decreases
        leading_spaces = total_rows
        while leading_spaces > current_row:
            print(' ', end=' ')
            leading_spaces -= 1
            
        # 2. Print the numbers for the current row
        # The quantity of numbers printed matches the current row value
        number_columns = 1
        while number_columns <= current_row:
            print(current_row, ' ', end=' ')
            number_columns += 1    
            
        # Move to the next line after completing the current row
        print()
        current_row -= 1

if __name__ == "__main__":
    # This block ensures the script runs automatically when executed directly,
    # but won't run automatically if imported as a module elsewhere.
    generate_pattern()