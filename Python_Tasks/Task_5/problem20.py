# Problem Name: Piling Up![cite: 24]
# HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    d = deque(map(int, input().split()))
    
    possible = True
    last = float('inf')
    
    while d:
        if d[0] >= d[-1]:
            elem = d.popleft()
        else:
            elem = d.pop()
            
        if elem <= last:
            last = elem
        else:
            possible = False
            break
            
    if possible:
        print("Yes")
    else:
        print("No")
