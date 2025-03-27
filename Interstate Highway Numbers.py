highway_number = int(input())
direction = 'north/south' if highway_number % 2 == 1 else 'east/west'
primary_highway = highway_number % 100
direction = 'east/west' if primary_highway % 2 == 0 else 'north/south'

if primary_highway == 0:
    print(f'{highway_number} is not a valid interstate highway number.')
elif highway_number > 1 and highway_number < 100:
    print(f'I-{highway_number} is primary, going {direction}.')
elif highway_number > 100 and highway_number < 1000:
    print(f'I-{highway_number} is auxiliary, serving I-{primary_highway}, going {direction}.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')