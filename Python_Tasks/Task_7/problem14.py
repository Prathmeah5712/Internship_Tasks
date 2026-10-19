# Problem: Anagram
def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    
    from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    diff = c1 - c2
    return sum(diff.values())

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(anagram(s))
