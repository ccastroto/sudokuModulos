def checkCuadrado(sudoku):

    for fila in sudoku:
        if len(fila) != len(sudoku):
            return False
    return True