# Problem Name: Check Strict Superset[cite: 24]
# Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem[cite: 24]

a = set(map(int, input().split()))
n = int(input())
result = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not a.issuperset(other) or len(a) <= len(other):
        result = False

print(result)
