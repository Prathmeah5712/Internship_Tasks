# Problem Name: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
shoe_inventory = Counter(map(int, input().split()))
n = int(input())

total_money = 0
for _ in range(n):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        total_money += price
        shoe_inventory[size] -= 1

print(total_money)
