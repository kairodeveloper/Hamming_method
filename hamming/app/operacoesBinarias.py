#_*_ coding: utf-8 _*_

#converte inteiro para o formato binario (String)
def converte_int_to_bin(numero):
    binario = ""
    while(numero>0):
        binario+=str(numero%2)
        numero=int(numero/2)

    return binario[::-1]

#verifica se o numero eh uma potencia de 2
def verifica_potencia(numero):
    condicao=0
    numero_binario = converte_int_to_bin(numero)
    for i in numero_binario:
        if(i=="1"):
            condicao+=1

    if(condicao==1):
        return True
    else:
        return False

#retorna os bits suficientes para a sequencia enviada
def verifica_numero_bits_paridade(sequencia):
    bits=[]
    tamanho = len(sequencia)
    for i in range(0,tamanho+1):
        if (verifica_potencia(i)):
            bits.append(i)

    return bits

#verifica se o numero eh realmente binario, sera usado no main, ao receber a sequencia, validando-a
def somente_0_1(sequencia):
    falhas = 0
    for i in sequencia:
        if(i!="0" and i!="1"):
            falhas+=1

    if(falhas>0):
        return False
    else:
        return True

#retorna os numeros (bits) que somados resultam naquele numero
def soma_numero(bits, numero):
    bits_resultantes=[]

    for i in range(len(bits)-1,-1,-1):
        if(numero>=bits[i]):
            numero-=bits[i]
            bits_resultantes.append(bits[i])

    return(bits_resultantes)
