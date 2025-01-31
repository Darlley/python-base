"""Execute:
$ python interpolacao3.py emails.txt email_tmpl.txt
"""
import os
import sys

arguments = sys.argv[1:]
print(arguments)
if not arguments:
  print("Informe o nome do arquivo de emails formatado (nome, email)")
  sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)
template = open(templatepath, encoding="utf-8").read()

for line in open(filepath):
  name, email = line.split(",")

  print(f"Enviando email para {email}\n")
  print(
    template.format(
      nome=name,
      produto="caneta",
      problema="escrever muito bem", 
      link="https://google.com", 
      quantidade=1,
      promocao=50.5
    )
  )
  print("\n" + ("-"*30) + "\n")