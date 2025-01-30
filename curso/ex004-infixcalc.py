#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python

"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 5 2
10

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultado serão salvos em "infixcalc.log"
"""
__version__ = "0.1.0"

import os
import sys
from datetime import datetime

arguments = sys.argv[1:]

if len(arguments) != 3:
  # Modo interativo
  operation = input("Qual operação deseja realizar? (sum, sub, mul ou div) ")
  while operation not in ["sum", "sub", "mul", "div"]:
    print("Operação inválida. Use: sum, sub, mul ou div")
    operation = input("Qual operação deseja realizar? (sum, sub, mul ou div) ")

  while True:
    try:
      n1 = float(input("Digite o primeiro valor: "))
      break
    except ValueError:
      print("Valor inválido. Digite um número.")

  while True:
    try:
      n2 = float(input("Digite o segundo valor: "))
      break
    except ValueError:
      print("Valor inválido. Digite um número.")
else:
  # Modo linha de comando
  operation, *nums = arguments
  
  if operation not in ["sum", "sub", "mul", "div"]:
    print("Operação inválida. Use: sum, sub, mul ou div")
    sys.exit(1)
  
  try:
    n1 = float(nums[0])
    n2 = float(nums[1])
  except ValueError:
    print("Números inválidos")
    sys.exit(1)

# Realiza a operação
if operation == "sum":
  result = n1 + n2
elif operation == "sub":
  result = n1 - n2
elif operation == "mul":
  result = n1 * n2
elif operation == "div":
  if n2 == 0:
    print("Erro: Divisão por zero!")
    sys.exit(1)
  result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USERNAME", 'anonymous')

with open(filepath, "a") as file_:
  file_.write(f"{user} - {timestamp} > {n1}{'+' if operation == 'sum' else '-' if operation == 'sub' else '*' if operation == 'mul' else '/'}{n2} = {result} \n")

print(f"O resultado é: {result}")
