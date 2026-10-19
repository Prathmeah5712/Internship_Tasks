# Problem: The Captain's Room
k = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)
captain_room = (k * sum(room_set) - sum(rooms)) // (k - 1)
print(captain_room)
