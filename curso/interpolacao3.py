nome = "Naruto"
emoji = "1F916"
produto = "caneta"
problema = "escrever muito bem"
link = "https://unicode-explorer.com/emoji/robot"
quantidade = 1
promocao = 50.5

email_tmpl = f"""
Olá, {nome} \N{panda face}

Tem interesse em comprar uma {produto}?

Este produto é ótimo para resolver {problema}

Clique agora em {link}

Apenas {quantidade:03d} disponíveis!

Preço promocional {promocao:.2f}
"""

print(email_tmpl)