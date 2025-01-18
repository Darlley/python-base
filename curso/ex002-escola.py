#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequenta cada uma das atividades.
"""
__version__ = "0.1.0"

sala1 = set(["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"])
sala2 = set(["Joao", "Antonio", "Carlos", "Mario", "Isolda"])

aula_ingles = set(["Erik", "Maia", "Joana", "Carlos", "Antonio"])
aula_musica = set(["Erik", "Carlos", "Maria"])
aula_danca = set(["Gustavo", "Sofia", "Joana", "Antonio"])

atividades = [  ("Inglês", aula_ingles), ("Música", aula_musica), ("Dança", aula_danca)  ]

for nome_atividade, alunos_atividade in atividades:
  # complexidade O(1)
  alunos_sala1 = sala1 & alunos_atividade
  alunos_sala2 = sala2 & alunos_atividade
  
  print(f"~ {nome_atividade} " + ("-" * 60) + "\n")
  print(f"SALA 1: {alunos_sala1}")
  print(f"SALA 2: {alunos_sala2}\n")