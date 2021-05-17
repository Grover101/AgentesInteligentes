# Importar librerias
import random
from os import system

# uso para dar limite a la expancion del arbol
# inicio = 0
# limite = 1000000


def getBoardCopy(board):
    # Hace una copia del tablero y la retorna
    copiaBoard = []
    for i in board:
        copiaBoard.append(i)
    return copiaBoard


def drawBoard(board):
    # Esta funcion imprime el tablero
    # Un cuadro representado por una lista de 9 strings
    copyBoard = getBoardCopy(board)

    for i in range(1, 17):
        if(board[i] == ''):
            copyBoard[i] = str(i)
        else:
            copyBoard[i] = board[i]

    print(' ' + copyBoard[13] + ' | ' + copyBoard[14] +
          ' | ' + copyBoard[15] + ' | ' + copyBoard[16])
    print('-------------------')
    print('  ' + copyBoard[9] + ' | ' + copyBoard[10] +
          ' | ' + copyBoard[11] + ' | ' + copyBoard[12])
    print('-------------------')
    print('  ' + copyBoard[5] + ' |  ' + copyBoard[6] +
          ' |  ' + copyBoard[7] + ' |  ' + copyBoard[8])
    print('------------------')
    print('  ' + copyBoard[1] + ' |  ' + copyBoard[2] +
          ' |  ' + copyBoard[3] + ' |  ' + copyBoard[4])


def inputPlayerLetter():
    # El jugador elige con que letra quiere jugar "X" u "O"
    # Devuelve una lista con una letra del juegador y una letra del computador
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Elija si quiere jugar con X u O?')
        letter = input().upper()
        if(letter != 'X' and letter != 'O'):
            print("Eligio una letra que no es correcta!")

    # El primer elemento en la lista es el jugador y el segundo es el computador
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirts():
    # Se elige aleatoriamente quien va primero humano o computador
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'jugador'


def makeMove(board, letter, move):
    # registra la jugada de un jugador sobre el tablero
    board[move] = letter


def isWinner(board, letter):
    # Dado un cuadro y una letra, esta funcion retorn True si la letra se repite 3 veces
    return(
        # Horizontales
        (board[13] == letter and board[14] == letter and board[15] == letter) or
        (board[14] == letter and board[15] == letter and board[16] == letter) or
        (board[9] == letter and board[10] == letter and board[11] == letter) or
        (board[10] == letter and board[11] == letter and board[12] == letter) or
        (board[5] == letter and board[6] == letter and board[7] == letter) or
        (board[6] == letter and board[7] == letter and board[8] == letter) or
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[2] == letter and board[3] == letter and board[4] == letter) or
        # Verticales
        (board[13] == letter and board[9] == letter and board[5] == letter) or
        (board[9] == letter and board[5] == letter and board[1] == letter) or
        (board[14] == letter and board[10] == letter and board[6] == letter) or
        (board[10] == letter and board[6] == letter and board[2] == letter) or
        (board[15] == letter and board[11] == letter and board[7] == letter) or
        (board[11] == letter and board[7] == letter and board[3] == letter) or
        (board[16] == letter and board[12] == letter and board[8] == letter) or
        (board[12] == letter and board[8] == letter and board[4] == letter) or
        # Diagonales
        (board[15] == letter and board[10] == letter and board[5] == letter) or
        (board[16] == letter and board[11] == letter and board[6] == letter) or
        (board[11] == letter and board[6] == letter and board[1] == letter) or
        (board[12] == letter and board[7] == letter and board[2] == letter) or
        (board[14] == letter and board[11] == letter and board[8] == letter) or
        (board[13] == letter and board[10] == letter and board[7] == letter) or
        (board[10] == letter and board[7] == letter and board[4] == letter) or
        (board[9] == letter and board[6] == letter and board[3] == letter))


def isSpaceFree(board, move):
    # Retorna True si un espacio solicitado esta libre en el tablero
    if(board[move] == ''):
        return True
    else:
        return False


