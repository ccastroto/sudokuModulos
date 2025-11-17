from src.checkNumeroValido import checkNumeroValido
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
        (casosTest.caracteres, False),
        (casosTest.numeros_reales, False),
        (casosTest.irregular_fila, True),
        (casosTest.irregular_columna, True),
        (casosTest.lista_vacia, True)
    ],
)

def test_checkNumeroValido(sudoku, sano):
    assert checkNumeroValido(sudoku) == sano
    