"""
Range Prime Number Finder

Description:
    A self-contained Python script that calculates and prints all 
    prime numbers within a user-specified range.

Output Preview:
    enter starting no : 1
    enter ending no : 20
    2 3 5 7 11 13 17 19 

How to Run:
    $ python prime_range_finder.py
"""

def generate_primes_in_range():
    """Finds and prints prime numbers within a specified boundary."""
    try:
        range_start = int(input('enter starting no : '))
        range_end = int(input('enter ending no : '))
    except ValueError:
        print("Please enter valid integers.")
        return

    print("Prime numbers in range:", end=' ')
    for current_num in range(range_start, range_end + 1):
        factor_count = 0
        for divisor in range(1, current_num + 1):
            if current_num % divisor == 0:
                factor_count += 1
        if factor_count == 2:
            print(current_num, end=' ')
    print()  # Final newline


if __name__ == "__main__":
    generate_primes_in_range()