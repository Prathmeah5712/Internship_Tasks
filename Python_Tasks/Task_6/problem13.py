# Problem Name: Set .union() Operation[cite: 24]
# Link: https://www.hackerrank.com/challenges/py-set-union/problem[cite: 24]

input()
set_a = set(map(int, input().split()))
input()
set_b = set(map(int, input().split()))
print(len(set_a.union(set_b)))
