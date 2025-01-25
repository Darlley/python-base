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

current_language = os.getenv("LANG")[:5]

msg = dict({
  "en_US": "Hello, World!",
  "pt_BR": "Olá, mundo!"
})

  
print(msg[current_language]) # Imprime uma palavra em maisucula

