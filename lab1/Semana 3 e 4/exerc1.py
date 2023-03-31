#Exercicio 1
num1 = int(input('Diga um numero: '))
if num1%2 == 1:
    print("Seu número é Impar")
else:
    print('Seu número é Par') 
#Exercicio 2 
Numero1 = int(input('Digite um número: '))
Numero2 = int(input('Digite outro número: '))
if Numero1 > Numero2:
    print('O primeiro número é maior')
elif Numero1 < Numero2:
    print('O segundo número é maior')
else:
    print('Os dois números são iguais')
#Exercicio 3 
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
if b != 0:
    print(f"O resultado da divisão entre ambas é {a/b}")
else:
    print("ERRO - O número não pode ser 0")
#Exercicio 4
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite o último número: '))
if a <b and a< c:
    print(f"O número {a} é menor")
elif b <a and b <c:
    print(f'O número {b} é menor')
else:
    print(f'O número {c} é menor')
#Exercicio 5
preço = int(input('Digite o preço do produto: R$'))
if preço < 0 or preço == 0:
    print('Preço INVALIDO - Negativo ou Zerado!')
elif preço > 0 and preço <= 30:
    print('Preço Baixo, APROVEITE!')
elif preço > 30 and preço <= 50:
    print('Preço médio, recomendada revisão!')
else:
    print('Preço ALTO, não recomendada a compra!')
#Exercicio 6
price = int(input('Digite o preço de custo do seu produto: R$ '))
if price <= 0:
    print('ERRO - Valor inválido ou negativo')
elif price < 100:
    print(f"O valor de venda do seu produto deve ser de {price*1.10}")
elif price >= 100 and price < 300:
    print(f"O valor de venda do seu produto deve ser de {price*1.20}")
elif price >= 300 and price < 1000: 
    print(f"O valor de venda do seu produto deve ser de {price*1.50}")
else:
    print(f"O valor de venda do seu produto deve ser de {price*1.50}")
#Exercicio 7
ano = int(input('Digite o ano que deseja consultar: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano não é bissexto')
#Exercicio 8
num1 = float(input('Digite um número para calcular: '))
num2 = float(input('Digite outro número para calcular: '))
operacao = int(input('\nDigite 1 para somar dois valores'
                '\nDigite 2 para subtrair dois valores'
                '\nDigite 3 para multiplicar dois valores'
                '\nDigite 4 para dividir dois valores'
                '\nDigite 5 para realizar uma potência entre dois valores'
                '\nDigite 6 para realizar uma radiciação entre dois valores'
                '\nDigite qualquer outro número para sair'
                '\n: '))
if operacao == 1:
    print(f'O resultado é {num1 + num2}')
elif operacao == 2:
    print(f'O resultado é {num1 - num2}')
elif operacao == 3:
    print(f'O resultado é {num1 * num2}')
elif operacao == 4:
    print(f'O resultado é {num1 / num2}')
elif operacao == 5:
    print(f'O resultado é {num1 ** num2}')
elif operacao == 6:
    print(f'O resultado é {num1 ** (1/num2)}')
else:
    print('Você saiu')
#Exercicio 9
ga = float(input('Digite sua nota de Grau A: '))
gb = float(input('Digite sua nota de Grau B: '))
media = (ga+gb)/2
if media >= 7:
    print('Não será necessário o Grau C, você está aprovado!')
else:
    print(f'Sua média foi de {media}, sendo assim você precisa de {15-(ga+gb)} no Grau C para passar')
#Exercicio 10
letra = str(input('Digite uma letra: ').lower())
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('É uma vogal')
else:
    print('É uma consoante')

