# Problem: Alphabet Rangoli
def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        chopped = alphabet[i:size]
        row = list(reversed(chopped)) + list(chopped[1:])
        lines.append("-".join(row))
    
    width = len(lines[0])
    final_lines = lines[::-1] + lines[1:]
    for line in final_lines:
        print(line.center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
