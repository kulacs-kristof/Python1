from os import system
import marci
from random import randint

slots = []


def createBoard(xSize, ySize):
    slots.clear()
    for x in range(xSize * ySize):
        slots.append("[ ]")


def drawBoard():
    system("cls")
    for x in range(len(slots)):
        if x % 3 == 0 and x != 0:
            print()
        print(slots[x], end="")


def checkWin():
    if slots[0] == slots[1] == slots[2] != "[ ]":
        print(slots[0], "nyert")
        return True
    elif slots[3] == slots[4] == slots[5] != "[ ]":
        print(slots[3], "nyert!")
        return True
    elif slots[6] == slots[7] == slots[8] != "[ ]":
        print(slots[6], "nyert!")
        return True
    elif slots[0] == slots[3] == slots[6] != "[ ]":
        print(slots[0], "nyert!")
        return True
    elif slots[1] == slots[4] == slots[7] != "[ ]":
        print(slots[1], "nyert!")
        return True
    elif slots[2] == slots[5] == slots[8] != "[ ]":
        print(slots[2], "nyert!")
        return True
    elif slots[0] == slots[4] == slots[8] != "[ ]":
        print(slots[0], "nyert!")
        return True
    elif slots[2] == slots[4] == slots[6] != "[ ]":
        print(slots[2], "nyert!")
        return True

    if "[ ]" not in slots:
        print("Döntetlen")
        return True
    return False


createBoard(3, 3)

ended = False

while True:
    if ended is False:
        drawBoard()
        x = ""
        while type(x) != int:
            x = input(f"\nHova szeretnél rakni? [1-{len(slots)}]\n")
            try:
                x = int(x)
            except BaseException:
                drawBoard()
        x = int(x)
        x -= 1

        while slots[x] != "[ ]" and x in range(len(slots)):
            drawBoard()
            x = int(input(f"\nHova szeretnél rakni? [1-{len(slots)}]\n")) - 1
        slots[x] = f"[{marci.color(marci.Foreground.CYAN, marci.BG_NONE, 'X')}]"

        drawBoard()
        print()
        ended = checkWin()

        ai_slot = x
        while slots[ai_slot] != "[ ]":
            ai_slot = randint(0, len(slots) - 1)
        slots[ai_slot] = f"[{marci.color(marci.Foreground.RED, marci.BG_NONE, 'O')}]"

        drawBoard()
        print()
        ended = checkWin()
    else:
        inp = input("Szeretnél új játékot kezdeni? [Y/N]\n")
        if inp.lower() == "y":
            createBoard(3, 3)
            ended = False
        else:
            break
