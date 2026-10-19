# Problem: CamelCase
def camelcase(s):
    count = 1
    for char in s:
        if char.isupper():
            count += 1
    return count

if __name__ == '__main__':
    s = input().strip()
    print(camelcase(s))
