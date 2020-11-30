#sodoku solver easy version 1*1
import random
sodoku = []
def solver():
    if sodoku[0] == 0:
        sodoku[0] = 1
        print("sodoku is solved, answer is:")
        print(sodoku)
        exit()
    elif sodoku[0] == 1:
        print("sodoku is already solved, answer is:")
        print(sodoku)
        exit()

while True:
    choice = input("would you like a random sodoku?:(Y/N)")
    if choice == "Y":
        number = random.randint(0, 1)
        sodoku.append(number)
        print("your generated sodoku is:")
        print(sodoku)
        solver()
    elif choice == "N":
        number = input("What is the number for row 1 coloum 1?:")
        sodoku.append(int(number))
        solver()
    else:
        print("incorrect input")
