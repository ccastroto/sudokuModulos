def checkFilas(sudoku):
    
    if not sudoku or not all(sudoku):
        return False
    
    numMax = max([len(fila) for fila in sudoku])
    filaCorrecta = list(range(1, (numMax + 1)))


    for fila in sudoku:
        if sorted(fila) != filaCorrecta:
            return False
    return True