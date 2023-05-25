import os
import pdb
import random

scorePLAYER = 0 
scoreCPU = 0
scoredraw = 0

#DEFF PLACES 

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

'''def scoreboard():
    print("============")
    print(f'Pontos de {nickname}: {scorePLAYER}')
    print(f'Pontos da CPU: {scoreCPU}')
    print(f'Rounds empatados: {scoredraw}')
    print("============")'''

def playerplay():
    if playermove == 1:
        print("Você escolheu Pedra")
        print(f'A CPU escolheu {cpumove}')
    elif playermove == 2:
        print("Você escolheu Papel")
        print(f'A CPU escolheu {cpumove}')
    elif playermove == 3:
        print("Você escoleu Tesoura")
        print(f'A CPU escolheu {cpumove}')

def scoreboard():
        print("============")
        print(f'Pontos de {nickname}: {scorePLAYER}')
        print(f'Pontos da CPU: {scoreCPU}')
        print(f'Rounds empatados: {scoredraw}')
        print("============")
        
def cpuindentify():
    if cpumove == 1:
        print("A CPU escolheu Pedra!")
    elif cpumove == 2:
         print("A CPU escolheu Papel!")
    elif cpumove == 3:
         print("A CPU escolheu Tesoura!")

def pointsforplayer():
    global scorePLAYER
    if playermove == 1 and cpumove == 3:
         print(f"Ponto para {nickname}!")
         scorePLAYER = scorePLAYER + 1
    elif playermove == 2 and cpumove == 1:
         print(f"Ponto para {nickname}!")
         scorePLAYER = scorePLAYER + 1
         
    elif playermove == 3 and cpumove == 2:
         print(f"Ponto para {nickname}!")
         scorePLAYER = scorePLAYER + 1
    return scorePLAYER
         
def pointforCPU():
    global scoreCPU
    if cpumove == 1 and playermove == 3:
          print(f"Ponto para a CPU!")
          scoreCPU = + 1 

    elif cpumove == 2 and playermove == 1:
          print(f"Ponto para a CPU!")
          scoreCPU = + 1 

    elif cpumove == 3 and playermove == 2:
          print(f"Ponto para a CPU!")
          scoreCPU = + 1 
    return scoreCPU
def pointfordraw():
    global scoredraw
    if cpumove == playermove:
        print(f"Its a Draw, stand down!")
        scoredraw = scoredraw + 1

def initialmenu():
    global playermove
    global cpumove
    scoreboard()
    print("Qual jogada deseja fazer?")
    print("01 - Pedra | 02 - Papel | 03 - Tesoura")
    playermove = int(input())
    cpumove = random.randint(1,3)
    while playermove >3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção errada! Escolhe uma válida")
        playermove = int(input("01 - Pedra | 02 - Papel | 03 - Tesoura\n"))
    if playermove == 1:
        print("Você escolheu Pedra")
        cpuindentify()
        pointsforplayer()
        pointforCPU() 
        pointfordraw()

    elif playermove == 2:
        print("Você escolheu Papel")
        cpuindentify()
        pointsforplayer()
        pointforCPU() 
        pointfordraw()

    elif playermove == 3:
        print("Você escoleu Tesoura")
        cpuindentify()
        pointsforplayer()
        pointforCPU() 
        pointfordraw()

    else:
        while playermove != 1 or playermove != 2 or playermove != 3:
            print("Opção errada! Escolhe uma válida")
            playermove = input("01 - Pedra | 02 - Papel | 03 - Tesoura\n")

#END OF DEFF PLACES

print("============")
print("Boas vindas ao R.P.S")
print("============")
print("Faça seu loggin:")
nickname = input("Como gostaria de ser chamado?\n")

if nickname == None:
    print("Digite um nickname valido: ")
    nickname = input("Como gostaria de ser chamado?\n")
else:
    clearscreen()
    scoreboard()

print("Qual jogada deseja fazer?")
print("01 - Pedra | 02 - Papel | 03 - Tesoura")
playermove = int(input())
cpumove = random.randint(1,3)
while playermove >3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção errada! Escolhe uma válida")
        playermove = int(input("01 - Pedra | 02 - Papel | 03 - Tesoura\n"))
if playermove == 1:
        print("Você escolheu Pedra")
        cpuindentify()
        pointsforplayer()
        pointforCPU() 
        pointfordraw()

elif playermove == 2:
        print("Você escolheu Papel")
        cpuindentify()
        pointsforplayer()
        pointforCPU() 
        pointfordraw()

elif playermove == 3:
        print("Você escoleu Tesoura")
        cpuindentify()
        pointsforplayer()
        pointforCPU() 
        pointfordraw()

else:
    while playermove != 1 or playermove != 2 or playermove != 3:
        print("Opção errada! Escolhe uma válida")
        playermove = input("01 - Pedra | 02 - Papel | 03 - Tesoura\n")
scoreboard()
print("Você gostaria de continuar? \n")
willofplayer = int(input("01 - Continuar | [Qualquer botão] Encerrar\n"))
clearscreen()
while True:
    if willofplayer == 1:
         clearscreen()
         initialmenu()
         print("Você gostaria de continuar? \n")
         willofplayer = int(input("01 - Continuar | [Qualquer botão] Encerrar\n"))
         clearscreen()
         continue
    else:
         break


