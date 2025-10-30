from ui import *
import os, sys, json, time
from storage import carregar_usuarios, adicionar_usuario, remover_usuario
while True:
    usuarios = carregar_usuarios()
    os.system("cls")
    menu_inicio()
    opcao = input("")
    if opcao not in ["1", "2", "3"]:
        sys.exit("Opção inválida!")
    elif opcao == "1":
        #Usuario
        while True:
            menu_usuarios()
            opcao = input("")
            if opcao not in ["0", "1", "2", "3", "4"]:
                continue
            if opcao == "0":
                break
            elif opcao == "1":
                #CADASTRAR
                nome = input("nome: ")
                if nome == "":
                        print("nome não pode ser vazio!")
                        time.sleep(1)
                        continue
                email = input("email: ")
                for usuario in usuarios:
                    if usuario["email"] == email:
                        print("email já cadastrado!")
                        time.sleep(1)
                        break
                else:
                    perfil = input("perfil: ")
                    if perfil == "":
                        adicionar_usuario(nome, email)
                    else:
                        adicionar_usuario(nome, email, perfil)
                    print("Usuario Adicionado!")
                    time.sleep(1)
                    break
            elif opcao == "2":
                #listar
                print()
            elif opcao == "3":
                #atualizar
                print()
            elif opcao == "4":
                email = input("email: ")
                for indice, usuario in enumerate(usuarios):
                    if usuario["email"] == email:
                        remover_usuario(indice)
                        print("usuário removido!")
                        time.sleep(1)
                        break

                else:
                    print("email não cadastrado!")
                    time.sleep(1)
                break

                
    elif opcao == "2":
        print("Você escolheu Projetos!")
    elif opcao == "3":
        print("Você escolheu Tarefas!")
