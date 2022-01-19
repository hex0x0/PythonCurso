


soma = 0
cont = 0
x = int(input("Digite uma idade:"))
soma = x
cont = 1
while x != -1:
    x = int(input("Digite uma idade:"))
    if x == -1:
        break
    soma += x
    cont += 1

print(soma / cont )