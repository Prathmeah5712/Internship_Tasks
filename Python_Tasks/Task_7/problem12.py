# Problem: Making Anagrams
def makingAnagrams(s1, s2):
    from collections import Counter
    count1 = Counter(s1)
    count2 = Counter(s2)
    diff = count1 - count2
    diff2 = count2 - count1
    return sum(diff.values()) + sum(diff2.values())

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(makingAnagrams(s1, s2))
