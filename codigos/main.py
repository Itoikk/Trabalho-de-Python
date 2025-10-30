from utils import *
import time
import os
lista = []
while 1:
    os.system("cls")
    inicio()
    opcao = input()
    if opcao == "1":
        os.system("cls")
        usuarios()
        opcao_nsei = input()
        if opcao_nsei == "0":
            continue
        elif opcao_nsei == "1":
            nome = input("nome: ")
            if nome == "":
                print("nome não deve ser vazio!")
                time.sleep(1)
                continue
            email = input("email: ")
            #Criar uma verificação do email se já existe!
            perfil = input("perfil: ")
            lista.append(cadastrar_usuario(nome, email, perfil))
            print("Contato adicionado!")
            time.sleep(1)
        elif opcao_nsei == "2":
            if lista == []:
                print("Nenhum usuario adicionado!")
            
            else:
                listar_usuarios(lista)
                time.sleep(3)
        elif opcao_nsei == "3":
            nome = input("Digite o nome: ")
            for dicionario in lista:
                if nome == dicionario["nome"]:
                    print(f"nome: {dicionario["nome"]}")
                    print(f"email: {dicionario["email"]}")
                    print(f"perfil: {dicionario["perfil"]}")
                    time.sleep(3)
                    continue
                else:
                    email = input("email: ")
                    for dicionario in lista:
                        if email == dicionario["email"]:
                            print(f"nome: {dicionario["nome"]}")
                            print(f"email: {dicionario["email"]}")
                            print(f"perfil: {dicionario["perfil"]}")
                            time.sleep(3)
                            continue
    elif opcao == "2":
        print("Você escolheu Projetos")
    elif opcao == "3":
        print("Você escolheu Tarefas")
    
    else:
        print("Opção inválida!")
        time.sleep(1)
        continue

    