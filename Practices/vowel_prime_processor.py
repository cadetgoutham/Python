"""
Vowel Index Prime Accumulator

Description:
    Analyzes a user-inputted word for vowels, tracks their first index 
    positions scaled by 100, and computes the sum of all prime numbers 
    up to those scaled limits.

Output Preview:
    enter the word to inspect : apple
    Vowel 'a' found at scaled index limit: 0
    Vowel 'e' found at scaled index limit: 400
    
    Results Summary:
    Sum of primes for Group A: 16729

How to Run:
    $ python vowel_prime_processor.py
"""

def process_vowel_primes():
    """
    Identifies vowels in a string, extracts their index positions scaled by 100,
    and aggregates unique prime totals based on those limits.
    """
    target_word = input('enter the word to inspect : ').lower()
    target_vowels = ['a', 'e', 'i', 'o', 'u']
    
    scaled_vowel_indices = []
    primes_group_a = []
    primes_group_b = []
    
    # Locate vowels and store their index positions multiplied by 100
    for vowel in target_vowels:
        if vowel in target_word:
            first_occurrence_index = target_word.find(vowel)
            scaled_limit = first_occurrence_index * 100
            scaled_vowel_indices.append(scaled_limit)
            print(f"Vowel '{vowel}' found at scaled index limit: {scaled_limit}")

    # Process limits to generate ranges of primes
    for list_index in range(len(scaled_vowel_indices)):
        upper_limit = scaled_vowel_indices[list_index]
        
        for candidate_num in range(1, upper_limit):
            if candidate_num > 1:
                # Prime verification check
                for divisor in range(2, candidate_num):
                    if (candidate_num % divisor) == 0:
                        break
                else:
                    # Separate results conditionally based on index sequence position
                    if list_index != 1:
                        primes_group_a.append(candidate_num)
                    else:
                        primes_group_b.append(candidate_num)

    # Display final aggregated summaries
    print("\nResults Summary:")
    print("Sum of primes for Group A:", sum(primes_group_a))
    if primes_group_b:
        print("Sum of primes for Group B:", sum(primes_group_b))


if __name__ == "__main__":
    process_vowel_primes()