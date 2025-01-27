hep() mostra detalhes do metodo

## TIPOS PRIMITIVOS

1. int - tipo não iterável. Exemplo: 42
2. float - tipo não iterável. Exemplo: 3.14
3. str - tipo iterável. Exemplo: "texto"
4. bool - tipo não iterável. Exemplo: True
5. tuple - tipo imutável iterável. Exemplo: ("valor1", "valor2") 
6. list - tipo mutável iterável. Exemplo: ["item1", "item2"]
7. set - tipo mutável iterável. Exemplo: {1, 2, 3} ou set({1, 2, 3})
8. dict - tipo mutável iterável. Exemplo: {"chave": "valor"} ou dict({"chave": "valor"})
9. None - tipo não iterável. Exemplo: None

## SET E CONJUNTOS

- set()
- aceita qualquer iteravel: set("string"), set(["array"]), set(("tupla"))
- | (união/interpolação): junta todos os valores de forma sequencial sem repetições: conjunto_x | conjunto_y
- & (interseção): retorna apenas os elementos em comum entre os conjuntos: conjunto_x & conjunto_y
- - (diferença): retorna elementos do primeiro conjunto que não estão no segundo: conjunto_x - conjunto_y
- ^ (diferença simétrica): retorna elementos que estão em um conjunto ou outro, mas não em ambos: conjunto_x ^ conjunto_y
- <= (subconjunto): verifica se um conjunto está contido em outro: conjunto_x <= conjunto_y
- >= (superconjunto): verifica se um conjunto contém outro: conjunto_x >= conjunto_y
- set().add(valor)
- Hash Table: Estrutura de dados que otimiza buscas. Enquanto a busca em arrays (value in array) tem complexidade O(n) pois precisa iterar toda a lista, o set implementa uma hash table com complexidade O(1), acessando diretamente o endereço de memória.

## Dicionário

- dict({ key: value }) ou simplesmente { key: value }
- exemplos: 
  { "key": "value" }
  { "key": 123 }
  { 0: 123 }
  { 0: "value" }
- Percorrer uma tupla ou array é O(n) mas o dicionário é O(1)
- da para usar ("value" in dicionario) para retornar um booleano
- acessa o valor diretamente usando variavel["chave"]
- união de dicionarios: 
  1. dicionario.upadate(outro_dicionario)
  2. { **dicionario, **outro_dicionario }
- acessar valores:
  1. dicionario["chave"]
  2. dicionario.get("chave") se não tiver passa um valor default como segundo parametro.

## SYS MÓDULO DE MÉTODO DO SISTEMA DE I/O (print e input)

- import sys
- dir(sys) para ver todos os metodos
- sys.platform mostra o SO do usuário
type(sys.stdou) = IO
- sys.stdout é um objeto IO, espera um texto e se comporta como um arquivo
  - sys.stdout.write() é o método abstraido de print()
  - print("example", file=open("hello.txt", "a")) Abre o arquivo e faz append do conteúdo.~
    - tail -f hello.txt para ficar monitorando o novo arquivo
- sys.stdin é um objeto IO, le um texto
  - sys.stdin.read() é o método abstraido de input()
  - raramente se usa o input (jogos de terminal, softwares dedicado, testes)
- sys.argv recupera os argumentos do terminal
  - python hello.py --lang="PT_BR"            retorna ['hello.py', '--lang=PT_BR']

env | grep 