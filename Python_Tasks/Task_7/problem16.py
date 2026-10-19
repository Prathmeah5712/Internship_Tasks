# Problem: Caesar Cipher
def caesarCipher(s, k):
    encrypted = []
    for char in s:
        if char.isupper():
            encrypted.append(chr((ord(char) - 65 + k) % 26 + 65))
        elif char.islower():
            encrypted.append(chr((ord(char) - 97 + k) % 26 + 97))
        else:
            encrypted.append(char)
    return "".join(encrypted)

if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    print(caesarCipher(s, k))
