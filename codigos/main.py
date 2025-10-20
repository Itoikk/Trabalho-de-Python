from utils import *
inicio()
opcao = input()
match opcao:
    case "1":
        print("Você escolheu Usuários")
    case "2":
        print("Você escolheu Projetos")
    case "3":
        print("Você escolheu Tarefas")
    case _:
        print("Opção inválida!")