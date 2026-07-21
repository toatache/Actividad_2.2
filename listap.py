def contar(n):
    pares = 0
    impares = 0
    for num in n:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

while True:
    numeros = []
    for i in range(10):
        num = int(input("Numero {}:".format(i+1)))
        numeros.append(num)

    p, i = contar(numeros)
    print("Pares: ", p)
    print("Impares: ", i)
    print(numeros)

    res = input("De nuevo? (si)=s/(no)=otro: ")
    if res != 's':
        break
print("ADIOS")