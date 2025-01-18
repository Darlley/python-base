#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequenta cada uma das atividades.
"""
__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Mario", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

aulas = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança", aula_danca)]

for atividade, aula in aulas:
  alunos_sala1 = []
  alunos_sala2 = []

  # complexidade O(n)
  for aluno in aula:
    if aluno in sala1:
      alunos_sala1.append(aluno)
    elif aluno in sala2:
      alunos_sala2.append(aluno)

  print(f"~ {atividade} " + ("-" * 60) + "\n")
  print(f"SALA 1: {alunos_sala1}")
  print(f"SALA 2: {alunos_sala2}\n")