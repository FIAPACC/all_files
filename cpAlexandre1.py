value = float(input('Escreva um preço em reais: '))

print(f'Valor em Dolar: {(value * 0.17):.2f} \nValor em Euro: {(value * 0.15):.2f}')
print(f'Valor em Peso Argetino: {(value * 181.78):.2f} \nValor em Libra Esterlina: {(value * 0.13):.2f}')
print(f'Valor em Iene: {(value * 25):.2f}')

num = int(input('Digite um número inteiro: '))
u = 0
d = 0
c = 0

while num >= 100:
    c += 100
    num -= 100
while num >= 10:
    d += 10
    num -= 10
while num >= 1:
    u += 1
    num -= 1



print(c)
print(d)
print(u)
print('a')
