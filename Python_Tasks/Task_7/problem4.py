# Problem: Funny String
def funnyString(s):
    s_rev = s[::-1]
    diff1 = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1)]
    diff2 = [abs(ord(s_rev[i]) - ord(s_rev[i+1])) for i in range(len(s_rev) - 1)]
    return "Funny" if diff1 == diff2 else "Not Funny"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(funnyString(s))
