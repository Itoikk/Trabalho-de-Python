#serve para criar as funções auxiliares

def cadastrar_usuario(nome, email, perfil):
    return {"nome": nome, "email": email, "perfil": perfil}


def inicio():
    print("================================")
    print("    Gerenciador de Projetos     ")
    print("================================")
    print("                                ")
    print("Opções:")
    print("1 - Usuários")
    print("2 - Projetos")
    print("3 - Tarefas")
def usuarios():
    print("Você escolheu Usuários!")
    print("Opções:")
    print("0 - Voltar")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Remover")
def listar_usuarios(lista):
    for indice, usuario in enumerate(lista):
        print(f"nome: {lista[indice]["nome"]}")
        print(f"email: {lista[indice]["email"]}")
        print(f"função: {lista[indice]["perfil"]}")
        print()
        print()
        