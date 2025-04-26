import os

def criar_pastas(base_path, pastas):
    for pasta in pastas:
        caminho = os.path.join(base_path, pasta)
        os.makedirs(caminho, exist_ok=True)
        print(f"Pasta criada: {caminho}")

if __name__ == "__main__":
    diretorio = input("Digite o caminho onde deseja criar as pastas: ")
    lista_pastas = ["Documentos", "Imagens", "Projetos", "Cursos", "Backup"]
    criar_pastas(diretorio, lista_pastas)
