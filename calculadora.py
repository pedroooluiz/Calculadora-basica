def CalculadoraBasica():
  lista = ['+', '-', '/', '*', '//', '%', 'exp', '**']
  continuar = 's'
  
  while continuar == 's':
    try:
      print("""Digite uma das operações: 
            + (soma), 
            / (divisão), 
            * (multiplicação), 
            - (subtração), 
            // (quociente), 
            % (resto da divisão), 
            **(raiz quadrada de a e b), 
            exp(expoente a sobre b): """)
      Calculadora = str(input('Escolha uma das operações: ')).strip()
      if Calculadora in lista:
        a = float(input('Digite o primeiro numero: '))
        b = float(input('Digite o segundo numero: '))
      if Calculadora == '+':
        operacao = a + b
        print(operacao)  
      elif Calculadora == '-':
        operacao = a - b
        print(operacao) 
      elif Calculadora == '/':
        operacao = a / b
        print(operacao) 
      elif Calculadora == '*':
        operacao = a * b
        print(operacao) 
      elif Calculadora == '//':
        operacao = a // b
        print(operacao)
      elif Calculadora == '%':
        operacao = a % b
        print(operacao)
      elif Calculadora == 'exp':
        operacao = a ^ b
        print(operacao)
      elif Calculadora == '**':
        operacao1 = pow(a)
        operacao2 = pow(b)
        print(operacao1)
        print(operacao2)
      else:
        print('Digite uma das operações.')
        continuar = str(input('Deseja continuar? (S/N)       ')).strip().lower()
      continuar = str(input('Deseja continuar? (S/N): ')).strip().lower()
    except:
      continuar = str(input('Deseja continuar? (S/N): ')).strip().lower()
CalculadoraBasica()
print('Obrigado por utilizar o nosso sistema.')
