from os import system
from random import randint
from marci import BG_NONE, color, Foreground

board: list[str] = []
prefix_x: str = f"[{color(Foreground.GREEN, BG_NONE, 'X')}]"
prefix_o: str = f"[{color(Foreground.RED, BG_NONE, 'O')}]"


def CreateBoard():
    board.clear()
    for x in range(9):
        board.append(f"[{color(Foreground.GREY, BG_NONE, str(x + 1))}]")


def DrawBoard():
    system("cls")
    for x in range(len(board)):
        if x % 3 == 0 and x != 0:
            print()
        print(board[x], end="")


def checkWin():
    if board[0] == board[1] == board[2] != "[ ]":
        print(f"\n{board[0]} nyert")
        return True
    elif board[3] == board[4] == board[5] != "[ ]":
        print(f"\n{board[3]} nyert!")
        return True
    elif board[6] == board[7] == board[8] != "[ ]":
        print(f"\n{board[6]} nyert!")
        return True
    elif board[0] == board[3] == board[6] != "[ ]":
        print(f"\n{board[0]} nyert!")
        return True
    elif board[1] == board[4] == board[7] != "[ ]":
        print(f"\n{board[1]} nyert!")
        return True
    elif board[2] == board[5] == board[8] != "[ ]":
        print(f"\n{board[2]} nyert!")
        return True
    elif board[0] == board[4] == board[8] != "[ ]":
        print(f"\n{board[0]} nyert!")
        return True
    elif board[2] == board[4] == board[6] != "[ ]":
        print(f"\n{board[2]} nyert!")
        return True

    for x in range(len(board)):
        if Foreground.GREY in board[x]:
            return False
    print("\nDöntetlen")
    return True


