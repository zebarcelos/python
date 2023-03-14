#Exercicio 1
nome = input('Qual o seu nome?')
print("Seu nome é", nome)


#Exercicio 2 
nome = input('Qual o seu nome?')
idade = input('Quantos anos você tem?')
print('Seu nome é', nome, 'e você tem', idade, 'anos')


#Exercicio 3
nome = input('Qual o seu nome?')
print('O seu nome é', nome)
altura = float(input('Qual a sua altura?'))
print('Você tem', altura , 'metros de altura')
print('Obrigado pela sua participação!')
print('Infelizmente sua altura de', altura, 'não é suficiente para buscar manga com a mão!')


#Exercicio 4
print('Precisamos saber o seu endereço!')
cep = int(input('Por favor, infome-nos o seu CEP? '))
if cep == int("91180001"):
    rua = ('AV. Baltazar de oliveira Garcia')
    print('Certo, você mora na AV. Baltazar de oliveira Garcia')
else:
    rua = str(input('Não consegui localizar, favor insira o nome da sua rua - '))
numero = int(input('Favor, preencha o seu número - '))
estado = str(input('Em qual estado você reside? '))
if estado == str('RS'):
    print('País - Brasil')
else:
    print('Estrangeiro')
print('Certo, então você reside na rua',rua,'numero -',numero, '- no estado do',estado)


#Exercício 5
print('Vamos agora pedir alguns números para você!')
n1 = int(input('Por favor, insira um número - '))
n2 = int(input('Por favor, insira mais um número inteiro - '))
n3 = int(input('Por favor, insira mais um número inteiro - '))
n4 = int(input('Por favor, insira mais um número inteiro - '))
n5 = int(input('Por favor, insira mais um número inteiro - '))
resultadodasoma = n1+n2+n3+n4+n5
resultadodamult = n1*n2*n3*n4*n5
print('Certo, a soma dos números depósitadas é:')
print(resultadodasoma)
print('Você gostaria de saber a multiplicação desses números? ')
pergunta1 = int(input('[1] Sim\n'
      '[2] Não\n'
      ''))
if pergunta1 == 1:
    print('Certo, o resultado é',resultadodamult)
else:
    print('Bom, de qualquer forma o resultado é',resultadodamult)


#Exerício 6
print('Agora vamos pegar alguns outros números')
A = int(input('Insira mais um número - '))
B = int(input('Insira mais um número - '))
C = int(input('Insira mais um número - '))
D = int(input('Insira mais um número - '))
E = int(input('Insira mais um número - '))
areadotriangulo = B*C/2
Pdretangulo = 2*(A+D)
adcirculo = 3.14*(E**2)
print('O tamanho do seu triangulo é',areadotriangulo)
print('O perímetro do retângulo é', Pdretangulo)
print('O área do circulo é', adcirculo)


#Exercicio 7
print('Vamos ver o resultado das suas avaliações')
nomedalenda = input(str('Mas antes, qual o seu nome? ')).upper()
if nomedalenda == 'JOSÉ' or nomedalenda =='JOSE':
    print('Ah sim kk boa sorte')
else: 
    print('Certo, vamos nessa!')
trabalho = float(input(('Qual a nota do seu trabalho? ')))
prova = float(input(('Qual a nota da sua prova? ')))
teste = float(input(('E a nota do seu teste? ')))
nftrab = trabalho*0.10
nfprova = prova*0.60
nfteste = teste*0.30
nftotal = nftrab+nfteste+nfprova
print('Sua nota no final é de', nftotal)
if nftotal >= 6 and nftotal < 10:
    print('Parabéns, você foi aprovado!')
elif nftotal >= 10:
    print('NOSSA! VOCÊ TIROU ',nftotal,'! MEUS PARABÉNS!', sep= '')
else:
    print('Você foi reprovado, infelizmente!')