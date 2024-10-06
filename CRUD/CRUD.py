import os
import time

lista = []

def limparTela():
    input("Digite qualquer tecla e enter para voltar ao menu: ")
    os.system("cls")


def create():
    print("Você escolheu CREATE")
    lista.append(input("Digite um nome: "))


def read():
    print("Você escolheu READ")
    for i, j in enumerate(lista):
        print(f"Indice [{i}] nome: {j}")
        

def update():
    print("Você escolheu UPDATE")
    indice = int(input("Digite um indice para fazer o update: "))
    if 0 <= indice <= (len(lista) - 1):  
        novoNome = input("Digite um novo nome: ")
        lista[indice] = novoNome
    else:
        print("indice não encontrado")   


def delete():
    print("Você escolheu DELETE")
    indice = int(input("Digite um indice para fazer o delete: "))
    if 0 <= indice <= (len(lista) - 1):
        print("Nome deletado com sucesso")
        lista.pop(indice)
    else:
        print("indice não encontrado")   


def sair():
    os.system("cls")
    mensagem = "Saindo da operação"
    for i in range(4): 
        print(f"\r{mensagem}{'.' * i}", end='', flush=True)
        time.sleep(0.5)

def main():
    while True:
        print("""
Digite 1 para CREATE
Digite 2 para READ
Digite 3 para UPDATE
Digite 4 para DELETE
Digite 0 para encerrar a operação""")
        op = int(input("Digite sua opção: "))

        match op:
            case 0:
                sair()
                break
            
            case 1:
                create()
                
            case 2:
                read()
            
            case 3:            
                update()          
                        
            case 4:
                delete()  
            
            case _:
                print("Opção invalida!!")

        limparTela()          


if __name__ == "__main__":
    main()