# Problem: Weighted Uniform Strings
def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    prev_char = ''
    
    for char in s:
        char_weight = ord(char) - 96
        if char == prev_char:
            current_weight += char_weight
        else:
            current_weight = char_weight
            prev_char = char
        weights.add(current_weight)
        
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())
    queries = [int(input().strip()) for _ in range(n)]
    print("\n".join(weightedUniformStrings(s, queries)))
