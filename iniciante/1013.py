
a, b, c = input().split(" ")

a, b, c  = int(a), int(b), int(c)


maior_ab = int((a + b + abs(a-b))/2)


if (maior_ab > c):
	print(f'{maior_ab} eh o maior')
else:
	print(f'{c} eh o maior')