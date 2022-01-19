pesos = []


def pesoMaior90kg(lista):
    aux = 0
    for i in range(0, len(lista)):
        if lista[i] > 90:
            aux += 1

    return aux
def calculaMediaPesos(lista):
    aux = 0
    for i in range(0, len(lista)):
        aux += lista[i]

    return aux / len(lista)


for i in range(1, 8):
    pesos.append(float(input("Digite o peso do cara:")))


print(pesos)



print(f'A quantidade de pessoas com peso maior que 90: {pesoMaior90kg(pesos)}')
print(f'A media dos pesos: {calculaMediaPesos(pesos)}')


