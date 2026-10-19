# Problem: Gemstones
def gemstones(arr):
    gem_set = set(arr[0])
    for rock in arr[1:]:
        gem_set.intersection_update(rock)
    return len(gem_set)

if __name__ == '__main__':
    n = int(input().strip())
    arr = [input().strip() for _ in range(n)]
    print(gemstones(arr))
