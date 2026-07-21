def maximo(lista):
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for num in lista[1:]:
        if num > maximo:
            maximo = num
    return maximo

def minimo(lista):
    if len(lista) == 0:
        return None
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

while True:
    numeros = []
    for i in range(8):
        num = int(input("Numero {}:".format(i+1)))
        numeros.append(num)

    num_M = maximo(numeros)
    num_m = minimo(numeros)
    fun_M = max(numeros)
    fun_m = min(numeros)
    print("Numero mayor man.: ", num_M)
    print("Numero menor man.: ", num_m)
    print("Numero mayor fun.: ", fun_M)
    print("Numero menor fun.: ", fun_m)
    print(numeros)

    res = input("De nuevo? (si)=s/(no)=otro: ")
    if res != 's':
        break
print("ADIOS")