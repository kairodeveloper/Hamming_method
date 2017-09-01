#_*_ coding: utf-8 _*_

from app import operacoesBinarias
from app import hamming

def mensagem(tipo):

    if(tipo==1):
        return("Qual a sequencia a ser enviada?\n>> ")

    elif(tipo==2):
        return("Qual a sequencia a ser recebida?\n>> ")

def main():
    try:
        tipo = int(input("Insira:\n1 - Para enviar\n2 - Para receber\n>> "))

        if(tipo!=1 and tipo!=2):
            print("\nOpcao invalida!")

        else:
            sequencia = input(mensagem(tipo))

            if(operacoesBinarias.somente_0_1(sequencia)):

                if(tipo==1):
                    print(hamming.enviar(sequencia))
                elif(tipo==2):
                    print(hamming.receber(sequencia))

                else:
                    print("Opcao Invalida!")

            else:
                print("\nSequencia introduzida eh invalida!")

    except Exception:
        print("\nOpcao invalida!")


if __name__=="__main__":
    main()