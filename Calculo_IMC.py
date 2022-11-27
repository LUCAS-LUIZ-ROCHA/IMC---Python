'''
Created on 11 de out. de 20
@author: LUCAS-LUIZ-ROCHA
'''
################### Entrada e tratamento de exceções.

quadro_atual=()
nome= input('Digite seu nome:') 

while True:
    try:
        peso= float(eval(input('Digite seu peso atual (Kg):')))
        break
    except:
        print('Digite um peso  invalido.')
        

while True:
    try:
        altura= float(eval(input('Digite sua altura:')))
        break
    except:
        print('Digite uma altura  invalido.')


################## Processamento.

imc= peso / altura**2
if(imc<18.5):
        quadro_atual= "desnutrição"
        
elif(imc<29.9):
        quadro_atual= "adequadro"
        
else:
        quadro_atual= "obesidade"
        
 
################## Saída.

print(f'{nome} o seu IMC é = {imc:.1f} e seu quadro atual é {quadro_atual}.')

    

