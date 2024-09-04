livros = {
    'livro 1': {'titulo': 'a arte da guerra',  'autor': 'sun tzu',  'ano': 1500},
    'livro 2': {'titulo' : 'senhor dos aneis',  'autor': 'tolken',  'ano': 1954}
}

print(livros['livro 1'])

#acessar uma chave no dicionario interno
print(livros['livro 1']['titulo'])# não se muda chave

#como interar em um dicionario interno

for livro, detalhes in livros.items():
    print(f'titulo do {livro} : {detalhes['titulo']}')
    