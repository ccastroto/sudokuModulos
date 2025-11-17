from src.checkColumnas import checkColumnas
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
        (casosTest.caracteres, True),
        (casosTest.numeros_reales, True),
        (casosTest.irregular_fila, True),
        (casosTest.irregular_columna, False),
        (casosTest.lista_vacia, True)
    ],
)

def test_checkColumnas(sudoku, sano):
    assert checkColumnas(sudoku) == sano
    