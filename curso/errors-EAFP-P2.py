#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python
"""
A forma correta de tratar erros sem cair em race condition:

EAFP - Easy to Ask Forgiveness than permission
É mais facil perdir perdão (except) do que permissão (if)

except = Bare Except
qualquer erro que acorre dentro do broco do try é capturado no except
por isso deve ser documentado um except para cada erro diferente que pode vir acontecer
Lide com erros individualmente != bare except
"""
__version__ = "0.1.0"

import sys

try:
  names = open("names.txt").readlines() # FileNotFoundError
  1/1 # ZeroDivisionError
  print(names.banana) # AttributeError
except FileNotFoundError:
  print("[Error] File names.txt not found")
  sys.exit(1)
except ZeroDivisionError:
  print("[Error] You can't divide by zero!!!")
  sys.exit(1)
except AttributeError:
  print("[Error] List doesn't have banana!!!")
  sys.exit(1)

try:
  print(names[2])
except:
  print("[Error] Missing name in the list")
  sys.exit(1)