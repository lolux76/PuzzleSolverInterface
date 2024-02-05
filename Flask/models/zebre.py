from pycsp3 import *

def zebra_puzzle():
    clear()
    position = range(1,6)
    # Entités
    Leslie, Holly, Andrea, Julie, Victoria = names = VarArray(size = 5, dom = position)
    Wilson, Miller, Davis, Brown, Lopes = surnames = VarArray(size = 5, dom = position)
    Red, Blue, White, Yellow, Green = shirts = VarArray(size = 5, dom = position)
    Argentine, Italian, Chilean, Australian, Bordeaux = wines = VarArray(size = 5, dom = position)
    Farfalle, Lasagne, Penne, Spaghetti, Ravioli = pastas = VarArray(size = 5, dom = position)
    y30, y35, y40, y45, y50 = age = VarArray(size = 5, dom = position)


    # Contraintes
    satisfy(
        AllDifferent(names),
        AllDifferent(surnames),
        AllDifferent(shirts),
        AllDifferent(wines),
        AllDifferent(pastas),
        AllDifferent(age),

        # Contraintes fournies dans la description
            # The woman wearing the White shirt is next to the woman who likes Lombardian (=Italian) wines.
        abs(White - Italian) == 1,
            # Ms Miller is somewhere between Ms Davis and Ms Brown, in that order.
        Davis < Miller,
        Miller < Brown,
            # The youngest woman is at the third position.
        y30 == 3,
            # The 45-year-old woman is somewhere to the right of the woman wearing the Red shirt.
        Red < y45,
            # The woman who likes Chilean wines also likes Farfalle.
        Chilean == Farfalle,
            # At the first position is the woman that likes Argentine wines.
        Argentine == 1,
            # Andrea is exactly to the right of the 35-year-old woman.
        Andrea == y35 + 1,
            # The woman wearing the Blue shirt is somewhere between Ms Davis...
        Davis < Blue,
            # ...and Holly, in that order.
        Blue < Holly,
            # Victoria is next to Leslie.
        abs(Victoria - Leslie) == 1,
            # The woman wearing the Red shirt is somewhere to the left of the woman who likes Australian wines.
        Red < Australian,
            # Ms Wilson is next to the 30-year-old woman.
        abs(Wilson - y30) == 1,
            # Leslie is exactly to the left of the 30-year-old woman.
        Leslie == y30 - 1,
            # Holly is somewhere to the right of the woman wearing the Red shirt.
        Red < Holly,
            # Ms Brown is exactly to the left of Julie.
        Brown == Julie - 1,
            # The youngest woman likes Penne.
        y30 == Penne,
            # Ms Wilson is wearing the White shirt.
        Wilson == White,
            # The woman who likes Lasagne is somewhere between the woman who likes Italian wines...
        Italian < Lasagne,
            # ...and the woman who likes Spaghetti, in that order.
        Lasagne < Spaghetti,
            # At the second position is the woman wearing the Blue shirt.
        Blue == 2,
            # The 40-year-old woman likes Lasagne.
        y40 == Lasagne,
            # Ms Lopes is at the fifth position.
        Lopes == 5,
            # The woman that likes Australian wines is somewhere between Victoria...
        Victoria < Australian,
            # ...and the woman who likes wines from Bordeaux, in that order.
        Australian < Bordeaux,
            # The woman wearing the Yellow shirt is exactly to the left of the 35-year-old woman.
        Yellow == y35 - 1,
    )

    # Résoudre le problème
    result = solve(solver=CHOCO)

    print("Result:", result)
    if result is SAT:
        # Afficher les résultats
        print("Solution found:")
        for i in range(1,6):
            print("Position " + str(i) + " : ")
            for j in range(0,5):
                if values(names[j]) == i:
                    print("\t" + str(names[j]))
                if values(surnames[j]) == i:
                    print("\t" + str(surnames[j]))
                if values(shirts[j]) == i:
                    print("\t" + str(shirts[j]))
                if values(wines[j]) == i:
                    print("\t" + str(wines[j]))
                if values(pastas[j]) == i:
                    print("\t" + str(pastas[j]))
                if values(age[j]) == i:
                    print("\t" + str(age[j]))

if __name__ == "__main__":
    zebra_puzzle()