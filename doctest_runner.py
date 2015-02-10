if __name__ == "__main__":
    import doctest

    from sped import campos
    from sped import erros
    from sped import registros

    doctest.testmod(campos)
    doctest.testmod(erros)
    doctest.testmod(registros)
