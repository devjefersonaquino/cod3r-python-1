a = 3
b = 4.4

print(a + b)

texto = 'Sua idade é...'
idade = 23
#print(texto + str(idade))
print(f'{texto} {idade}')

saudacao = 'bom dia '
print(3 * saudacao)

PI = 3.14
# PI = 3.1415
raio = float(input('Informe o raio da circunferencia: '))
# area = PI * raio * raio
area = PI * pow(raio, 2)

print(f' A area da circ é :  {area} m2.')
