## MORPION
from random import randint

Player1 = []
Player2 = []
Board = [["▯", "▯", "▯"],["▯", "▯", "▯"],["▯", "▯", "▯"]]
AcceptableResponse = [ 'A1', 'A2', 'A3', 'B1', 'B2', 'B3' , 'C1' , 'C2', 'C3' ]

### INITIALISATION
def Initialisation():
    CurrentPlayer = None
    print("Nous allons definir l'ordre des joueurs. \n Voulez vous definir l'ordre des joeurs aleatoirement ou choisir un ordre?")
    if CurrentPlayer != ("r" or "random" or "Random" or "X" or "x" or "o" or "O"):
        CurrentPlayer = input(" Tapez r ou random pour jouer avec un ordre aleatoire, sinon \n tapez X ou O pour definir le premier joueur.")
    if CurrentPlayer == "r" or "random" or "R" or "Random":
        CurrentPlayer = randint(0,1)
        if CurrentPlayer == 1:
            CurrentPlayer = "X"
        else:
            CurrentPlayer = "O"
    return CurrentPlayer

def ShowBoard(Board):
    print("     A -  B  - C  ")
    print("1 |",Board[0][0], " |", Board[0][1], " |" ,Board[0][2])
    print("------------------")
    print("2 |",Board[1][0], " |", Board[1][1], " |" ,Board[1][2])
    print("------------------")
    print("3 |",Board[2][0], " |", Board[2][1], " |" ,Board[2][2])
    return None

def ChangePlayerSign(PlayerSign):
    if PlayerSign == "X":
        PlayerSign = "O"
    else:
        PlayerSign = "X"
    return PlayerSign

# AcceptableResponse = [ 'A1', 'A2', 'A3', 'B1', 'B2', 'B3' , 'C1' , 'C2', 'C3' ]
ShowBoard(Board)
def ModifyBoard(PlayerSign,Board):
    SelectedCell = None
    print("Tour du Joeur", PlayerSign)
    while SelectedCell not in AcceptableResponse:
        SelectedCell = input("Selectionnez une case disponible. Utilisez les lettres et les numeros pour reperer les cases disponibles.")
    if SelectedCell in "A":
        if SelectedCell in "1":
            Board[0][0] = PlayerSign
            AcceptableResponse[0] = None   
        if SelectedCell in "2":
            Board[0][1] = PlayerSign
            AcceptableResponse[1] = None 
        if SelectedCell in "3":
            Board[0][2] = PlayerSign
            AcceptableResponse[2] = None 
    if SelectedCell in "B":
        if SelectedCell in "1":
            Board[1][0] = PlayerSign
            AcceptableResponse[0] = None   
        if SelectedCell in "2":
            Board[1][1] = PlayerSign
            AcceptableResponse[1] = None 
        if SelectedCell in "3":
            Board[1][2] = PlayerSign
            AcceptableResponse[2] = None 
    if SelectedCell in "C":
        if SelectedCell in "1":
            Board[2][0] = PlayerSign
            AcceptableResponse[0] = None   
        if SelectedCell in "2":
            Board[2][1] = PlayerSign
            AcceptableResponse[1] = None 
        if SelectedCell in "3":
            Board[2][2] = PlayerSign
            AcceptableResponse[2] = None 
    ShowBoard(Board)

ModifyBoard("X",Board)