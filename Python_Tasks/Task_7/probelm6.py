# Problem: Pangrams
def pangrams(s):
    letters = set(c.lower() for c in s if c.isalpha())
    return "pangram" if len(letters) == 26 else "not pangram"

if __name__ == '__main__':
    s = input()
    print(pangrams(s))
