def sumar(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

while True:
    numeros = []
    for i in range(5):
        num = int(input("Numero {}:".format(i+1)))
        numeros.append(num)

    total = sumar(numeros)
    total_m = sum(numeros)
    print("Total bucle: ", total)
    print("Total sum: ", total_m)
    print(numeros)

    res = input("De nuevo? (si)=s/(no)=otro: ")
    if res != 's':
        break
print("ADIOS")