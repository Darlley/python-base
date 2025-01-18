oferta = {
  "produto": "caneta",
  "problema": "escrever muito bem", 
  "link": "https://google.com", 
  "quantidade": 1,
  "promocao": 50.5
}

email_tmpl = """
Olá, %(nome)s 🍉

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(problema)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(promocao).2f
"""

for cliente in ["Naruto","Saitama","Goku"]:
  print(email_tmpl % {"nome": cliente, **oferta})