# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo MUESTRA en la consola.
def display_board(board):
    print('+-------' * 3, '+', sep = '')
    for row in range(3):
        print('|       ' * 3, '|', sep = '')
        for col in range(3):
            print('|   ', str(board[row][col]), '   ', sep = '', end='')
        print('|')
        print('|       ' * 3, '|', sep = '')
        print('+-------' * 3, '+', sep = '')
    enter_move(board)
# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
# VERIFICA LA ENTRADA y actualiza el tablero acorde a la decisión del usuario.
def enter_move(board):
    ok = False
    while not ok:
        mov = input('Es tu turno, elige una casilla libre: ')
        if mov is int and mov > 0 and mov < 10:
            for row in range(3):
                for col in range(3):
                    if board[row][col] == mov:
                        board[row][col] = '0'
                        display_board(board)
            display_board(board)
            ok = True
        else: print('Valor inválido.')
    
# La función examina el tablero y CONSTRUYE UNA LISTA de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
# def make_list_of_free_fields(board):


# # La función analiza el estatus del tablero para verificar si 
# # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
# # def victory_for(board, sign):


# # La función dibuja el movimiento de la máquina y actualiza el tablero.
# # def draw_move(board):


board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
display_board(board)