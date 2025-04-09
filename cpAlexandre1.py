#QUESTÃO 1
value = float(input('Escreva um preço em reais: '))

print(f'Valor em Dolar: {(value * 0.17):.2f} \nValor em Euro: {(value * 0.15):.2f}')
print(f'Valor em Peso Argetino: {(value * 181.78):.2f} \nValor em Libra Esterlina: {(value * 0.13):.2f}')
print(f'Valor em Iene: {(value * 25):.2f}')

#QUESTÃO 2
num = int(input('\nDigite um número inteiro(0-999): '))

c = (num // 100) * 100 if num >= 100 else 0
d = ((num % 100) // 10) * 10 if num >= 10 else 0
u = num % 10

print(f"Centena: {c}")
print(f"Dezena: {d}")
print(f"Unidade: {u}")

#QUESTÃO 3
y = int(input('\nVamos calcular, em dias, a sua idade.\nComesse dizendo quantos anos você tem:' ))
m = int(input('Agora, quantos meses inteiros se passaram depois do dia do seu último aniversário: '))
d = int(input('E por fim, quantos dias que se passaram desde a última vez que passou o dia(e somente o dia) do seu aniversário: '))

print('Sua idade em dias é de ' + str( y * 365 + m * 30 + d) + '.')

#QUESTÃO 4
d = int(input('Agora diga um número(dias) para ser convertido em anos, meses e dias: '))
y = d//365
m = (d - y * 365)//30
d = d - y * 365 - m * 30
print(f'Este número equivale a {y} ano(s), {m} mese(s) e {d} dia(s).')
