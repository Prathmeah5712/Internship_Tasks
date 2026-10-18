# Problem Name: Validating the Phone Number[cite: 24]
# Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem[cite: 24]

import re

for _ in range(int(input())):
    number = input().strip()
    if re.match(r"^[789]\d{9}$", number):
        print("YES")
    else:
        print("NO")
