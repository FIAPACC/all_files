def calc(pU, fP, n):
  if n > 1:
    n = n/100

  potAt = pU/n
  potAp = potAt/fP
  potRe = (potAp**2 - potAt**2)**0.5

  return potAt, potAp, potRe

def organizedPrint(engineName, potAt, potAp, potRe):
  print(f'=-=- ENGINE {engineName} =-=-')

  print(f'Potencia Ativa: {potAt:.4f}')
  print(f'Potencia Aparente: {potAp:.4f}')
  print(f'Potencia Reativa: {potRe:.4f}\n')

# --------------------

print('-=Resultado dos calculos da atividade:=-')
organizedPrint(1, *calc(0.13, 0.58, 0.5))
organizedPrint(2, *calc(75, .85, 0.946))
organizedPrint(3, *calc(300, 0.89, 0.958))
organizedPrint(4, *calc(1.1, 0.75, .815))

# --------------------
print('\n-=Utilize seu próprio motor!=-\n')
while True:
  pU = input('Potência útil do motor em KW: ')
  fP = input('Fator de Potência do motor: ')
  n = input('Rendimento do motor: ')

  print('\n')
  organizedPrint('X', *calc(float(pU), float(fP), float(n)))
