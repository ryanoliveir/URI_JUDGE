
a, b, c, d = input().split(" ")
a, b, c, d = int(a), int(b), int(c), int(d)

confirmation = 0
if(b > c and d > a ):
	confirmation += 1

	if(c + d > a + b):
		confirmation += 1
	

		if(c > 0 and d > 0):
			confirmation += 1
		

			if(a % 2 == 0):
				confirmation += 1
				


if(confirmation != 4):
	print("Valores nao aceitos")
else:
	print("Valores aceitos")
