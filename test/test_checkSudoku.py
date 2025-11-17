from checkSudoku import checkSudoku
import casosTest.casosTest as casosTest
import pytest

@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto, True),
        (casosTest.numero_repetido_fila_columna, False),
        (casosTest.numero_repetido_columna, False),
        (casosTest.numero_no_presente, False),
        (casosTest.numero_fuera_del_rango, False),
        (casosTest.caracteres, False),
        (casosTest.numeros_reales, False),
        (casosTest.irregular_fila, False),
        (casosTest.irregular_columna, False),
        (casosTest.lista_vacia, False)
    ],
)

def test_checkSudoku(sudoku, sano):
    assert checkSudoku(sudoku) == sano
    