def cadastrar_usuario(nome, email, perfil):
    return {"nome": nome, "email": email, "perfil": perfil}
def listar_usuarios(lista):
    for indice, usuario in enumerate(lista):
        print(f"nome: {lista[indice]["nome"]}")
        print(f"email: {lista[indice]["email"]}")
        print(f"função: {lista[indice]["perfil"]}")
        print()
        print()
        