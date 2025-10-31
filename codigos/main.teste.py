from ui import *
import os, sys, json, time
from storage import carregar_usuarios, adicionar_usuario, remover_usuario, atualizar_usuario
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
            usuarios = carregar_usuarios()
            menu_usuarios()
            opcao = input("")
            if opcao not in ["0", "1", "2", "3", "4", "5"]:
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
                indices = []
                email = input("email: ")
                if email != "":
                    for indice, usuario in enumerate(usuarios):
                        if email == usuario["email"]:
                            indices.append(indice)
                            mostrar_usuarios(indices, usuarios)
                            input()
                            break
                    else:
                        print("usuário não encontrado!")
                        time.sleep(1)
                        break
                    break
                nome = input("nome: ")
                if nome != "":
                    for indice, usuario in enumerate(usuarios):
                        if nome == usuario["nome"]:
                            indices.append(indice)
                            mostrar_usuarios(indices, usuarios)
                            input()
                            break
                    else:
                        print("usuário não encontrado!")
                        time.sleep(1)
                    break
                else:
                    print("usuário não encontrado!")
                    time.sleep(1)
                    break
            elif opcao == "4":
                #atualizar
                email = input("email: ")
                for index, usuario in enumerate(usuarios):
                    if usuario["email"] == email:
                        indice = index
                        break
                else:
                    print("email não encontrado")
                    time.sleep(1)
                    break
                nome = input("novo nome: ")
                if nome == "":
                    nome == usuarios[indice]["nome"]
                email = input("novo email: ")
                for usuario in usuarios:
                    if email == usuario["email"]:
                        print("email já cadastrado!")
                        break
                if email == "":
                    email = usuarios[indice]["email"]
                perfil = input("novo perfil: ")
                if perfil == "":
                    perfil = usuarios[indice][perfil]
                atualizar_usuario(indice, nome, email, perfil)
                print("atualizado!")
                time.sleep(1)
            elif opcao == "5":
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