def getPlayerMove(board):
    # Recibe el movimiento del jugador
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
        print('Cual es su proximo movimiento? (1-16)')
        move = input()
        if(move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'):
            print("MOVIMENTO INVALIDO!, EL MOVIMIENTO DEBE SER UN VALOR ENTRE 1 Y 16!")

        if(move in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'):
            if(not isSpaceFree(board, int(move))):
                print(
                    "ESPACO NO DISPONIBLE! ELIJA OTRO ESPACIO ENTRE 1 Y 16 DE LOS ESPACIOS DISPONIBLES!")

    return int(move)


# def chooseRandomMoveFromList(board, movesList):
#     # Retorna un movimento valido aleatorio
#     # Retorna None si no existen movimentos validos posibles
#     posiblesMovimentos = []
#     for i in movesList:
#         if isSpaceFree(board, i):
#             posiblesMovimentos.append(i)

#     if len(posiblesMovimentos) != 0:
#         return random.choice(posiblesMovimentos)
#     else:
#         return None


def isBoardFull(board):
    # Retorna True si no existen espacios disponibles en el tablero
    for i in range(1, 17):
        if isSpaceFree(board, i):
            return False
    return True


def espaciosDisponibles(board):
    # Retorna una lista de todos los espacion disponibles en el tablero
    espacios = []
    for i in range(1, 17):
        if isSpaceFree(board, i):
            espacios.append(i)
    return espacios


def finishGame(board, computerLetter):
    # Verifica si el juego a llegado a su final
    # Retorna -1 si gana el jugador
    # Retorna 1 si gana el computador
    # Retorna 0 si el juego termina empatado
    # Retorna None si el juego no ha terminado

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if(isWinner(board, computerLetter)):
        return 1

    elif(isWinner(board, playerLetter)):
        return -1

    elif(isBoardFull(board)):
        return 0

    else:
        return None


def alphabeta(board, computerLetter, turn, alpha, beta):
    # Fazemos aqui a poda alphabeta
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if turn == computerLetter:
        nextTurn = playerLetter
    else:
        nextTurn = computerLetter

    finish = finishGame(board, computerLetter)

    if (finish != None):
        return finish
    # para no expandir el arbol
    # global inicio
    # global limite
    # if(inicio >= limite):
    #     limite*2
    #     return 1
    # else:
    #     inicio += 1

    espacios = espaciosDisponibles(board)

    if turn == computerLetter:
        for move in espacios:
            makeMove(board, turn, move)
            val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
            makeMove(board, '', move)
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return alpha
        return alpha

    else:
        for move in espacios:
            makeMove(board, turn, move)
            val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
            makeMove(board, '', move)
            if val < beta:
                beta = val
            if alpha >= beta:
                return beta
        return beta


def getComputerMove(board, turn, computerLetter):
    # Definimos aqui cual sera los movimentos del computador
    a = -2
    opcoes = []
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Comecamos aqui con MiniMax
    # Primero verificamos que podemos ganar un proximo movimento
    for i in range(1, 17):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # verifica si el jogador puede vencer en el proximo movimento o bloquearlo
    for i in range(1, 17):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    possiveisOpcoesOn = espaciosDisponibles(board)

    for move in possiveisOpcoesOn:
        makeMove(board, computerLetter, move)
        val = alphabeta(board, computerLetter, playerLetter, -2, 2)
        makeMove(board, '', move)
        if val > a:
            a = val
            opcoes = [move]
        elif val == a:
            opcoes.append(move)
    return random.choice(opcoes)


print('Vamos a jugar el 4 en raya')
jugar = True
while jugar:
    # Comienzo del juego
    theBoard = [''] * 17
    playerLetter, computerLetter = inputPlayerLetter()
    # usar turno aleatorio de jugador
    # turn = whoGoesFirts()
    turn = 'jugador'
    print(turn + ' juega primero,')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'jugador':
            # Turno del jugador
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Woooow! Ganaste el Juego!')
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('El juego terminó en empate')
                    break
                else:
                    turn = 'computador'

        else:
            # Turno del computador
            move = getComputerMove(theBoard, playerLetter, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("La computadora gana :(")
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('El juego terminó en empate')
                    break
                else:
                    turn = 'jugador'

    letraNueva = ''
    while not(letraNueva == 'S' or letraNueva == 'N'):
        print("¿Quieres jugar de nuevo? Escriba Y (para sí) o N (para no)")
        letraNueva = input().upper()
        if (letraNueva != 'S' and letraNueva != 'N'):
            print("¡Entrada inválida! Escriba Y (para sí) o N (para no).")
        if(letraNueva == 'N'):
            print("¡Fue bueno jugar contigo! ¡Hasta luego!")
            jugar = False
