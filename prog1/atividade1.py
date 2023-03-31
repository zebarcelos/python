#Questao 1
x = int(input('Digite um numero: '))
y = int(input('Digite um numero: '))
def desenhaLinha(x, y):
    # código para desenhar a linha com os parâmetros x e y
    print(f"Desenhando linha com os pontos {y} e {x}")
desenhaLinha(x, y) # chamada correta da função com os argumentos passados
#não é necessario o comando print para chamar uma função DEF já criada acima'''
#Questao 2
z = 50
while (z != 10):
    if (z > 10):
        z = z-1
    else:
        z= z+1 
print(z)
#Questao 3
sexo = input('Qual o seu sexo: ')
if(sexo == 'F' and sexo =='f'):
    print('Sexo feminino!')
elif(sexo =='M' and sexo == 'm'):
    print("Sexo masculino!")
else:
    print('Sexo inválido!')
#Questao 6
x = "Até a pé nós iremos"
for i in x:
    print(i)
