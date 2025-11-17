def checkNumeroValido(sudoku):
    n = len(sudoku)

    for fila in sudoku:
        if fila == sudoku:
            return True
        if range(1, (n + 1)) == fila:
            return True
        
        for numero in fila:
            if not isinstance(numero, int):
                return False
    return True