# Problem: Beautiful Binary String
def beautifulBinaryString(b):
    count = 0
    i = 0
    b_list = list(b)
    while i <= len(b_list) - 3:
        if b_list[i] == '0' and b_list[i+1] == '1' and b_list[i+2] == '0':
            b_list[i+2] = '1'
            count += 1
            i += 3
        else:
            i += 1
    return count

if __name__ == '__main__':
    n = int(input().strip())
    b = input().strip()
    print(beautifulBinaryString(b))
