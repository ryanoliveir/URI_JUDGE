

tempo_segundos = int(input())


segundos = tempo_segundos % 60

minutos = (tempo_segundos // 60) % 60

horas = (tempo_segundos // 60 ) // 60

print(horas,minutos,segundos, sep=":")