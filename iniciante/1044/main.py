
num1 , num2 = input().split(' ')

num1, num2 = int(num1), int(num2)

if (num1 % num2 == 0 or num2 % num1 == 0): 
    print("Sao Multiplos")
else: 
    print("Nao sao Multiplos")

