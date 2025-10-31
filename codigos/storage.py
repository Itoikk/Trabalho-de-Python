import json
import os
ARQUIVO = "codigos/data/usuarios.json"
usuarios = []

def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        print("erro foi aq")
        return []
    try:
        with open(ARQUIVO, "r", encoding = "utf-8") as f:
            usuarios = json.load(f)
            return usuarios
    except json.JSONDecodeError:
        return []
    
def atualizar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding = "utf-8") as f:
        json.dump(usuarios, f, indent = 4, ensure_ascii = False)

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