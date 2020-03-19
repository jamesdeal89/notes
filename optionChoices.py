#creates option choices for students at a school
subject = ["biology", "chemistry", "history", "geography", "computer science"]
biology = []
chemistry = []
history = []
geography = []
computerScience = []
choice2 = ''
choice1 = ''
name = ''
completed=0
calculationSubjects=[[biology,"biology"], [chemistry, "chemistry"], [history, "history"], [geography, "geography"], [computerScience, "computer science"]]


def nextStage():
    print("bye bye")
    input()
    exit()


def checkNumbers():
    print("These numbers will now be assesed to ensure there are no anomallies and correct pupil amounts")
    input("press any key and then enter to continue")
    for x in calculationSubjects:
        if len(x[0]) < 5:
            print(x[1], " is not avalible this year, less than 5 pupils")
            input("press any key and then enter to continue")
            nextStage()
            


def addOneStudent():
    print("one student has been assigned to their two choices of subject")
    print("This will now loop to start for the next student \n current numbers are:")
    print("biology:",len(biology), biology)
    print("chemistry:",len(chemistry), chemistry)
    print("history:",len(history), history)
    print("geography:",len(geography), geography)
    print("computer science:",len(computerScience), computerScience)
    global completed
    completed = completed + 1
    if completed < 40:
        start()
    else:
        print("the results are now over, above is the final numbers for all 40")
        checkNumbers()
        



def choicePick2():
    while True:
        choice2 = input("what is your second choice?")
        if choice2 == subject[0]:
                biology.append(name)
                addOneStudent()
        elif choice2 == subject[1]:
                chemistry.append(name)
                addOneStudent()
        elif choice2 == subject[2]:
                history.append(name)
                addOneStudent()
        elif choice2 == subject[3]:
                geography.append(name)
                addOneStudent()
        elif choice2 == subject[4]:
                computerScience.append(name)
                addOneStudent()
        else:
            print("invalid second choice, case sensitive, please retry. only these are allowed", subject)


def addName1():
    while True:
        choice1 = input("what is your first choice?")
        if choice1 == subject[0]:
                biology.append(name)
                choicePick2()
        elif choice1 == subject[1]:
                chemistry.append(name)
                choicePick2()
        elif choice1 == subject[2]:
                history.append(name)
                choicePick2()
        elif choice1 == subject[3]:
                geography.append(name)
                choicePick2()
        elif choice1 == subject[4]:
                computerScience.append(name)
                choicePick2()
        else:
            print("please choose from the five allowed subject", subject)



def start():
    global name
    for x in subject:
        print(x)
    print("here are the subjects you can choose from. These are case sensitive")
    while True:
        name = input("what is your name?")
        if name.isalpha():
                addName1()
        else:
            print("please try again, no numbers in names")         
    else:
        print("invalid input, no numbers in name")

start()



