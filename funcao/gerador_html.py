def tag_boco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    #testes (assertions)
    assert tag_boco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'
    assert tag_boco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'
    print(tag_boco('bloco'))
