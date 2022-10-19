'''
Q1 Quais são os dados de entrada?
Velocidade do carro

Q2 O que devo fazer com estes dados?
Analisar a velocidade, e exibir se houve multa, multa leve, meédia ou grave

Q3 Quais são as restrições desse problema?

Q4 Qual o resultado esperado?
Exibir a mensagem que corresponde com o nível da multa que a pessao levou 

Q5 Qual a sequência de passos para chegar no resultado esperado?

input velocidade_atual
velocidade_maxima = 80
if velocidade_atual < velocidade_maxima = Não levou multa

'''

velocidade_atual = int(input("Qual a velocidade atual?  "))
velocidade_maxima = 80
if velocidade_atual <= velocidade_maxima:
    print("Não houve multa por excesso de velocidade")
elif velocidade_atual > velocidade_maxima and velocidade_atual <= velocidade_maxima + 10:
    print("Multa leve por excesso de velocidade")
elif velocidade_atual >= velocidade_maxima + 11 and velocidade_atual <= velocidade_maxima +20:
    print("Multa média por excesso de velocidade")
elif velocidade_atual > velocidade_maxima + 20:
    print("Multa gravíssima por excesso de velocidade")

#*******************
#Modificando branch - teste github