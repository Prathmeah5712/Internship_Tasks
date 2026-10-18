# Problem Name: Set .discard(), .remove() & .pop()[cite: 24]
# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem[cite: 24]

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    try:
        line = input().split()
        if not line:
            continue
        cmd = line[0]
        if cmd == 'pop':
            if s:
                s.pop()
        elif cmd == 'remove':
            val = int(line[1])
            if val in s:
                s.remove(val)
        elif cmd == 'discard':
            s.discard(int(line[1]))
    except (EOFError, IndexError):
        break

print(sum(s))
