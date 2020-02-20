# asks for slab specs and then prices it
import math
print("Hello and welcome to SLAB. We make slabs."
      "\nplease answer the following questions on your ideal slab"
      "\nthank you using SLAB today.")

Pi = 3.14


def areaofslab():
    userData[1] = int(userData[1])
    if userData[2] == "square":
        while True:
            AorB = (input(
                "What are the dimensions of the slab you would like (A)600*600 or (B)450*450, letter only").lower())
            if AorB == "a":
                return userData[1] * 600 * 600
            elif AorB == "b":
                return userData[1] * 450 * 450
            else:
                print("only write 'A' or 'B', please try again")
    if userData[2] == "rectangle":
        while True:
            AorB = (input(
                "What are the dimensions of the slab you would like (A)600*700 or (B)600*450, letter only").lower())
            if AorB == "a":
                return userData[1] * 600 * 700
            elif AorB == "b":
                return userData[1] * 600 * 450
            else:
                print("only write 'A' or 'B', please try again")
    if userData[2] == "round":
        while True:
            AorB = (input("What is the diameter you would like (A) 300 or (B) 450").lower())
            if AorB == "a":
                return Pi * 150 ** 2 * userData[1]
            if AorB == "b":
                return Pi * 225 ** 2 * userData[1]
            else:
                print("only write 'A' or 'B', try again")


def gradeOfSlab():
    if userData[0] == "grey":
        while True:
            gradeIs = input("What grade of slab would you like?('basic', no increase, or 'best', 7% more)")
            if gradeIs == "best":
                return basePrice * 1.07
            elif gradeIs == "basic":
                return basePrice
            else:
                print("incorrect input, only do 'basic' or 'best'. try again")
    return basePrice



def finalPrice():
    print("The price will be calculated for you SLAB slab now")
    global basePrice
    basePrice = userData[3] / 100000 * 5
    if userData[0] == "red" or userData == "green":
        basePrice = basePrice * 1.1
    elif userData[0] == "custom":
        basePrice = basePrice + 500
        basePrice = basePrice * 1.15
    basePrice = gradeOfSlab()
    dollarPrice = basePrice / 100
    batchPrice = dollarPrice * 20
    print("Your slabs will be charged at $", batchPrice, " for a batch of 20")
    while True:
        batchNumber = int(input("How many slabs would you like? 20-100"))
        if batchNumber < 20 or batchNumber > 100:
            print("please try again, less than 20 and more than 100 will not be accepted.")
        if 100 > batchNumber > 20:
            roundedBatchNumber = math.ceil(batchNumber / 20)
            finalFinalOrder = batchPrice * roundedBatchNumber
            print("the price for your order will be $", finalFinalOrder, "which will be for ", roundedBatchNumber, "set(s) of 20")
            exit()
        else:
            print("please try again")


while True:
    print("please choose from the following colours:\n"
          "Grey\n"
          "Red\n"
          "Green\n"
          "Custom")
    userData = [input("Please type the colour of your choice:").lower()]
    if userData[0] == "grey":
        print("You have chosen Grey")
        while True:
            userData.append(input("Please input your slab depth(either 38 or 45, digits only):"))
            if userData[1] == "38":
                print("You have chosen " + str(userData[1]) + " slab depth for your " + str(userData[0]) + " slab")
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            if userData[1] == "45":
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            else:
                print("please try again, only use digits and one or the other.")
    if userData[0] == "red":
        print("You have chosen Red")
        while True:
            userData.append(input("Please input your slab depth(either 38 or 45, digits only):"))
            if userData[1] == "38":
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            if userData[1] == "45":
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            else:
                print("please try again, only use digits and one or the other.")
    if userData[0] == "green":
        print("You have chosen Green")
        while True:
            userData.append(input("Please input your slab depth(either 38 or 45, digits only):"))
            if userData[1] == "38":
                print("You have chosen " + str(userData[1]) + " slab depth for your " + str(userData[0]) + " slab")
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            if userData[1] == "45":
                print("You have chosen " + str(userData[1]) + " slab depth for your " + str(userData[0]) + " slab")
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            else:
                print("please try again, only use digits and one or the other.")
    if userData[0] == "custom":
        print("You have chosen Custom")
        while True:
            userData.append(input("Please input your slab depth(either 38 or 45, digits only):"))
            if userData[1] == "38":
                print("You have chosen " + str(userData[1]) + " slab depth for your " + str(userData[0]) + " slab")
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            if userData[1] == "45":
                print("You have chosen " + str(userData[1]) + " slab depth for your " + str(userData[0]) + " slab")
                while True:
                    userData.append(
                        input("Now, please enter you slab shape (either square or rectangle or round)").lower())
                    if userData[2] == "square":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "rectangle":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    elif userData[2] == "round":
                        print("You have chosen a " + str(userData[0]) + " slab with a depth of " + str(
                            userData[1]) + " and a shape of " + str(userData[2]))
                        areaOfDimension = areaofslab()
                        userData.append(areaOfDimension)
                        finalPrice()
                    else:
                        print("Please select either rectangle or square, please retry")
            else:
                print("please try again, only use digits and one or the other.")
    else:
        print("That is not a colour from the menu, please try again.")
