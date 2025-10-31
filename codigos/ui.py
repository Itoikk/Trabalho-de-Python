import os
def menu_inicio():
    print("================================")
    print("    Gerenciador de Projetos     ")
    print("================================")
    print("                                ")
    print("Opções:")
    print("1 - Usuários")
    print("2 - Projetos")
    print("3 - Tarefas")
def menu_usuarios():
    os.system("cls")
    print("Você escolheu Usuários!")
    print("Opções:")
    print("0 - Voltar")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar usuário")
    print("4 - Atualizar")
    print("5 - Remover")
def mostrar_usuarios(indices, usuarios):
    if indices == []:
        return
    for indice in indices:
        print()
        print("="*20)
        print(f"nome: {usuarios[indice]["nome"]}\nemail: {usuarios[indice]["email"]}\nperfil: {usuarios[indice]["perfil"]}")
        print("="*20)