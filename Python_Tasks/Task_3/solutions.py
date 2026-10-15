# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_char(word):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in word:
        if counts[ch] == 1:
            return ch
    return None

# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Q5. Find the First Repeating Character in a String
def first_repeating_char(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros

# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(lst):
    distinct = sorted(list(set(lst)), reverse=True)
    return distinct[1] if len(distinct) >= 2 else None

# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, N):
    expected_sum = N * (N + 1) // 2
    return expected_sum - sum(nums)

# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first_pair(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return []

# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    closest = nums[0]
    for n in nums[1:]:
        if abs(n) < abs(closest):
            closest = n
        elif abs(n) == abs(closest) and n > closest:
            closest = n
    return closest

# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    set2 = set(list2)
    seen = set()
    result = []
    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k != 0 else nums[:]

# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs_with_target_sum(nums, target):
    seen_elements = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen_elements:
            pair = tuple(sorted([complement, num]))
            pairs.add(pair)
        seen_elements.add(num)
    sorted_pairs = sorted([list(p) for p in pairs], key=lambda x: x[0])
    return sorted_pairs