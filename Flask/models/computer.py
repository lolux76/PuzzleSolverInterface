from pycsp3 import *


def logic_puzzle_computer():
    # Données
    processorsDomain = [20, 23, 25, 27, 31]
    processorsRange = range(1, 5)

    hardDisksDomain = [250, 320, 500, 750, 1024]
    hardDisksRange = range(1, 5)

    monitorsDomain = [130, 150, 156, 215, 270]
    monitorsRange = range(1, 5)

    pricesDomain = [699, 999, 1149, 1349, 1649]
    pricesRange = range(1, 5)

    # Variables principales

    # Andrew [processors , HD , monitor , prices]
    Andrew = VarArray(size=4, dom=range(5))
    PCA = VarArray(size=4, dom=range(5))
    PCB = VarArray(size=4, dom=range(5))
    PCC = VarArray(size=4, dom=range(5))
    PCD = VarArray(size=4, dom=range(5))

    # Variables auxiliaires
    for i in range(0, 4):
        satisfy(
            AllDifferent(
                Andrew[i],
                PCA[i],
                PCB[i],
                PCC[i],
                PCD[i]
            )
        )

    # Variables auxiliaires
    processorsSecondaires = VarArray(size=5, dom=[0, 1, 2, 3, 4])
    satisfy(
        AllDifferent(processorsSecondaires)
    )
    for p in processorsRange:
        satisfy(
            imply(Andrew[0] == p, processorsSecondaires[p] == 0),
            imply(PCA[0] == p, processorsSecondaires[p] == 1),
            imply(PCB[0] == p, processorsSecondaires[p] == 2),
            imply(PCC[0] == p, processorsSecondaires[p] == 3),
            imply(PCD[0] == p, processorsSecondaires[p] == 4),
        )

    hardDisksSecondaires = VarArray(size=5, dom=[0, 1, 2, 3, 4])
    satisfy(
        AllDifferent(hardDisksSecondaires)
    )
    for d in hardDisksRange:
        satisfy(
            imply(Andrew[1] == d, hardDisksSecondaires[d] == 0),
            imply(PCA[1] == d, hardDisksSecondaires[d] == 1),
            imply(PCB[1] == d, hardDisksSecondaires[d] == 2),
            imply(PCC[1] == d, hardDisksSecondaires[d] == 3),
            imply(PCD[1] == d, hardDisksSecondaires[d] == 4),
        )

    monitorsSecondaires = VarArray(size=5, dom=[0, 1, 2, 3, 4])
    satisfy(
        AllDifferent(monitorsSecondaires)
    )
    for m in monitorsRange:
        satisfy(
            imply(Andrew[2] == m, monitorsSecondaires[m] == 0),
            imply(PCA[2] == m, monitorsSecondaires[m] == 1),
            imply(PCB[2] == m, monitorsSecondaires[m] == 2),
            imply(PCC[2] == m, monitorsSecondaires[m] == 3),
            imply(PCD[2] == m, monitorsSecondaires[m] == 4),
        )
    pricesSecondaires = VarArray(size=5, dom=[0, 1, 2, 3, 4])
    satisfy(
        AllDifferent(pricesSecondaires)
    )
    for p in pricesRange:
        satisfy(
            imply(Andrew[3] == p, pricesSecondaires[p] == 0),
            imply(PCA[3] == p, pricesSecondaires[p] == 1),
            imply(PCB[3] == p, pricesSecondaires[p] == 2),
            imply(PCC[3] == p, pricesSecondaires[p] == 3),
            imply(PCD[3] == p, pricesSecondaires[p] == 4),
        )

    # Use-full variables to map PROCESSORS, order : 0= Andrew, 1=PCA, 2=PCB, 3=PCC, 4=PCD
    PROCESSORS = VarArray(size=5, dom=range(0, 5))
    # Unification
    satisfy(
        Andrew[0] == PROCESSORS[0],
        PCA[0] == PROCESSORS[1],
        PCB[0] == PROCESSORS[2],
        PCC[0] == PROCESSORS[3],
        PCD[0] == PROCESSORS[4],
    )
    # Use-full variables to map HARDDISKS, order : 0= Andrew, 1=PCA, 2=PCB, 3=PCC, 4=PCD
    HARDDISKS = VarArray(size=5, dom=range(0, 5))
    # Unification
    satisfy(
        Andrew[1] == HARDDISKS[0],
        PCA[1] == HARDDISKS[1],
        PCB[1] == HARDDISKS[2],
        PCC[1] == HARDDISKS[3],
        PCD[1] == HARDDISKS[4],
    )
    # Use-full variables to map MONITORS, order : 0= Andrew, 1=PCA, 2=PCB, 3=PCC, 4=PCD
    MONITORS = VarArray(size=5, dom=range(0, 5))
    # Unification
    satisfy(
        Andrew[2] == MONITORS[0],
        PCA[2] == MONITORS[1],
        PCB[2] == MONITORS[2],
        PCC[2] == MONITORS[3],
        PCD[2] == MONITORS[4],
    )
    # Use-full variables to map PRICE, order : 0= Andrew, 1=PCA, 2=PCB, 3=PCC, 4=PCD
    PRICES = VarArray(size=5, dom=range(0, 5))
    # Unification
    satisfy(
        Andrew[3] == PRICES[0],
        PCA[3] == PRICES[1],
        PCB[3] == PRICES[2],
        PCC[3] == PRICES[3],
        PCD[3] == PRICES[4],
    )

    # Constraint Element cant read in native python list
    processorsVarDomain = VarArray(size=5, dom=processorsDomain)
    hardDisksVarDomain = VarArray(size=5, dom=hardDisksDomain)
    monitorsVarDomain = VarArray(size=5, dom=monitorsDomain)
    pricesVarDomain = VarArray(size=5, dom=pricesDomain)
    # Unification
    for i in range(0, len(processorsDomain)):
        satisfy(
            processorsVarDomain[i] == processorsDomain[i],
            hardDisksVarDomain[i] == hardDisksDomain[i],
            monitorsVarDomain[i] == monitorsDomain[i],
            pricesVarDomain[i] == pricesDomain[i]
        )

    # Auxiliary Variable to encode constraint 1 (<=> existential variable)
    XN = Var(dom=range(5))
    # var of distance between 21.5 monitor and XN (0.4)
    C1P = Var(dom={4})  # CONSTANT

    #  Andrew bought the computer which was three hundred Euros less than the PC which has a processor that is 0.4 MHz more powerful than the one which has a 21.5' screen.
    # Unification
    satisfy(XN == processorsSecondaires[PROCESSORS[XN]])

    # Processor constraint
    satisfy(
        XN != monitorsSecondaires[3],
        processorsVarDomain[PROCESSORS[XN]] - processorsVarDomain[PROCESSORS[monitorsSecondaires[3]]] == C1P
    )  # <=> XN.processors - YMonitors(21.5).processors = 4

    # price constraint
    satisfy(
        XN != 0,
        300 + pricesVarDomain[Andrew[3]] == pricesVarDomain[PRICES[XN]]
    )  # <=> XN.prices == A.prices + 300

    # The five computers are:

    # the one chosen by Andrew (which doesn't have the 27' screen),
    satisfy(
        Andrew[2] != monitorsSecondaires[4]
    )  # <=> Andrew.monitor != 27'
    # the one which has the 2.0-MHz processor,
    satisfy(
        processorsSecondaires[0] != 0
    )  # <=> processors(20).ordinatuer != Andrew

    # the computer that has a 250 GB HD,
    satisfy(
        hardDisksSecondaires[0] != processorsSecondaires[0],
        hardDisksSecondaires[0] != 0
    )  # <=> HarsDisks(250).ordinateur != Andrew && HarsDisks(250).ordinateur != processors(20).ordinatuer
    # the one which has a price of 1,149 Euros
    satisfy(
        pricesSecondaires[2] != processorsSecondaires[0],
        pricesSecondaires[2] != 0,
        pricesSecondaires[2] != hardDisksSecondaires[0],
    )  # <=> prices(1149).ordinateur != Andrew && prices(1149).ordinateur != HarsDisks(250).ordinateur && prices(1149).ordinateur != processors(20).ordinatuer
    # and the computer (which doesn't have the 15' screen) that has the HD bigger than the one chosen by Andrew but smaller than that the one which has the 2.7 MHz processor.

    X15 = Var(dom=range(5))
    satisfy(
        X15 != monitorsSecondaires[1],
        hardDisksVarDomain[HARDDISKS[X15]] > hardDisksVarDomain[Andrew[1]],
        hardDisksVarDomain[HARDDISKS[X15]] < hardDisksVarDomain[HARDDISKS[processorsSecondaires[3]]],
        X15 == hardDisksSecondaires[HARDDISKS[X15]],
        X15 != processorsSecondaires[0],
        X15 != 0,
        X15 != hardDisksSecondaires[0],
        X15 != pricesSecondaires[2]

    )
    # The computer with the 320 Gb HD has either the 2.0 or the 2.3 MHz processor.
    satisfy(
        (hardDisksSecondaires[1] == processorsSecondaires[0]) |
        (hardDisksSecondaires[1] == processorsSecondaires[1])
    )

    # The processor of the computer which has the 15' screen is more powerful than the one in the computer that costs 999 euros but less powerful than the processor that is included in the 1,349 Euros computer.
    satisfy(
        processorsVarDomain[PROCESSORS[monitorsSecondaires[1]]] > processorsVarDomain[PROCESSORS[pricesSecondaires[1]]],
        processorsVarDomain[PROCESSORS[monitorsSecondaires[1]]] < processorsVarDomain[PROCESSORS[pricesSecondaires[3]]]
    )
    # The computer that has the 27' screen doesn't have the 320 Gb hard drive.
    satisfy(
        monitorsSecondaires[4] != hardDisksSecondaires[1]
    )

    # The 500 GB HD is included in the computer that has a more powerful processor and a larger size screen than the one which costs 699 euros (which doesn't include the 320 Gb HD).
    satisfy(
        processorsVarDomain[PROCESSORS[hardDisksSecondaires[2]]] > processorsVarDomain[
            PROCESSORS[pricesSecondaires[0]]],
        monitorsVarDomain[MONITORS[hardDisksSecondaires[2]]] > monitorsVarDomain[MONITORS[pricesSecondaires[0]]],
        pricesSecondaires[0] != hardDisksSecondaires[1]
    )

    # Résoudre le problème
    result = solve(solver=CHOCO)

    print("Result:", result)
    if result is SAT:
        # Afficher les résultats
        # print("Solution processorsSecondaires:",values(processorsSecondaires))
        # print("Solution monitorsSecondaires:",values(monitorsSecondaires))
        # print("Solution pricesSecondaires:",values(pricesSecondaires))
        """
        print("Solution Andrew:",values(Andrew))
        print("Solution PCA:",values(PCA))
        print("Solution PCB:",values(PCB))
        print("Solution PCC:",values(PCC))
        print("Solution PCD:",values(PCD))
        print("Solution XN:",values(XN))
        print("Solution processors values\t",[processorsDomain[values(PROCESSORS)[i]]/10 for i in range(0,5)])
        print("Solution HD values\t\t",[hardDisksDomain[values(HARDDISKS)[i]] for i in range(0,5)])
        print("Solution monitors values\t",[monitorsDomain[values(MONITORS)[i]]/10 for i in range(0,5)])
        print("Solution prices values\t\t",[pricesDomain[values(PRICES)[i]] for i in range(0,5)])
        """

        print("Andrew:")
        print("\tProcessor : ", processorsDomain[values(PROCESSORS)[values(Andrew[0])]] / 10, "MHz")
        print("\tHD : ", hardDisksDomain[values(HARDDISKS)[values(Andrew[1])]], "Gb")
        print("\tMonitor : ", monitorsDomain[values(MONITORS)[values(Andrew[2])]] / 10, "'")
        print("\tPrices : ", pricesDomain[values(PRICES)[values(Andrew[3])]], "€")

        print("PCA:")
        print("\tProcessor : ", processorsDomain[values(PROCESSORS)[values(PCA[0])]] / 10, "MHz")
        print("\tHD : ", hardDisksDomain[values(HARDDISKS)[values(PCA[1])]], "Gb")
        print("\tMonitor : ", monitorsDomain[values(MONITORS)[values(PCA[2])]] / 10, "'")
        print("\tPrices : ", pricesDomain[values(PRICES)[values(PCA[3])]], "€")

        print("PCB:")
        print("\tProcessor : ", processorsDomain[values(PROCESSORS)[values(PCB[0])]] / 10, "MHz")
        print("\tHD : ", hardDisksDomain[values(HARDDISKS)[values(PCB[1])]], "Gb")
        print("\tMonitor : ", monitorsDomain[values(MONITORS)[values(PCB[2])]] / 10, "'")
        print("\tPrices : ", pricesDomain[values(PRICES)[values(PCB[3])]], "€")

        print("PCC:")
        print("\tProcessor : ", processorsDomain[values(PROCESSORS)[values(PCC[0])]] / 10, "MHz")
        print("\tHD : ", hardDisksDomain[values(HARDDISKS)[values(PCC[1])]], "Gb")
        print("\tMonitor : ", monitorsDomain[values(MONITORS)[values(PCC[2])]] / 10, "'")
        print("\tPrices : ", pricesDomain[values(PRICES)[values(PCC[3])]], "€")


if __name__ == "__main__":
    logic_puzzle_computer()