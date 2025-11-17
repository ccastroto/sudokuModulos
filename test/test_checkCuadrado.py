from src.checkCuadrado import checkCuadrado
import casosTest.casosTest as casosTest
import pytest

@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto, True),
        (casosTest.numero_repetido_fila_columna, True),
        (casosTest.numero_repetido_columna, True),
        (casosTest.numero_no_presente, True),
        (casosTest.numero_fuera_del_rango, True),
        (casosTest.caracteres, True),
        (casosTest.numeros_reales, True),
        (casosTest.irregular_fila, False),
        (casosTest.irregular_columna, False),
        (casosTest.lista_vacia, False)
    ],
)

def test_checkCuadrado(sudoku, sano):
    assert checkCuadrado(sudoku) == sano
    