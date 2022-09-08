for i in range(10):
    print(i, end =' ')
print('') # Quebra de Linha
for i in range(1, 11):
        print(i, end =' ')
print('') # Quebra de Linha
for i in range(0, 100, 10):
        print(i, end =' ')
print('') # Quebra de Linha
for i in range(20, 0, -3):
        print(i, end =' ')
print('') # Quebra de Linha
nums = [2, 4, 6, 8]
for n in nums:
    print(n, end =' ')
print('') # Quebra de Linha
texto = 'Python é muito massa!'

for letra in texto:
    print(letra, end= ' ')
print('') # Quebra de Linha
for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')
print('') # Quebra de Linha
produto = {
    'nome' :  'caneta',
    'preco' :  8.80,
    'desc' : 0.5
}

for dic in produto:
    print(dic, ':', produto[dic], end =' ')
print('') # Quebra de Linha
for dic, valor in produto.items():
    print(dic, '->', valor, end =' ')
print('') # Quebra de Linha
for valor in produto.values():
    print(valor, end= ' ')
print('') # Quebra de Linha
for dic in produto.keys():
    print(dic, end= ' ')