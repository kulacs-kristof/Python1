import random


def main() -> None:
    while True:
        választások = ["Kő", "Papír", "Olló"]

        inp = int(input("0 - Kő, 1 - Papír, 2 - Olló \n"))

        AI_inp = random.randint(0, 2)

        # 0-lose 1-draw 2-win
        asd = ""

        if (inp == 0 and AI_inp == 2):
            asd = "Nyertél"
        elif (inp == 1 and AI_inp == 0):
            asd = "Nyertél"
        elif (inp == 2 and AI_inp == 1):
            asd = "Nyertél"
        elif (inp == AI_inp):
            asd = "Döntetlen"
        else:
            asd = "Vesztettél"

        print(f"{asd}! {választások[inp]} - {választások[AI_inp]}\n")


if __name__ == "__main__":
    main()
