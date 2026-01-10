
x = 0
suma = 0
tem = ""

while x < 10:
    suma += x
    tem += str(x) + "+"
    x += 2

print("La suma de los números pares menores a 10 es:")
print(tem[:-1], "=", suma)
