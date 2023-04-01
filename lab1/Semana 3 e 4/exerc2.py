#Exercicio 1 
'''print("Digite o nome de 13 pessoas:\n")
cont = 0 #contador de nomes digitados
while cont < 13:
  nome = input("Digite o nome da "+str(cont+1)+" pessoa: ")
  cont += 1'''
#Exercicio 2
'''num = 0
while num <= 1000:
  print(num)
  num += 1'''
#Exercicio 3
'''numeros = 0
while numeros <= 2000:
    print(numeros)
    numeros +=2'''
#Exercicio 4
'''nume = 1000
while nume >= 0:
    print(nume)
    nume -= 1'''
#Exercicio 5
'''cont = 0
contGremistas = 0
while cont < 10:
  time = input("Digite seu time: ")
  if time == "Gr�mio":
    contGremistas += 1
  cont += 1
print("Quantidade de gremistas:",contGremistas)'''
#Exercicio 6
'''cont = 0
while cont < 5:
    numdig = str(input('Digite os numeros: '))
    numeros = str(numdig + numdig * cont +'\n')
    cont += 1
print(str('\n' + numeros))'''
'''cont = 0
numeros = ""
while cont < 5:
  valor = float(input("Digite um valor com ponto flutuante:"))
  numeros = numeros + str(valor)+ "\n"
  cont += 1
print("Valores digitados:\n"+numeros)'''
#Exercicio 7
'''cont = 0
while cont < 10:
    num = int(input('Digite valores para somarmos: '))
    soma = num + num * cont
    cont+=1
print(soma)'''
#Exercicio 8
'''quant = int(input('Quantos números você deseja verificar? '))
while quant > 0:
    num = int(input('Diga o seu número: '))
    if num > 0:
        print('O número digitado é positivo')
    elif num == 0:
        print('O número é zero')
    else:
        print('O número é negativo')
    quant -= 1'''
#Exercicio 9
'''val1 = int(input('Digite um número: '))
val2 = int(input('Digite um segundo número: '))
while val1 > val2:
    numeros = val1 - 2
    val1 -=2
print(numeros) # INACABADO'''
#Exercicio 10
'''cont = 0
soma = 0
while cont <= 198:
  soma += cont
  cont += 1
print(soma)'''
#Exercicio 11
cont = int(input('Quantos numeros deseja testar: '))
numpar = 0
numimpar = 0
while cont != 0:
    numtest = int(input(' Digite então o seu número: '))
    if numtest%2 == 0:
        numpar += numtest 
    elif numtest%2 == 1:
        numimpar += numtest
    cont -= 1
print(numpar, numimpar)
