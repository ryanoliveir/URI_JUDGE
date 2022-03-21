
valor = int(input())

print(valor)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for i in range(0, len(cedulas)):
    
    numero_cedulas = valor // cedulas[i]
    print(f'{numero_cedulas} nota(s) de R$ {cedulas[i]},00')
    valor -= numero_cedulas * cedulas[i]