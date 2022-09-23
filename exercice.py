#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	sous_total = 0

	for i in data:
		sous_total += i[1] * i[2]

	taxes = sous_total * 0.15
	total = sous_total + taxes

	return ("""%s
SOUS TOTAL    %.2f$
TAXES         %.2f$
TOTAL         %.2f$
""" % (name, sous_total, taxes, total))


def format_number(number, num_decimal_digits):

	full_part = str((round((abs(number) // 1))))
	decimal_part2 = number % 1.00
	decimal_part = str(round((abs(number) % 1.0), num_decimal_digits))
	final = ''
	count = 0

	for i in reversed(full_part):
		if count % 3 == 0 and count != 0:
			final = i + ' ' + final
		else:
			final = i + final

		count += 1

	for i in range(len(decimal_part)):
		if i > 0:
			final = final + decimal_part[i]

	return ("-" if number < 0 else "") + final

def get_triangle(num_rows):
	space = ' '
	count_space = num_rows - 1
	number_rows = 1
	dessin = 'A'
	print('+' * (2 * num_rows + 1))

	while number_rows <= num_rows:  # 1, 2 pour 2 rows
		if number_rows != num_rows:
			print(f'+{space * count_space}{dessin * (2 * number_rows - 1)}{space * count_space}+')
			number_rows += 1
			count_space -= 1
		else:
			print(f'+{dessin * (2 * num_rows - 1)}+')
			number_rows += 1

	print('+' * (2 * num_rows + 1))

	return

if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
