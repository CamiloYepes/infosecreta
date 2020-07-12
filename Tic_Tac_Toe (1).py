import random


def clearBoard():
    board = [["°","°","°"],
            ["°","°","°"],
            ["°","°","°"]]
    slots = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
    userInput = []
    pcInput = []

    mark1 = "X"
    mark2 = "O"
    gameBoard(board,slots,mark1,mark2,userInput,pcInput)


def gameBoard(board,slots,mark1,mark2,userInput,pcInput):
    print("  A B C")
    for count, row in enumerate(board):
        print(count+1, *row)

    gameUser(board,slots,mark1,mark2,userInput,pcInput)
    
def gameUser(board,slots,mark1,mark2,userInput,pcInput):
    user = input("Escoge una posicion: ")
    user = user.upper()
    if len(slots) > 1:
        if user in slots:
            slots.remove(user)
            userInput.append(user)
            if user == "A1":
                board[0][0] = mark1
            elif user == "A2":
                board[1][0] = mark1
            elif user == "A3":
                board[2][0] = mark1
            elif user == "B1":
                board[0][1] = mark1
            elif user == "B2":
                board[1][1] = mark1
            elif user == "B3":
                board[2][1] = mark1
            elif user == "C1":
                board[0][2] = mark1
            elif user == "C2":
                board[1][2] = mark1
            elif user == "C3":
                board[2][2] = mark1
        else:
            print("Error")
            gameUser(board,slots,mark1,mark2,userInput,pcInput)

    gamePC(board,slots,mark1,mark2,userInput,pcInput)
    
def gamePC(board,slots,mark1,mark2,userInput,pcInput):

    pcRand = random.choice(slots)
    slots.remove(pcRand)
    pcInput.append(pcRand)
    if pcRand == "A1":
        board[0][0] = mark2
    elif pcRand == "A2":
        board[1][0] = mark2
    elif pcRand == "A3":
        board[2][0] = mark2
    elif pcRand == "B1":
        board[0][1] = mark2
    elif pcRand == "B2":
        board[1][1] = mark2
    elif pcRand == "B3":
        board[2][1] = mark2
    elif pcRand == "C1":
        board[0][2] = mark2
    elif pcRand == "C2":
        board[1][2] = mark2
    elif pcRand == "C3":
        board[2][2] = mark2
    gameWin(board,slots,mark1,mark2,userInput,pcInput)
            
def gameWin(board,slots,mark1,mark2,userInput,pcInput):
## Horizontal
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "°":
            if row[0] == mark1:
                print("Eres el ganador Jugador")
                salir()
            elif row[0] == mark2:
                print("Te ha ganado la computadora")
                salir()
        else:
            pass
## Vertical
    if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != "°":
        if board[0][0] == mark1:
            print("Eres el ganador Jugador")
            salir()
        elif board[0][0] == mark2:
            print("Te ha ganado la computadora")
            salir()
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != "°":
        if board[0][1] == mark1:
            print("Eres el ganador Jugador")
            salir()
        elif board[0][1] == mark2:
            print("Te ha ganado la computadora")
            salir()
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != "°":
        if board[0][2] == mark1:
            print("Eres el ganador Jugador")
            salir()
        elif board[0][2] == mark2:
            print("Te ha ganado la computadora")
            salir()
    else:
        pass
## Diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != "°":
        if board[0][0] == mark1:
            print("Eres el ganador Jugador")
            salir()
        elif board[0][0] == mark2:
            print("Te ha ganado la computadora")
            salir()
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != "°":
        if board[0][2] == mark1:
            print("Eres el ganador Jugador")
            salir()
        elif board[0][2] == mark2:
            print("Te ha ganado la computadora")
            salir()
    else:
        gameBoard(board,slots,mark1,mark2,userInput,pcInput)

def salir():
    print("Deseas: 1. Salir. 2.  Jugar de nuevo")
    choose = int(input("Selecciona una opción: "))
    if choose == 2:
        clearBoard()
    else:
        quit()

def empate():
    print("Ha sido un empate")
    salir()

clearBoard()