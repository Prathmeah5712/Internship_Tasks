# Problem: Sherlock and the Valid String
def isValid(s):
    from collections import Counter
    freq = Counter(s)
    counts = list(freq.values())
    
    if len(set(counts)) == 1:
        return "YES"
    if len(set(counts)) > 2:
        return "NO"
        
    c_freq = Counter(counts)
    if len(c_freq) == 2:
        (f1, count1), (f2, count2) = c_freq.items()
        if (f1 == 1 and count1 == 1) or (f2 == 1 and count2 == 1):
            return "YES"
        if (abs(f1 - f2) == 1) and ((f1 > f2 and count1 == 1) or (f2 > f1 and count2 == 1)):
            return "YES"
            
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))
