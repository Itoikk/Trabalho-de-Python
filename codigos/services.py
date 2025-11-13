from models import *
from storage import *
from utils import *
def listar_usuarios(lista):
    for indice, usuario in enumerate(lista):
        print(f"nome: {lista[indice]["nome"]}")
        print(f"email: {lista[indice]["email"]}")
        print(f"função: {lista[indice]["perfil"]}")
        print()
        print()
def adicionar_usuario(nome, email, perfil = "user"):
    usuarios = carregar_usuarios()
    usuario = {
        "nome": nome,
        "email": email,
        "perfil": perfil
    }
    usuarios.append(usuario)
    atualizar_usuarios(usuarios)

def remover_usuario(indice):
    usuarios = carregar_usuarios()
    usuarios.pop(indice)
    atualizar_usuarios(usuarios)

def atualizar_usuario(indice, nome, email, perfil = "user"):
    usuarios = carregar_usuarios()
    usuario = {
        "nome": nome,
        "email": email,
        "perfil": perfil
    }
    usuarios[indice] = usuario
    atualizar_usuarios(usuarios)


def adicionar_projeto(nome, inicio, fim, descricao = "Descricao vazia"):
    projetos = carregar_projetos()
    projeto = {
        "nome": nome,
        "inicio": inicio,
        "fim": fim,
        "descricao": descricao
    }
    projetos.append(projeto)
    atualizar_projetos(projetos)


def atualizar_projeto(indice, nome, inicio, fim, descricao = "Descricao vazia"):
    projetos = carregar_projetos()
    projeto = {
        "nome": nome,
        "inicio": inicio,
        "fim": fim,
        "descicao": descricao
    }
    projetos[indice] = projeto
    atualizar_projetos(projetos)



def listar_projetos(lista):
    for indice, projeto in enumerate(lista):
        print(f"nome: {lista[indice]["nome"]}")
        print(f"inicio: {lista[indice]["inicio"]}")
        print(f"fim: {lista[indice]["fim"]}")
        print(f"descricao: {lista[indice]["descricao"]}")
        print()


def remover_projeto(indice):
    projetos = carregar_projetos()
    projetos.pop(indice)
    atualizar_projetos(projetos)