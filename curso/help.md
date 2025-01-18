hep() mostra detalhes do metodo

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