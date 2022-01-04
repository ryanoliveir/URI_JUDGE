#notas
n1, n2, n3, n4 = input().split(" ")
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

#pesos
p1, p2, p3, p4 = 2, 3, 4, 1
#peso_total
p_total = p1 + p2 + p3 + p4

#media
media = (n1*p1 + n2*p2 + n3*p3 + n4*p4)/ p_total



#aprovado
if media >= 7.0:
	print(f'Media: {media:.1f}\nAluno aprovado.')
#reprovado
elif media < 5.0:
	print(f'Media: {media:.1f}\nAluno reprovado.')
#exame
elif media >= 5 and media <= 6.9:
	print(f'Media: {media:.1f}\nAluno em exame.')
	
	n_exame = float(input())
	print(f'Nota do exame: {n_exame:.1f}')

	media_final = (media + n_exame)/2

	#exame_final
	if media_final >= 5:
		print('Aluno aprovado.')
	else:
		print('Aluno reprovado.')

	print(f'Media final: {media_final}')