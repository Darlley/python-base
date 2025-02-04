#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python
"""
A forma correta de tratar erros sem cair em race condition:

EAFP - Easy to Ask Forgiveness than permission
É mais facil perdir perdão (except) do que permissão (if)

except = Bare Except
qualquer erro que acorre dentro do broco do try é capturado no except
por isso deve ser documentado um except para cada erro diferente que pode vir acontecer
Lide com erros individualmente != bare except

Também conseguimos capturar a mensagem tipo do erro 

Conseguimos forçar que um erro ocorra com raise + classe de erro 
"""
__version__ = "0.1.0"

import sys


try:
  raise RuntimeError("Ocorreu um erro")
except Exception as e:
  print(str(e))


try:
  names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
  print(f"[Error] {str(e)}.")
  sys.exit(1)
  # TODO: Usar p retry
else:
  print("Não aconteceu nenhum erro")
finally:
  print("De qualquer forma executa o finally")

try:
  print(names[2])
except:
  print("[Error] Missing name in the list")
  sys.exit(1)