processor = [["p3", 100], ["p5", 120], ["p7", 200]]
RAM = [["16GB", 75], ["32GB", 150]]
storage = [["1TB", 50], ["2TB", 100]]
screen = [["19 inch", 65], ["23 inch", 120]]
case = [["mini tower", 40], ["midi tower", 70]]
usbPorts = [["2 ports", 10], ["4 ports", 20]]
userData = []
estimateNumber = 0
listOfEstimateNumber = []


def priceEstimate():
    global estimateNumber
    estimateNumber = estimateNumber + 1
    listOfEstimateNumber.append(estimateNumber)
    print("Your estimate number is #", estimateNumber)
    finalPrice = userData[0][1] + userData[1][1] + userData[2][1] + userData[3][1] + userData[4][1] + userData[5][1]
    print("Your estimate for this build will be $", finalPrice * 1.2, "including the 20% build fee.")
    while True:
        restart = input("would you like to create another build? (y/n)")
        if restart == "y":
            start()
        elif restart == "n":
            exit()
        else:
            print("please try again, only 'y' or 'n' in lower case")




def usbPortsq():
    while True:
        question5 = input("what is the number of usb ports you would like? ('2' or '4')")
        if question5 == "2":
            userData.append(usbPorts[0])
            priceEstimate()
        if question5 == "4":
            userData.append(usbPorts[1])
            priceEstimate()
        else:
            print("please try again, only type either or.")


def caseq():
    while True:
        question4 = input("what is the case type you would like? ('mini tower' or 'midi tower')")
        if question4 == "mini tower":
            userData.append(case[0])
            usbPortsq()
        elif question4 == "midi tower":
            userData.append(case[1])
            usbPortsq()
        else:
            print("please try again, only type either or for each option in lower case.")


def screenq():
    while True:
        question3 = input("what is the size of the screen you would like?('19 inch' or '23 inch'):")
        if question3 == "19 inch":
            userData.append(screen[0])
            caseq()
        elif question3 == "23 inch":
            userData.append(screen[1])
            caseq()
        else:
            print("please enter only either '19 inch' or '23 inch'")



def storageq():
    while True:
        question2 = input("what amount of storage would you like?(1tb or 2tb):")
        if question2 == "1tb":
            userData.append(storage[0])
            screenq()
        elif question2 == "2tb":
            userData.append(storage[1])
            screenq()
        else:
            print("That is not an option, please only enter in lowercase")


def ramq():
    while True:
        question1 = input("What amount of RAM would you like?(16gb or 32gb):")
        if question1 == "16gb":
            userData.append(RAM[0])
            storageq()
        elif question1 == "32gb":
            userData.append(RAM[1])
            storageq()
        else:
            print("That's not an option, please retry with only the choices given in lower case")


def start():
    while True:
        question = input("what processor would you like for your system?(p3,p5,p7):").lower()
        if question == "p3":
            userData.append(processor[0])
            ramq()
        elif question == "p5":
            userData.append(processor[1])
            ramq()
        elif question == "p7":
            userData.append(processor[2])
            ramq()
        else:
            print("that is not an option, please type only the choices listed.")


start()