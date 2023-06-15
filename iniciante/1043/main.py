
a , b, c = input().split(' ')

a, b, c = float(a), float(b), float(c)

isTrinagle = False

# check a sement
if (abs(b - c) < a < b + c):
    isTrinagle = True

# check b sement
if (abs(a - c) < b < a + c):
    isTrinagle = True

# check c sement
if (abs(a - c) < b < a + c):
    isTrinagle = True


if(isTrinagle):
    perimeter = a + b + c
    print("Perimetro = {:.1f}".format(perimeter))
else: 
    trapeze_area = ((a + b) * c) / 2
    print("Area = {:.1f}".format(trapeze_area))


    



