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
def adicionar_tarefa(titulo, projeto, responsavel, status, prazo):
    tarefas = carregar_tarefas()
    tarefa = {
        "titulo": titulo,
        "projeto": projeto,
        "responsavel": responsavel,
        "status": status,
        "prazo": prazo
        }
    tarefas.append(tarefa)
    atualizar_tarefas(tarefas)