"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
  1 x 1 = 1
  2 x 1 = 2
  3 x 3 = 3
  ...
############
Tabuada do 2
  2 x 1 = 2
  2 x 2 = 4
  2 x 3 = 6
  ...
############

"""
__version__ = "0.1.1"
__author__ = "Darlley"

template = """
--- Tabuada do {numero} ---
  
{operacoes}
#####################
"""


numbers = list(range(1,11))

# iterator (listas percorriveis)

for x in numbers:
  operacoes = ""

  for y in numbers:
    resultado = x * y
    operacoes += f"   {x} x {y:^6} = {resultado:^6}\n"
    
  print(template.format(numero=x, operacoes=operacoes))
