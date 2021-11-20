fila = [];

def menu():
    print ("\n"+"MENU:".center(50,':'))
    opcao=int(input('''
1 - Incluir
2 - Excluir
3 - Consultar
0 - Sair 
Escolha:  '''))

    if opcao == 1:
        incluir(fila)
    elif opcao == 2:
        excluir(fila)
    elif opcao == 3:
        consultar(fila)
    elif opcao == 0:
        exit()
    else:
        print("Alternativa inválida!\nTente novamente.")
        menu()
    
def incluir(fila):
    incluir = input("Digite um elemento para incluir: ")
    fila.append(incluir)
    print("Elemento "+incluir+" incluído à fila")

def excluir(fila):
    fila.pop(0)
    print("Primeiro elemento removido da fila!")

def consultar(fila):
    print ("\n"+"CONSULTAR:".center(50,':'))
    opcao=int(input('''
    1 - Primeiro elemento
    2 - Último elemento
    3 - Quantidade de elementos
    4 - Fila
    0 - Voltar ao menu principal 
    Escolha:  '''))

    if opcao == 1:
        print(fila[0])
    elif opcao == 2:
        i = len(fila)-1
        print(fila[i])
    elif opcao == 3:
        print(len(fila))
    elif opcao == 4:
        print(fila)
    elif opcao == 0:
        menu()
    else:
        print("Alternativa inválida!\nTente novamente.")
        consultar()

while True:
        menu()
