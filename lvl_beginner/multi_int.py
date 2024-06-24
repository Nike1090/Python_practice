def generar_n_caracteres(quantity: int, string: str) -> str:
    return string * quantity


if __name__ == '__main__':
    print(generar_n_caracteres(5, 'x'))
    print(generar_n_caracteres(3, 'a'))
    print(generar_n_caracteres(2, 'n'))