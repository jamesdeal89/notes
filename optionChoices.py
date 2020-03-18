#creates option choices for students at a school
subject = ["biology", "chemistry", "history", "geography", "computer science"]
biology = []
chemistry = []
history = []
geography = []
computerScience = []

def addOneStudent():
    print("one student has been assigned to their two choices of subject")
    print("This will now loop to start for the next student")

def addName2():
    if choice2 == subject[0] or subject[1] or subject[2] or subject[3] or subject[4]:
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

def choicePick2():
    While True:
        choice2 = input("what is your second choice?")
        addName2()


def addName1():
    if choice1 == subject[0] or subject[1] or subject[2] or subject[3] or subject[4]:
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



def start():
    while True:
    name = input("what is your name?")
    if name.isalpha():
        while True:
            choice1 = input("what is your first choice?")
            addName()
            else:
                print("please try again")         
    else:
        print("invalid input, no numbers in name")

for x in range(1,40):
    start()

print(len(biology))
print(len(chemistry))
print(len(history))
print(len(Geography))
print(len(computerScience))
