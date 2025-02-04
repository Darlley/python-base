#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python
"""
LBYL - Look Vefore You Leap (Olhe antes de atravessar)
Antes de tentar fazer a gente testa se é possível
não é perfeita, por que o tempo de execução de um programa não é constante
Porblema: RACE CONDITION o arquivo vai ficar executando mesmo que outro programa possa ter apagado o arquivo
"""
__version__ = "0.1.0"

import sys
import os

if os.path.exists("names.txt"):
  print("O arquivo existe")
  input("...")
  names = open("names.txt").readlines()

  if len(names) >= 2:
    print(names[2])
  else:
    print("[Error] Missing name in the list")
    sys.exit(1)
else:
  print("[Error] File names.txt not found")
  sys.exit(1)