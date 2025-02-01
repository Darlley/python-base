#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python
"""Bloco de notas

Para escrever uma nova nota:

$ notes.py new "Titulo da Nota"
$ tag: tech
$ text: Conteúdo

Para listar as notas

$ notes.py read --tag=tech
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notas.txt")

cmds = ("read", "new")
arguments = sys.argv[1:]

if not arguments:
  print("Invalid usage")
  print(f"You must specify subcommand {cmds}")
  sys.exit(1)

if arguments[0] not in cmds:
  print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
  # leitura de nota
  notes_dir = os.path.join(path, "anotacoes")
  
  # Lista os arquivos do diretório
  arquivos = os.listdir(notes_dir)
  
  # Mostra os arquivos numerados
  for i, arquivo in enumerate(arquivos, 1):
    print(f"{i}. {arquivo}")
  
  # Solicita qual arquivo abrir
  numero = int(input("\nQual nota você quer ler? Digite o número: "))
  
  if 1 <= numero <= len(arquivos):
    arquivo_selecionado = arquivos[numero-1]
    caminho_arquivo = os.path.join(notes_dir, arquivo_selecionado)
    
    # Lê e exibe o conteúdo do arquivo
    with open(caminho_arquivo, "r") as arquivo:
      print("-"*40)
      print("\n" + arquivo.read())
  else:
    print("Número inválido!")

if arguments[0] == "new":
  title = arguments[1]
  tag = input("Nome da tag: ").strip()
  text = input("Escreva sua nota:\n").strip()
  content = f"TÍTULO: {title}\nTAG: {tag}\n\n{text}"
  
  # Cria diretório de anotações se não existir
  notes_dir = os.path.join(path, "anotacoes")
  os.makedirs(notes_dir, exist_ok=True)
  
  # Cria arquivo com nome da nota
  file_format_title = os.path.join(notes_dir, f"{title.lower().replace(" ", "-")}.txt")
  with open(file_format_title, "w") as file_:
    file_.write(content)