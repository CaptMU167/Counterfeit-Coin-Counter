import os
from random import choice

def coinBot():
    print("First I'll weigh up ABCD and EFGH...")
    balance("ABCD EFGH")
    if coins["A"] == "C":
        print("I, J, K, and L? Ok, I'll weigh IJ against AB!")
        balance("IJ AB")
        if coins["I"] != "C":
            print("Still I and J? Ok, I'll weigh up I and A!")
            balance("I A")
            for coin in ["I", "J"]:
                if coins[coin] != "C":
                    print(f"The counterfeit coin is coin {coin}!")
        else:
            print("So it's K or L? I'll weigh K against A then!")
            balance("K A")
            for coin in ["K", "L"]:
                if coins[coin] != "C":
                    print(f"The counterfeit coin is coin {coin}!")
    else:
        print("Ok... let's try ABCEF against DIJKL!")
        balance("ABCEF DIJKL")
        if coins["A"] != "C":
            print("A, B, or C? Let's try A against B then!")
            balance("A B")
            for coin in ["A", "B", "C"]:
                if coins[coin] != "C":
                    print(f"The counterfeit coin is coin {coin}!")
        elif coins["E"] != "C":
            print("D, E, or F? Let's try E against F then!")
            balance("E F")
            for coin in ["D", "E", "F"]:
                if coins[coin] != "C":
                    print(f"The counterfeit coin is coin {coin}!")
        else:
            print("G or H? Easy! G against H!")
            balance("G H")
            for coin in ["G", "H"]:
                if coins[coin] != "C":
                    print(f"The counterfeit coin is coin {coin}!")

def clearCoins():
    allCoins = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    for coin in allCoins:
        coins[coin] = "?"

def balance(weights):
    passed = False
    leftTotal = 0
    rightTotal = 0
    leftCoins = []
    rightCoins = []
    allCoins = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

    for coin in weights:
        if coin == " ":
            passed = True
            toAdd = 0
        else:
            allCoins.remove(coin)
            if coin == fakeCoin[0]:
                if fakeCoin[1] == "H":
                    toAdd = 1.5
                else:
                    toAdd = 0.5
            else:
                toAdd = 1
            
            if not passed:
                leftTotal += toAdd
                leftCoins.append(coin)
            else:
                rightTotal += toAdd
                rightCoins.append(coin)

    if leftTotal < rightTotal:
        for coin in leftCoins:
            if coins[coin] == "?":
                coins[coin] = "L"
            elif coins[coin] == "H":
                coins[coin] = "C"

        for coin in rightCoins:
            if coins[coin] == "?":
                coins[coin] = "H"
            elif coins[coin] == "L":
                coins[coin] = "C"
        
        for coin in allCoins:
            coins[coin] = "C"

    elif leftTotal > rightTotal:
        for coin in leftCoins:
            if coins[coin] == "?":
                coins[coin] = "H"
            elif coins[coin] == "L":
                coins[coin] = "C"

        for coin in rightCoins:
            if coins[coin] == "?":
                coins[coin] = "L"
            elif coins[coin] == "H":
                coins[coin] = "C"
        
        for coin in allCoins:
            coins[coin] = "C"
    
    else:
        for coin in leftCoins:
            coins[coin] = "C"
        for coin in rightCoins:
            coins[coin] = "C"

# MAIN CODE
# ALL COINS, ONE FAKE
coins = {
    "A": "?",
    "B": "?",
    "C": "?",
    "D": "?",
    "E": "?",
    "F": "?",
    "G": "?",
    "H": "?",
    "I": "?",
    "J": "?",
    "K": "?",
    "L": "?"
}

# FAKE COIN DEFINING, YOU NEED TO EDIT THIS TO MOVE THE COUNTERFEIT
# Index position 0 marks which coin to target, position 1 dictates whether it's light or heavy
guessed = False
count = 0

fakeCoin = ["A", "H"]

mode = input("Do you want to set a coin for the bot or do you want the bot to challenge you? (B or ME) ").upper()

if mode == "B":
    useBot = True
else:
    useBot = False

if useBot:
    coin = input("What coin do you want to be fake? ")
    weight = input("What weight will it be? (L or H) ")
    fakeCoin = [coin, weight]
    coinBot()

else:
    fakeCoin = [choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]), choice(["H", "L"])]
    guessed = False
    count = 0

    while not guessed and count <= 2:
        count += 1
        print("A B C D E F G H I J K L")
        print(f"{coins["A"]} {coins["B"]} {coins["C"]} {coins["D"]} {coins["E"]} {coins["F"]} {coins["G"]} {coins["H"]} {coins["I"]} {coins["J"]} {coins["K"]} {coins["L"]}")

        weights = input("Please select the coins you want to balance with a space in between (e.g. ABCD EFGH puts ABCD on the left balance and EFGH on the right)\n> ").upper()
        balance(weights)
        os.system('cls')

        print("A B C D E F G H I J K L")
        print(f"{coins["A"]} {coins["B"]} {coins["C"]} {coins["D"]} {coins["E"]} {coins["F"]} {coins["G"]} {coins["H"]} {coins["I"]} {coins["J"]} {coins["K"]} {coins["L"]}")

        guess = input("What coin do you think it is?\n> ").upper()
        if guess == fakeCoin[0]:
            print("You got it!")
        else:
            print("You didn't get it. Try again!")

    clearCoins()