#_*_ coding: utf-8 _*_

from app.operacoesBinarias import *

#converte a sequencia(String) para vetor
def string_to_vetor(string):
    vetor=[]

    for i in string:
        vetor.append(i)

    return vetor

#converte o vetor da sequencia para uma String
def vetor_to_string(vetor):
    word = ""

    for i in vetor:
        word+=i

    return(word)

#verifica a paridade dos bits de paridade
def verifica_paridade_do_bit(bit, bits , sequencia_com_bits):

    matriz_bit_e_sua_paridade = []
    matriz_bit_de_paridade_e_suas_aparicoes = []

    #verifica e atribui um numero e seus respectivos bits de paridade (7 = 4+2+1) e os atribui a uma matriz
    for i in range(1, len(sequencia_com_bits)):
        if(i not in bits):
            vetor_modelo = []
            vetor_modelo.append(i)
            vetor_modelo.append(soma_numero(bits,i))

            matriz_bit_e_sua_paridade.append(vetor_modelo)

    #armazena em uma matriz os bits de paridade e suas aparicoes (1 = [3,5,7,9,11,13])
    for i in bits:
        bit_de_paridade = []
        bit_de_paridade.append(i)

        aparicao = []
        for k in matriz_bit_e_sua_paridade:
            if(i in k[1]):
                aparicao.append(k[0])

        bit_de_paridade.append(aparicao)

        matriz_bit_de_paridade_e_suas_aparicoes.append(bit_de_paridade)

    #separa em uma matriz os valores binarios (0 ou 1) de cada bit
    valor_bits_das_aparicoes = []
    for i in matriz_bit_de_paridade_e_suas_aparicoes:
        if(i[0]==bit):
            for k in i[1]:
                valor_bits_das_aparicoes.append(sequencia_com_bits[k])

    count=0
    for i in valor_bits_das_aparicoes:
        if(int(i)%2!=0):
            count+=1

    if(count%2==0):
        return True
    else:
        return False


#implementacao da funcao de enviar do metodo de hamming
#bit0 do 'sequencia_com_bits' sera ignorado durante toda a execucao
def enviar(sequencia):
    bits = verifica_numero_bits_paridade(sequencia)
    sequencia = string_to_vetor(sequencia)
    sequencia_com_bits = (len(sequencia)+len(bits)+1)*["0"]
    sequencia_com_bits[0]="-"

    pos=0
    for i in range(1,len(sequencia_com_bits)):

        if(i in bits):
            sequencia_com_bits[i]=" "

        else:
            sequencia_com_bits[i]=sequencia[pos]
            pos+=1


    for i in range(1,len(sequencia_com_bits)):
        if(i in bits):
            if(verifica_paridade_do_bit(i, bits, sequencia_com_bits)):
                sequencia_com_bits[i]="0"
            else:
                sequencia_com_bits[i]="1"

    return "\n"+str(vetor_to_string(sequencia_com_bits[1:len(sequencia_com_bits):1]))


#bit0 do 'sequencia_recebida' sera ignorado durante toda a execucao
def receber(sequencia_recebida):
    bits = verifica_numero_bits_paridade(sequencia_recebida)
    sequencia_recebida = string_to_vetor(sequencia_recebida)
    sequencia_recebida.insert(0,"-")
    erros = []

    for i in range(1,len(sequencia_recebida)):
        if(i in bits):
            if(verifica_paridade_do_bit(i,bits, sequencia_recebida)):
                x="0"
            else:
                x="1"

            if(x!=sequencia_recebida[i]):
                erros.append(i)

    if(len(erros)==0):
        return "Nenhum erro encontrado! Mensagem correta!"

    string = ""
    bit_de_erro = 0
    for i in range(len(erros)):
        if(i==len(erros)-1):
            bit_de_erro+=erros[i]
            string+=str(erros[i])+"."
        else:
            bit_de_erro += erros[i]
            string+=str(erros[i])+" "

    return "\nErros de paridade nos bits: "+string+"\nBit %s com erro: "%(str(bit_de_erro))

#print(enviar("1010"))
#print(receber("101110"))
#verifica_paridade_do_bit(1,[1,2,4], ["-"," "," ","1"," ","0","1","0"])