id1, q1, valor1 = input().split(" ")
id2, q2, valor2 = input().split(" ")


id1, q1, valor1 = int(id1), int(q1), float(valor1)
id2, q2, valor2 = int(id2), int(q2), float(valor2)

total1 = q1*valor1
total2 = q2*valor2 


print("VALOR A PAGAR : R$ {:.2f}".format(total2+total1))
