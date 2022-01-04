 
a, b, c = input().split(" ")

a, b, c = float(a), float(b), float(c)

pi = 3.14159


triangulo = f'TRIANGULO: {((a * c)/2) :.3f}'
circulo = f'CIRCULO: {(pi * (c ** 2)) :.3f}'
trapezio = f'TRAPEZIO: {(((a + b) * c)/2) :.3f}'
quadrado = f'QUADRADO: {b ** 2 :.3f}'
retangulo = f'RETANGULO: {a * b :.3f}'

print(f'{triangulo}\n{circulo}\n{trapezio}\n{quadrado}\n{retangulo}')

