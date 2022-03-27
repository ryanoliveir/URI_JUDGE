

value = float(input())

bancknotes_list = [100, 50, 20, 10, 5, 2]
coins_list = [1, 0.5, 0.25, 0.10, 0.05, 0.01]


print("NOTAS:")
for bancknote in bancknotes_list:

	bancknotes_number = int(value // bancknote)
	print(f"{bancknotes_number} nota(s) de R$ {bancknote:.2f}")
	value -= bancknotes_number * bancknote

print("MOEDAS:")
for coin in coins_list:

	coins_number = int(round(value, 2) / coin)
	print(f"{coins_number} moeda(s) de R$ {coin:.2f}")
	value -= coins_number * coin

