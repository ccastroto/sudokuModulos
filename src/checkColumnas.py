def checkColumnas(sudoku):

    assert isinstance(sudoku, list),"interfaz exigue sudoku debe ser una lista"

    numColuma = len(sudoku)
    filaActual = 0

    for fila in sudoku:
        
        for numero in fila:
        
            filaSig = filaActual + 1

            while filaSig < numColuma:

                try:

                    posicionNumFilaSig = sudoku[filaSig].index(numero)

                except ValueError:

                    return False
        
                else:
                    if posicionNumFilaSig == fila.index(numero):
                        return False

                    else:
                        filaSig += 1

        filaActual += 1
    
    return True