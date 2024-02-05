from pycsp3 import *


def logic_puzzle_alPacino():
    timesDomain = [1175, 1180, 1220, 1230, 1245]
    timesRange = range(1, 5)

    filmsDomain = ["Scarface", "Scarecrow", "Donnie Brasco", "Minutes 88", "The Recruit"]
    filmsRange = range(1, 5)

    namesDomain = ["Sally", "Mary", "Jessica", "Laurie", "Mark"]
    namesRange = range(1, 5)

    # Day [times , films , names]
    Monday = VarArray(size=3, dom=range(5))
    Tuesday = VarArray(size=3, dom=range(5))
    Wednesday = VarArray(size=3, dom=range(5))
    Thursday = VarArray(size=3, dom=range(5))
    Friday = VarArray(size=3, dom=range(5))

    for i in range(0, 3):
        satisfy(
            AllDifferent(
                Monday[i],
                Tuesday[i],
                Wednesday[i],
                Thursday[i],
                Friday[i]
            )
        )
    # Variables auxiliaires
    timesSecondaires = VarArray(size=5, dom=[0, 1, 2, 3, 4])
    satisfy(
        AllDifferent(timesSecondaires)
    )
    for t in timesRange:
        satisfy(
            imply(Monday[0] == t, timesSecondaires[t] == 0),
            imply(Tuesday[0] == t, timesSecondaires[t] == 1),
            imply(Wednesday[0] == t, timesSecondaires[t] == 2),
            imply(Thursday[0] == t, timesSecondaires[t] == 3),
            imply(Friday[0] == t, timesSecondaires[t] == 4)
        )

    filmsSecondaires = VarArray(size=5, dom=[0, 1, 2, 3, 4])
    satisfy(
        AllDifferent(filmsSecondaires)
    )
    for f in filmsRange:
        satisfy(
            imply(Monday[1] == f, filmsSecondaires[f] == 0),
            imply(Tuesday[1] == f, filmsSecondaires[f] == 1),
            imply(Wednesday[1] == f, filmsSecondaires[f] == 2),
            imply(Thursday[1] == f, filmsSecondaires[f] == 3),
            imply(Friday[1] == f, filmsSecondaires[f] == 4)
        )

    namesSecondaires = VarArray(size=5, dom=[0, 1, 2, 3, 4])
    satisfy(
        AllDifferent(namesSecondaires)
    )
    for n in namesRange:
        satisfy(
            imply(Monday[2] == n, namesSecondaires[n] == 0),
            imply(Tuesday[2] == n, namesSecondaires[n] == 1),
            imply(Wednesday[2] == n, namesSecondaires[n] == 2),
            imply(Thursday[2] == n, namesSecondaires[n] == 3),
            imply(Friday[2] == n, namesSecondaires[n] == 4)
        )

    # Use-full variables to map TIMES, order : 0= Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday
    TIMES = VarArray(size=5, dom=range(0, 5))
    # Unification
    satisfy(
        Monday[0] == TIMES[0],
        Tuesday[0] == TIMES[1],
        Wednesday[0] == TIMES[2],
        Thursday[0] == TIMES[3],
        Friday[0] == TIMES[4],
    )

    # Use-full variables to map FILMS, order : 0= Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday
    FILMS = VarArray(size=5, dom=range(0, 5))
    # Unification
    satisfy(
        Monday[1] == FILMS[0],
        Tuesday[1] == FILMS[1],
        Wednesday[1] == FILMS[2],
        Thursday[1] == FILMS[3],
        Friday[1] == FILMS[4],
    )

    # Use-full variables to map NAMES, order : 0= Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday
    NAMES = VarArray(size=5, dom=range(0, 5))
    # Unification
    satisfy(
        Monday[2] == NAMES[0],
        Tuesday[2] == NAMES[1],
        Wednesday[2] == NAMES[2],
        Thursday[2] == NAMES[3],
        Friday[2] == NAMES[4],
    )

    # Constraint Element cant read in native python list
    timesVarDomain = VarArray(size=5, dom=timesDomain)
    filmsVarDomain = VarArray(size=5, dom=filmsDomain)
    namesVarDomain = VarArray(size=5, dom=namesDomain)
    # Unification
    for i in range(0, len(timesDomain)):
        satisfy(
            timesVarDomain[i] == timesDomain[i],
            filmsVarDomain[i] == filmsDomain[i],
            namesVarDomain[i] == namesDomain[i]
        )

        # 1. Of the 20-hundreds releases (88 Minutes & The Recruit), neither of which was Jessica's choice, one opened the week and one closed the week.
    satisfy(
        abs(filmsSecondaires[3] - filmsSecondaires[4]) == 4,
        Monday[2] != namesSecondaires[2],
        Friday[2] != namesSecondaires[2],
    )
    # 2. The latest of the 19-hundreds releases was shown at 30 minutes past the hour.
    T30 = Var(dom={30})
    satisfy(
        timesVarDomain[TIMES[filmsSecondaires[2]]] % 60 == T30
    )

    # 3. The releases shown before 8:00 pm were on consecutive days, as were the releases shown after 8:00 pm.
    satisfy(
        abs(timesSecondaires[0] - timesSecondaires[1]) == 1,
        abs(timesSecondaires[2] - timesSecondaires[4]) + abs(timesSecondaires[2] - timesSecondaires[3]) + abs(
            timesSecondaires[3] - timesSecondaires[4]) == 4
    )

    # 4. One of the men and one of the women had a showing before 8:00 pm, but neither was mid-week.
    satisfy(
        (
            (
                    (namesSecondaires[3] == timesSecondaires[0]) |
                    (namesSecondaires[3] == timesSecondaires[1])
            ), namesSecondaires[3] != 2
        ) or
        (
            (
                    (namesSecondaires[4] == timesSecondaires[0]) |
                    (namesSecondaires[4] == timesSecondaires[1])
            ), namesSecondaires[4] != 2
        )
    )
    satisfy(
        (
            (
                    (namesSecondaires[0] == timesSecondaires[0]) |
                    (namesSecondaires[0] == timesSecondaires[1])
            ), namesSecondaires[0] != 2
        ) or
        (
            (
                    (namesSecondaires[1] == timesSecondaires[0]) |
                    (namesSecondaires[1] == timesSecondaires[1])
            ), namesSecondaires[1] != 2
        ) or
        (
            (
                    (namesSecondaires[2] == timesSecondaires[0]) |
                    (namesSecondaires[2] == timesSecondaires[1])
            ), namesSecondaires[2] != 2
        )
    )

    # 5. Mark, whose choice was Scarecrow, had a showing at a time of one hour and five minutes after that of Scarface.
    T65 = Var(dom={65})
    satisfy(
        namesSecondaires[4] == filmsSecondaires[1],
        timesVarDomain[TIMES[namesSecondaires[4]]] == timesVarDomain[TIMES[filmsSecondaires[0]]] + T65
    )

    # 6. Neither Miss Farmer nor Miss Peters had a showing on an even-numbered day
    # <=> ni mardi (1) ni jeudi (3)
    satisfy(
        namesSecondaires[1] != 1,
        namesSecondaires[2] != 1,
        namesSecondaires[1] != 3,
        namesSecondaires[2] != 3
    )
    # 7. 88 Minutes showed at a time both 40 minutes to the hour and 40 minutes after the Thursday showing.
    T20 = Var(dom={20})
    satisfy(
        timesVarDomain[TIMES[filmsSecondaires[3]]] % 60 == T20,
        timesVarDomain[TIMES[filmsSecondaires[3]]] == timesVarDomain[TIMES[3]] + 40
    )

    # Résoudre le problème
    result = solve(solver=CHOCO)

    print("Result:", result)
    if result is SAT:
        # Afficher les résultats
        print("Solution found:")

        print("Monday:")
        print("\tHour : ", timesDomain[values(TIMES)[values(Monday[0])]], "//",
              timesDomain[values(TIMES)[values(Monday[0])]] // 60 - 12, ":",
              timesDomain[values(TIMES)[values(Monday[0])]] % 60)
        print("\tFilm : ", filmsDomain[values(FILMS)[values(Monday[1])]])
        print("\tName : ", namesDomain[values(NAMES)[values(Monday[2])]])

        print("Tuesday:")
        print("\tHour : ", timesDomain[values(TIMES)[values(Tuesday[0])]] // 60 - 12, ":",
              timesDomain[values(TIMES)[values(Tuesday[0])]] % 60)
        print("\tFilm : ", filmsDomain[values(FILMS)[values(Tuesday[1])]])
        print("\tName : ", namesDomain[values(NAMES)[values(Tuesday[2])]])

        print("Wednesday:")
        print("\tHour : ", timesDomain[values(TIMES)[values(Wednesday[0])]] // 60 - 12, ":",
              timesDomain[values(TIMES)[values(Wednesday[0])]] % 60)
        print("\tFilm : ", filmsDomain[values(FILMS)[values(Wednesday[1])]])
        print("\tName : ", namesDomain[values(NAMES)[values(Wednesday[2])]])

        print("Thursday:")
        print("\tHour : ", timesDomain[values(TIMES)[values(Thursday[0])]] // 60 - 12, ":",
              timesDomain[values(TIMES)[values(Thursday[0])]] % 60)
        print("\tFilm : ", filmsDomain[values(FILMS)[values(Thursday[1])]])
        print("\tName : ", namesDomain[values(NAMES)[values(Thursday[2])]])

        print("Friday:")
        print("\tHour : ", timesDomain[values(TIMES)[values(Friday[0])]] // 60 - 12, ":",
              timesDomain[values(TIMES)[values(Friday[0])]] % 60)
        print("\tFilm : ", filmsDomain[values(FILMS)[values(Friday[1])]])
        print("\tName : ", namesDomain[values(NAMES)[values(Friday[2])]])

        return Monday, Tuesday, Wednesday, Thursday, Friday


if __name__ == "__main__":
    logic_puzzle_alPacino()