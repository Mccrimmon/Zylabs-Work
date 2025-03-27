phone_number = int(input())

area_code = phone_number // 10000000
first_three = (phone_number // 10000) % 1000
last_four = phone_number % 10000

output = f'({area_code:03d}) {first_three:03d}-{last_four:04d}'
print(output)