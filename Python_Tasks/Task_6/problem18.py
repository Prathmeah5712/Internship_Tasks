# Problem Name: Set Mutations[cite: 24]
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem[cite: 24]

input()
A = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, _ = input().split()
    other = set(map(int, input().split()))
    getattr(A, cmd)(other)

print(sum(A))
