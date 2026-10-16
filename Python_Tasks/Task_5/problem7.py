# Problem Name: Symmetric Difference[cite: 7]
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))

diff = sorted(set1.symmetric_difference(set2))
for x in diff:
    print(x)
