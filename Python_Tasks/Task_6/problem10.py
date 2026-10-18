# Problem Name: Designer Door Mat[cite: 24]
# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem[cite: 24]

N, M = map(int, input().split())

for i in range(1, N, 2):
    print((".|." * i).center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N - 2, 0, -2):
    print((".|." * i).center(M, "-"))
