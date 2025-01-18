"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3...
-------------
Tabuada do 2
2
4
6...
-------------

"""
__version__ = "0.1.0"
__author__ = "Darlley"


numbers = list(range(1,11))

# iterator (listas percorriveis)

for x in numbers:
  print("Tabuada do", x)
  print("-" * 3)

  for y in numbers:
    print(x, "X", y, " = ", x*y)

  print("-" * 14)