def AI_BRAIN():
    if board[0] == prefix_x and board[1] == prefix_x and board[2] != prefix_o:
        place(2, prefix_o)
    elif board[0] == prefix_x and board[2] == prefix_x and board[1] != prefix_o:
        place(1, prefix_o)
    elif board[0] == prefix_x and board[3] == prefix_x and board[6] != prefix_o:
        place(6, prefix_o)
    elif board[0] == prefix_x and board[6] == prefix_x and board[3] != prefix_o:
        place(3, prefix_o)
    elif board[0] == prefix_x and board[4] == prefix_x and board[8] != prefix_o:
        place(8, prefix_o)
    elif board[0] == prefix_x and board[8] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[1] == prefix_x and board[4] == prefix_x and board[7] != prefix_o:
        place(7, prefix_o)
    elif board[1] == prefix_x and board[7] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[2] == prefix_x and board[4] == prefix_x and board[6] != prefix_o:
        place(6, prefix_o)
    elif board[2] == prefix_x and board[6] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[2] == prefix_x and board[5] == prefix_x and board[8] != prefix_o:
        place(8, prefix_o)
    elif board[2] == prefix_x and board[8] == prefix_x and board[5] != prefix_o:
        place(5, prefix_o)
    elif board[2] == prefix_x and board[1] == prefix_x and board[0] != prefix_o:
        place(0, prefix_o)
    elif board[2] == prefix_x and board[0] == prefix_x and board[1] != prefix_o:
        place(1, prefix_o)
    elif board[3] == prefix_x and board[4] == prefix_x and board[5] != prefix_o:
        place(5, prefix_o)
    elif board[3] == prefix_x and board[5] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[3] == prefix_x and board[0] == prefix_x and board[6] != prefix_o:
        place(6, prefix_o)
    elif board[3] == prefix_x and board[6] == prefix_x and board[0] != prefix_o:
        place(0, prefix_o)
    elif board[4] == prefix_x and board[0] == prefix_x and board[8] != prefix_o:
        place(8, prefix_o)
    elif board[4] == prefix_x and board[8] == prefix_x and board[0] != prefix_o:
        place(0, prefix_o)
    elif board[4] == prefix_x and board[2] == prefix_x and board[6] != prefix_o:
        place(6, prefix_o)
    elif board[4] == prefix_x and board[6] == prefix_x and board[2] != prefix_o:
        place(2, prefix_o)
    elif board[4] == prefix_x and board[1] == prefix_x and board[7] != prefix_o:
        place(7, prefix_o)
    elif board[4] == prefix_x and board[7] == prefix_x and board[1] != prefix_o:
        place(1, prefix_o)
    elif board[4] == prefix_x and board[3] == prefix_x and board[5] != prefix_o:
        place(5, prefix_o)
    elif board[4] == prefix_x and board[5] == prefix_x and board[3] != prefix_o:
        place(3, prefix_o)
    elif board[5] == prefix_x and board[2] == prefix_x and board[8] != prefix_o:
        place(8, prefix_o)
    elif board[5] == prefix_x and board[8] == prefix_x and board[2] != prefix_o:
        place(2, prefix_o)
    elif board[5] == prefix_x and board[3] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[5] == prefix_x and board[4] == prefix_x and board[3] != prefix_o:
        place(3, prefix_o)
    elif board[6] == prefix_x and board[7] == prefix_x and board[8] != prefix_o:
        place(8, prefix_o)
    elif board[6] == prefix_x and board[8] == prefix_x and board[7] != prefix_o:
        place(7, prefix_o)
    elif board[6] == prefix_x and board[0] == prefix_x and board[3] != prefix_o:
        place(3, prefix_o)
    elif board[6] == prefix_x and board[3] == prefix_x and board[0] != prefix_o:
        place(0, prefix_o)
    elif board[6] == prefix_x and board[2] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[6] == prefix_x and board[4] == prefix_x and board[2] != prefix_o:
        place(2, prefix_o)
    elif board[7] == prefix_x and board[6] == prefix_x and board[8] != prefix_o:
        place(8, prefix_o)
    elif board[7] == prefix_x and board[8] == prefix_x and board[6] != prefix_o:
        place(6, prefix_o)
    elif board[7] == prefix_x and board[1] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[7] == prefix_x and board[4] == prefix_x and board[1] != prefix_o:
        place(1, prefix_o)
    elif board[8] == prefix_x and board[6] == prefix_x and board[7] != prefix_o:
        place(7, prefix_o)
    elif board[8] == prefix_x and board[7] == prefix_x and board[6] != prefix_o:
        place(6, prefix_o)
    elif board[8] == prefix_x and board[2] == prefix_x and board[5] != prefix_o:
        place(5, prefix_o)
    elif board[8] == prefix_x and board[5] == prefix_x and board[2] != prefix_o:
        place(2, prefix_o)
    elif board[8] == prefix_x and board[0] == prefix_x and board[4] != prefix_o:
        place(4, prefix_o)
    elif board[8] == prefix_x and board[4] == prefix_x and board[0] != prefix_o:
        place(0, prefix_o)
    else:
        while place(randint(0, len(board) - 1), prefix_o) is False:
            continue


def place(x, prefix):
    # Foglalt mező
    try:
        if board[x] == prefix_x or board[x] == prefix_o:
            return False
        else:
            board[x] = prefix
            DrawBoard()
            return True
    except IndexError:
        return False


def main() -> None:
    CreateBoard()
    ended = False
    while True:
        if ended is False:
            x = ""

            # User input
            while x not in range(0, len(board)):
                try:
                    DrawBoard()
                    x = int(input("\nAdj meg egy számot [1-9]\n")) - 1

                    if place(x, prefix_x) is False:
                        x = ""
                        continue
                except ValueError:
                    DrawBoard()
                    continue

            ended = checkWin()

            if ended is True:
                continue

            # Computer input
            AI_BRAIN()

            ended = checkWin()
        else:
            inp = input("\nSzeretnél új játékot kezdeni? [Y/N]\n")
            if inp.lower() == "y":
                CreateBoard()
                ended = False
            else:
                break


if __name__ == "__main__":
    main()
