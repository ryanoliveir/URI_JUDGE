
total_days = int(input())

year = 365

years =  total_days // year

months = (total_days % year) // 30

days = (total_days % year) % 30


print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")