
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)


valores= [n1, n2, n3]
valores.sort()

print(*valores, sep ="\n")
print()
print(f'{n1}\n{n2}\n{n3}')


