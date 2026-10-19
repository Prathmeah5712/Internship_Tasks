# Problem: Game of Thrones - I
def gameOfThrones(s):
    from collections import Counter
    counts = Counter(s).values()
    odd_count = sum(1 for c in counts if c % 2 != 0)
    return "YES" if odd_count <= 1 else "NO"

if __name__ == '__main__':
    s = input().strip()
    print(gameOfThrones(s))
