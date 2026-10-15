from solutions import (
    word_frequency,
    char_frequency,
    first_non_repeating_char,
    are_anagrams,
    first_repeating_char,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates_preserve_order,
    find_missing_number,
    two_sum_first_pair,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_sum,
    all_pairs_with_target_sum
)

def run_tests():
    print("--- Q1: Word Frequency ---")
    print("Given Test:     ", word_frequency("python is easy and python is powerful"))
    print("Additional Test:", word_frequency("data science is fun and python is fun"))
    print()

    print("--- Q2: Character Frequency ---")
    print("Given Test:     ", char_frequency("banana"))
    print("Additional Test:", char_frequency("internship"))
    print()

    print("--- Q3: First Non-Repeating Character ---")
    print("Given Test:     ", first_non_repeating_char("swiss"))
    print("Additional Test:", first_non_repeating_char("aabbcc"))
    print()

    print("--- Q4: Anagram Check ---")
    print("Given Test:     ", are_anagrams("listen", "silent"))
    print("Additional Test:", are_anagrams("triangle", "integral"))
    print()

    print("--- Q5: First Repeating Character ---")
    print("Given Test:     ", first_repeating_char("programming"))
    print("Additional Test:", first_repeating_char("abcdef"))
    print()

    print("--- Q6: Move Zeros to End ---")
    print("Given Test:     ", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
    print("Additional Test:", move_zeros_to_end([1, 0, 2, 0, 3, 0]))
    print()

    print("--- Q7: Second Highest Distinct ---")
    print("Given Test:     ", second_highest_distinct([10, 20, 40, 30, 40, 20]))
    print("Additional Test:", second_highest_distinct([50, 50, 50]))
    print()

    print("--- Q8: Remove Duplicates Preserving Order ---")
    print("Given Test:     ", remove_duplicates_preserve_order([4, 2, 4, 5, 2, 7, 5]))
    print("Additional Test:", remove_duplicates_preserve_order([10, 20, 10, 30, 20, 40]))
    print()

    print("--- Q9: Find Missing Number ---")
    print("Given Test:     ", find_missing_number([1, 2, 4, 5, 6], 6))
    print("Additional Test:", find_missing_number([2, 3, 4, 5], 5))
    print()

    print("--- Q10: Two Sum First Pair ---")
    print("Given Test:     ", two_sum_first_pair([2, 7, 11, 15], 9))
    print("Additional Test:", two_sum_first_pair([1, 3, 5, 8], 14))
    print()

    print("--- Q11: Closest to Zero ---")
    print("Given Test:     ", closest_to_zero([-8, -3, 2, 5, -2]))
    print("Additional Test:", closest_to_zero([-4, 4, -1, 1]))
    print()

    print("--- Q12: Common Elements ---")
    print("Given Test:     ", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("Additional Test:", common_elements([10, 20, 30, 40], [30, 50, 10, 60]))
    print()

    print("--- Q13: Rotate Right by K ---")
    print("Given Test:     ", rotate_right([1, 2, 3, 4, 5], 2))
    print("Additional Test:", rotate_right([10, 20, 30, 40, 50], 3))
    print()

    print("--- Q14: Max Consecutive Sum ---")
    print("Given Test:     ", max_consecutive_sum([4, 7, 2, 9, 5]))
    print("Additional Test:", max_consecutive_sum([1, -2, 5, 8, 3]))
    print()

    print("--- Q15: All Unique Pairs with Target Sum ---")
    print("Given Test:     ", all_pairs_with_target_sum([2, 4, 3, 5, 7, 8, 1], 9))
    print("Additional Test:", all_pairs_with_target_sum([1, 5, 3, 3, 2, 4], 6))
    print()

if __name__ == "__main__":
    run_tests()