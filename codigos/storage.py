import json
import os
ARQUIVO = "codigos/data/usuarios.json"
ARQUIVO2= "codigos/data/projetos.json"
usuarios = []
projetos= []

def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
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

carregar_usuarios()



def carregar_projetos():
    if not os.path.exists(ARQUIVO2):
        return []
    try:
        with open(ARQUIVO2, "r", encoding = "utf-8") as f:
            projetos = json.load(f)
            return projetos
    except json.JSONDecodeError:
        return []


def atualizar_projetos(projetos):
    with open(ARQUIVO2, "w", encoding = "utf-8") as f:
        json.dump(projetos, f, indent = 4, ensure_ascii = False)


carregar_projetos()