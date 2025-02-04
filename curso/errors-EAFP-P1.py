#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python
"""
A forma correta de tratar erros sem cair em race condition:

EAFP - Easy to Ask Forgiveness than permission
É mais facil perdir perdão (except) do que permissão (if)

except = Bare Except
qualquer erro que acorre dentro do broco do try é capturado no except
"""
__version__ = "0.1.0"

import sys

try:
  names = open("names.txt").readlines()
except:
  print("[Error] File names.txt not found")
  sys.exit(1)

try:
  print(names[2])
except:
  print("[Error] Missing name in the list")
  sys.exit(1)