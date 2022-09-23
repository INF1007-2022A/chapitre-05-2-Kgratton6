number = -1456846.8946
num_decimal_digits = 2
full_part = str((round((abs(number) // 1))))
decimal_part2 = number % 1.00
decimal_part = str(round((abs(number) % 1.0), num_decimal_digits))
final = ''
count = 0

for i in reversed(full_part):
	if (count % 3) == 0 and count != 0:
		final = i + ' ' + final
	else:
		final = i + final

	count += 1

for i in range(len(decimal_part)):
	if i > 0:
		final = final + decimal_part[i]

print(("-" if number < 0 else "") + final)