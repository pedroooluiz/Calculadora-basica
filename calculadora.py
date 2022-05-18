def Soma():
  a = float(input('Digite o primeiro numero: '))
  b = float(input('Digite o segundo numero: '))
  operacao = a + b
  print(operacao)  
def Subtracao():
  c = float(input('Digite o primeiro numero: '))
  d = float(input('Digite o segundo numero: '))
  operacao = c - d
  print(operacao)
def Divisao():
  e = float(input('Digite o primeiro numero: '))
  f = float(input('Digite o segundo numero: '))
  operacao = e / f
  print(operacao)
def Multiplicacao():
  g = float(input('Digite o primeiro numero: '))
  h = float(input('Digite o segundo numero: '))
  operacao = g * h
  print(operacao)
  
continuar = 's'

while continuar == 's':
  try:
    Calculadora = str(input('Digite a operação direto. Exemplo + (soma) e aperte enter, / (divisão) *(multiplicação) - (subtração): ')).strip()
  
    if Calculadora == '+':
      Soma()
    elif Calculadora == '-':
      Subtracao()
    elif Calculadora == '/':
      Divisao()
    elif Calculadora == '*':
      Multiplicacao()
    else:
      print('Digite uma das operações.')
    continuar = str(input('Deseja continuar? (S/N) ')).strip().lower()
  except:
    print('Precisa digitar uma das operações')


print('Obrigado por utilizar o nosso sistema.')
