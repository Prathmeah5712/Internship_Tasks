# Problem Name: collections.Counter()[cite: 20]
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
shoe_sizes = Counter(map(int, input().split()))
n = int(input())

total_earned = 0
for _ in range(n):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        shoe_sizes[size] -= 1
        total_earned += price

print(total_earned)
