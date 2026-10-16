# Problem Name: Set .add()[cite: 9]
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
stamps = set()
for _ in range(n):
    stamps.add(input())
print(len(stamps))
