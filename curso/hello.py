#!/c/Users/darll/AppData/Local/Microsoft/WindowsApps/python

""" This is multi-line commentary

Dependendo da lingua configurada no ambiente 
o programa exibe a mensagem correspondente.

Como usar:

Tenho a variavel LANG devidamente configrada ex:

  export LANG=pt_BR

Execução:

  python3 hello.py
  ou
  ./hello.py

"""

# convenção de uso de varaiveis com informações adicionais (metadados): Dunder == __
__version__ = "0.0.1" 
__author__ = "Darlley"
__license__ = "Unlicense"

import os
import sys

arguments = {
  "lang": None,
  "count": 1
}

for arg in sys.argv[1:]:
  try:
    key, value = arg.split("=")
  except ValueError as e:
    print(str(e))
    sys.exit(1)

  key = key.lstrip("-").strip()
  value = value.strip()
  if key not in arguments:
    print(f"Ivalid option argument{arg}")
    sys.exit()
  arguments[key] = value

current_language = arguments['lang']
if current_language is None:
  if "LANG" in os.environ:
    current_language = os.getenv("LANG")
  else:
    current_language = input("Choose a language: ")

current_language = current_language[:5] 

msg = dict({
  "en_US": "Hello, World!",
  "pt_BR": "Olá, mundo!"
})

print(f"{arguments["count"]}x: {msg[current_language] * int(arguments["count"])}")