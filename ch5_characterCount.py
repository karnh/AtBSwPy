import pprint

message = 'Mozerella cheese'
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] += 1

pprint.pprint(count)