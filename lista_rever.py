def invertir(lista):
    invertida = []
    for num in range(len(lista) - 1, -1, -1):
        invertida.append(lista[num])
    return invertida

while True:
    numeros = []
    for i in range(6):
        num = int(input("Numero {}:".format(i+1)))
        numeros.append(num)

    print("Original: ", numeros)

    invertida = invertir(numeros)
    print("Invertida: ", invertida)

    res = input("De nuevo? (si)=s/(no)=otro: ")
    if res != 's':
        break
print("ADIOS")