# Problem: Separate the Numbers
def separateNumbers(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        x_str = s[:i]
        x = int(x_str)
        current = x
        built = x_str
        while len(built) < length:
            current += 1
            built += str(current)
        if built == s:
            print(f"YES {x}")
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
