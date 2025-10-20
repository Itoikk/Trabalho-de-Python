#serve para criar as funções auxiliares

def criar_usuario(nome, email, perfil):
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
    