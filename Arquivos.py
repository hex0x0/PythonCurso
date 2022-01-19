"""
w - cria um arquivo. se ele já existir, sobrescreve
a - cria um arquivo. se ele já existir, adiciona no fim
file.read() - retorna todo o conteúdo lido
file.readlines() -> retorna uma lista separada por quebras de linha


ex1.


texto = "Perdi foi tudo kek  xd\n"
arquivo.write(texto)

"""

arquivo = open('C:\\Users\\delta\\Desktop\\teste.txt', 'r')

x = arquivo.readlines()

print(x[0])

arquivo.close



