# Problem Name: What's Your Name?[cite: 24]
# Link: https://www.hackerrank.com/challenges/whats-your-name/problem[cite: 24]

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
