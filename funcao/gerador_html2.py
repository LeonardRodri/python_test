def tag_boco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_boco('bloco'))
    print(tag_boco('inline e classe', 'info', True))
    print(tag_boco('inline', inline=True))
    print(tag_boco('Falhou', classe='error'))
    print(tag_boco(inline=True, texto='Ola texto'))
    print(tag_boco(inline=False, texto='Ola texto'))