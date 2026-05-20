#5. Realizar un programa que lea los lados de n triángulos, e informar:
#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
#iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.

n = int(input("Cantidad de triángulos: "))

equilateros = 0
isoceles = 0
escalenos = 0

for x in range(n):
    print("Triángulo", x+1)
    a = int(input("Lado 1: "))
    b = int(input("Lado 2: "))
    c = int(input("Lado 3: "))

    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Equilatero")
            equilateros += 1
        elif a == b or a == c or b == c:
            print("Isosceles")
            isoceles += 1
        else:
            print("Escaleno")
            escalenos += 1
    else:
        print("No es un triangulo valido")
print(f"Equilateros {equilateros}")
print(f"Isosceles {isoceles}")
print(f"Escaleno {escalenos}")

