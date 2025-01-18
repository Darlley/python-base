oferta = {
  "produto": "caneta",
  "problema": "escrever muito bem", 
  "link": "https://google.com", 
  "quantidade": 1,
  "promocao": 50.5
}

email_tmpl = """
Olá, {nome} 🍉

Tem interesse em comprar {produto}?

Este produto é ótimo para resolver {problema}

Clique agora em {link}

Apenas {quantidade:03d} disponíveis!

Preço promocional {promocao:.2f}
"""

for cliente in ["Naruto","Saitama","Goku"]:
  print(email_tmpl.format(**oferta, nome=cliente))