nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado? (s/n): ') == 's' else False

if nota >= 9 and comportado:
    print(f'Quadro de Honra: PARABENS, nota: {nota}.')
elif nota >= 7:
    print(f'Aprovado, nota: {nota}.')
elif nota >= 5.0:
    print(f'Recuperação, nota: {nota}.')
else:
    print(f'Reprovado, nota: {nota}.')
