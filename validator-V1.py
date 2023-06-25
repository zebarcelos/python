import pandas as pd
import os

def clear():
    os.system('cls')

df = pd.read_html('https://www.apimec.com.br/certificacao/profissionais-certificados-cnpi/')[0]
certificados = list(df['Certificado Nº.1'])
print('Bem vindo ao validador de Certificado CNPI')
while True:
    dignummber = input(str('Número consultado: '))

    if dignummber in certificados:
        clear()
        print('Código CNPI Válido!')
    else:
        clear()
        print('Não válido!')