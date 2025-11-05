import json
import os
ARQUIVO = "codigos/data/usuarios.json"
usuarios = []

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