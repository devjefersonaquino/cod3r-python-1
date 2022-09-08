pessoas = ['Gui', 'Ana', 'João']
adj = ['Sapeca', 'Inteligente', 'Esperto']

for p in pessoas:
    for a in adj:
        print(f'{p} é {a}.')

for i in [1, 2, 3]:
    pass
print(' ') # Quebra de Linha
for i in range (1, 11):
    if i % 2:
        continue
    print(i, end= ' ')

print(' ') # Quebra de Linha
for i in range(1, 11):
    if i == 5:
        break
    print(i, end= ' ')
print(' ') # Quebra de Linha
print('Fim!')