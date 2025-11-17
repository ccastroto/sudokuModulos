from src.checkCuadrado import checkCuadrado
from src.checkNumeroValido import checkNumeroValido
from src.checkFilas import checkFilas
from src.checkColumnas import checkColumnas

def checkSudoku(sudoku):
    return checkCuadrado(sudoku) and checkNumeroValido(sudoku) \
        and checkFilas(sudoku) and checkColumnas(sudoku)

if __name__ == '__main__':
    correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

    numero_repetido_fila_columna = [[1, 2, 3, 4],
                                    [2, 3, 1, 3],
                                    [3, 1, 2, 3],
                                    [4, 4, 4, 2]]

    numero_repetido_columna =   [[1, 2, 3],
                                [2, 3, 1],
                                [2, 3, 1]]

    numero_no_presente =    [[1, 2, 3, 4],
                            [2, 3, 1, 2],
                            [4, 1, 2, 3],
                            [2, 3, 1, 4]]

    numero_fuera_del_rango =    [[1, 2, 3, 4, 5],
                                [2, 3, 1, 5, 6],
                                [4, 5, 2, 1, 3],
                                [3, 4, 5, 2, 1],
                                [5, 6, 4, 3, 2]]
    
    caracteres = [['a', 'b', 'c'],
                ['b', 'c', 'a'],
                ['c', 'a', 'b']]

    numeros_reales =    [[1, 1.5],
                        [1.5, 1]]

    irregular_fila =    [[1, 2, 3],
                        [2, 3, 1]]

    irregular_columna = [[1, 2, 3],
                        [2, 3, 1],
                        [3, 1]]

    lista_vacia = [[]]

    # checkSudoku (conjunto de checkCuadrado, checkNumeroValido, checkFilas, checkColumnas)
    assert checkSudoku(correcto)
    assert not checkSudoku(numero_repetido_fila_columna)
    assert not checkSudoku(numero_repetido_columna)
    assert not checkSudoku(numero_no_presente)
    assert not checkSudoku(numero_fuera_del_rango)
    assert not checkSudoku(caracteres)
    assert not checkSudoku(numeros_reales)
    assert not checkSudoku(irregular_fila)
    assert not checkSudoku(irregular_columna)
    assert not checkSudoku(lista_vacia)

    #checkCuadrado:
    assert checkCuadrado(correcto)
    assert checkCuadrado(numero_repetido_fila_columna)
    assert checkCuadrado(numero_repetido_columna)
    assert checkCuadrado(numero_no_presente)
    assert checkCuadrado(numero_fuera_del_rango)
    assert checkCuadrado(caracteres)
    assert checkCuadrado(numeros_reales)
    assert not checkCuadrado(irregular_fila)
    assert not checkCuadrado(irregular_columna)
    assert not checkCuadrado(lista_vacia)

    #checkNumeroValido:
    assert checkNumeroValido(correcto)
    assert checkNumeroValido(numero_repetido_fila_columna)
    assert checkNumeroValido(numero_repetido_columna)
    assert checkNumeroValido(numero_no_presente)
    assert checkNumeroValido(numero_fuera_del_rango)
    assert not checkNumeroValido(caracteres)
    assert not checkNumeroValido(numeros_reales)
    assert checkNumeroValido(irregular_fila)
    assert checkNumeroValido(irregular_columna)
    assert checkNumeroValido(lista_vacia)

    #checkFilas
    assert checkFilas(correcto)
    assert not checkFilas(numero_repetido_fila_columna)
    assert checkFilas(numero_repetido_columna)
    assert not checkFilas(numero_no_presente)
    assert not checkFilas(numero_fuera_del_rango)
    assert not checkFilas(caracteres)
    assert not checkFilas(numeros_reales)
    assert checkFilas(irregular_fila)
    assert not checkFilas(irregular_columna)
    assert not checkFilas(lista_vacia)

    #checkColumnas
    assert checkColumnas(correcto)
    assert not checkColumnas(numero_repetido_fila_columna)
    assert not checkColumnas(numero_repetido_columna)
    assert not checkColumnas(numero_no_presente)
    assert not checkColumnas(numero_fuera_del_rango)
    assert checkColumnas(caracteres)
    assert checkColumnas(numeros_reales)
    assert checkColumnas(irregular_fila)
    assert not checkColumnas(irregular_columna)
    assert checkColumnas(lista_vacia)