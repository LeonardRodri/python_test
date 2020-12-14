def tag_boco(conteudo,*args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not  callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_boco('bloco'))
    print(tag_boco('inline e classe', 'info', True))
    print(tag_boco('inline', inline=True))
    print(tag_boco('Falhou', classe='error'))
    print(tag_boco(inline=True, conteudo='Ola texto'))
    print(tag_boco(inline=False, conteudo='Ola texto'))
    print(tag_boco(tag_lista('Item1', 'Item2', 'Item3'), classe='info'))
    print(tag_boco(tag_lista,'sabado', 'domingo', classe='info', inline=True))