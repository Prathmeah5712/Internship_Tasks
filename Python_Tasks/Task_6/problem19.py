# Problem Name: Company Logo[cite: 24]
# Link: https://www.hackerrank.com/challenges/most-commons/problem[cite: 24]

from collections import Counter

if __name__ == '__main__':
    s = input()
    sorted_chars = sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))
    for char, freq in sorted_chars[:3]:
        print(char, freq)
