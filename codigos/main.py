from ui import *
from storage import *
from models import *
from services import *
from utils import *

import os, sys, json, time

while True:
    usuarios = carregar_usuarios()
    os.system("cls")
    menu_inicio()
    opcao_menu = input("")
    if opcao_menu not in ["1", "2", "3"]:
        sys.exit("Opção inválida!")
        time.sleep(1)
        continue
    elif opcao_menu == "1":
        #Usuario
        while True:
            usuarios = carregar_usuarios()
            menu_usuarios()
            opcao_usuario = input("")
            if opcao_usuario not in ["0", "1", "2", "3", "4", "5"]:
                continue
            if opcao_usuario == "0":
                break
            elif opcao_usuario == "1":
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
            elif opcao_usuario == "2":
                #listar
                listar_usuarios(usuarios)
                input()
                break
            elif opcao_usuario == "3":
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
                    condicao = True
                    for indice, usuario in enumerate(usuarios):
                        if nome == usuario["nome"]:
                            indices.append(indice)
                            condicao = False
                    if condicao:
                        print("usuário não encontrado!")
                        time.sleep(1)
                        break
                    mostrar_usuarios(indices, usuarios)
                    input()
                    break
                else:
                    print("usuário não encontrado!")
                    time.sleep(1)
                    break
            elif opcao_usuario == "4":
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
                    nome = usuarios[indice]["nome"]
                email = input("novo email: ")
                for usuario in usuarios:
                    if email == usuario["email"]:
                        print("email já cadastrado!")
                        break
                if email == "":
                    email = usuarios[indice]["email"]
                perfil = input("novo perfil: ")
                if perfil == "":
                    perfil = usuarios[indice]["perfil"]
                atualizar_usuario(indice, nome, email, perfil)
                print("atualizado!")
                time.sleep(1)
            elif opcao_usuario == "5":
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
    elif opcao_menu == "2":
        print("Você escolheu Projetos!")
        time.sleep(1)
        while True:
            #Projetos
            menu_projetos()
            opcao_projetos = input("")
            if opcao_projetos not in ["0", "1", "2", "3", "4", "5"]:
                continue
            if opcao_projetos == "0":
                break
            elif opcao_projetos == "1":
                #Cadastrar projeto(Não funciona ainda!)
                nome_projeto = input("nome do projeto: ")
                if nome_projeto == "":
                    print("nome do projeto não pode ser vazio!")
                    time.sleep(1)
                    continue
                if nome_projeto == projeto["nome"]:
                    print("Já existe um projeto com este nome!")
                    time.sleep(1)
                    break
                descricao = input("descrição: ")
                inicio = input("Digite a data de início(AA/MM/DD):")
                fim = input("Digite a data de encerramento(AA/MM/DD):")
                break
            elif opcao_projetos == "2":
                #listar projetos
                print("Tem que criar o dicionário ainda")
            elif opcao_projetos == "3":
                #buscar projeto
                print("Tem que criar o dicionário ainda")
            elif opcao_projetos == "4":
                #atualizar projeto
                print("Tem que criar o dicionário ainda")
            elif opcao_projetos == "5":
                #remover projetos
                print("Tem que criar o dicionário ainda")
    elif opcao_menu == "3":
        print("Você escolheu Tarefas!")
        while True:
            menu_tarefas()
            opcao_tarefas = input()
            if opcao_tarefas not in ["0", "1", "3", "4"]:
                print("Opção inválida!")
                time.sleep(1)
                continue
            if opcao_tarefas == "0":
                break
            if  opcao_tarefas == "1":
                titulo_tarefa = input("nome: ")
                if titulo_tarefa == "":
                    print("o título não deve ser vazio!")
                    time.sleep(1)
                    break
                projeto_tarefa = input("projeto: ")


                responsavel_tarefa = input("responsável: ")
                if responsavel_tarefa == "":
                    print("a tarefa deve ter um responsável!")
                    time.sleep(1)
                    break
                status_tarefa = padronizar_texto(input("status: "))
                if status_tarefa not in ["pendente", "em andamento", "concluida"]:
                    print("status inválido!")
                    time.sleep(1)
                    break
                print("ex: YYYY-MM-DD")
                prazo_tarefa = input("prazo: ")
                if not data_valida(prazo_tarefa):
                    print("data inválida")
                    time.sleep(1)
                    break
                adicionar_tarefa(titulo_tarefa, projeto_tarefa, responsavel_tarefa, status_tarefa, prazo_tarefa)
                print("Tarefa adicionada!")
                time.sleep(1)
                break
