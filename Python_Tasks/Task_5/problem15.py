# Problem Name: Lists[cite: 19]
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        args = command[1:]
        
        if cmd == "print":
            print(lst)
        else:
            eval(f"lst.{cmd}({','.join(args)})")
