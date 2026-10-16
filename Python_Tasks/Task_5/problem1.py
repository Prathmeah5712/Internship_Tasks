# Problem Name: Find the Runner-Up Score![cite: 1]
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = set(arr)
    sorted_scores = sorted(unique_scores)
    print(sorted_scores[-2])
