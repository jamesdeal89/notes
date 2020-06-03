# creates option choices for students at a school
subject = ["biology", "chemistry", "history", "geography", "computer science"]
# bellow are all the lists for the subjects, students names will be appended into them.
biology = []
chemistry = []
history = []
geography = []
computerScience = []
# varibales to be used in future subroutines are stated bellow. records each students choices and name.
choice2 = ''
choice1 = ''
name = ''
# a variable which keeps a record of the total number of completed option choice questions.
completed=0
# a list of every students name to be used to check their total number of subjects.
allNames = []
# a list of subjects to be used in future checks in subroutines.
calculationSubjects=[[biology,"biology"], [chemistry, "chemistry"], [history, "history"], [geography, "geography"], [computerScience, "computer science"]]
# a variable for students with more/less than 2 subjects.
anomalyPupils = []
# a variable to check if free spaces are avalible for unallocated choices.
spareSpacesTotal = 0
unallocatedChoices = 0


def spareSpaces(): 
    print("the number of spare spaces is: ", spareSpacesTotal, " .this will now be checked to see if we can allocate the anomally students with less/more than two choices.")
    print("the number of unallocated students is ", unallocatedChoices)
    # the number of free spaces in other subjects is compared to the number of unallocated extra students
    if spareSpaces < unallocatedChoices:
        print("there is not enough spare spaces for all the unallocated choices.")
    else:
        print("there are enough spaces for the unallocated students!")


def twoSubjects():
    print("Now the program will ensure that a persons name has two subjects. and no less or more")
    # This loop iterates through all the students to check that they all have two subjects. If not they get added to a list.
    for x in range(len(allNames)):
        totalApear = 0
        if allNames[x] in calculationSubjects[0][0]:
            print(allNames[x], " is doing Biology")
            # this variable is used to count how many times their name apears in each subject list.
            totalApear = totalApear + 1

        if allNames[x] in calculationSubjects[1][0]:
            print(allNames[x], " is doing Chemistry")
            totalApear = totalApear + 1

        if allNames[x] in calculationSubjects[2][0]:
            print(allNames[x], " is doing History")
            totalApear = totalApear + 1

        if allNames[x] in calculationSubjects[3][0]:
            print(allNames[x], " is doing Geography")
            totalApear = totalApear + 1

        if allNames[x] in calculationSubjects[4][0]:
            print(allNames[x], " is doing CS")
            totalApear = totalApear + 1

        if totalApear == 2:
            # the number of apearances is checked to ensure the valid number of choices was made.
            print(allNames[x]," is clear, they have exactly two subjects")
            input("press enter to continue")
        else:
            # if the student doesn't have two subjects, they are identified and added to a list.
            print("student ", allNames[x], "has more or less than 2 subjects, he is invalid")
            anomalyPupils.append(allNames[x])
            input("press enter to continue")
        spareSpaces()
    


def checkNumbers():
    print("These numbers will now be assesed to ensure there are no anomallies and correct pupil amounts")
    input("press any key and then enter to continue")
    # iterates over all of the subjects in a for loop.
    for x in calculationSubjects:
        # ensures that the number of students in each subject meets the requirements of over 5, but under 15.
        if len(x[0]) < 5 or len(x[0]) > 15:
            print(x[1], " is not avalible this year, less than 5 pupils or more than 15.")
            if len(x[0]) < 15:
                # here the spare spaces are calculated for the 'spareSpaces()' subroutine. 
                spareSpacesCalc = 15 - len(x[0])
                spareSpacesTotal = spareSpacesTotal + spareSpacesCalc
            if len(x[0]) > 15:
                # here the number of unallocated choices is checked by seeing how many students are over the 15 pupil subject limit
                unallocatedChoices = unallocatedChoices + (len(x[0]) - 15)
            input("press any key and then enter to continue")
    twoSubjects()


def addOneStudent():
    print("one student has been assigned to their two choices of subject")
    print("This will now loop to start for the next student \n current numbers are:")
    # now the program prints the data for each subject including: number of students and names of students.
    print("biology:",len(biology), biology)
    print("chemistry:",len(chemistry), chemistry)
    print("history:",len(history), history)
    print("geography:",len(geography), geography)
    print("computer science:",len(computerScience), computerScience)
    # this is here to ensure that all 40 student's choices are counted before continuing. 
    global completed
    completed = completed + 1
    if completed < 40:
        # the program loops again until all 40 are done.
        start()
    else:
        print("the results are now over, above is the final numbers for all 40")
        checkNumbers()
        



def choicePick2():
    # This subroutine asks the student for their second choice.
    while True:
        choice2 = input("what is your second choice?")
        if choice2 == subject[0]:
                #the students name is added to the subject list and then moves onto the subroutine for looping to the next student.
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
    # here the first choice is accounted for. 
    while True:
        choice1 = input("what is your first choice?")
        if choice1 == subject[0]:
                # students name is added to a list for the subject they chose.
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
            # this prevents invalid inputs.
            print("please choose from the five allowed subject", subject)



def start():
    global name
    for x in subject:
        print(x)
    print("here are the subjects you can choose from. These are case sensitive")
    # this asks for the name of the student and checks it's valid with no numbers.
    while True:
        name = input("what is your name?")
        if name.isalpha():
                # the name is added to the student list.
                allNames.append(name)
                addName1()
        else:
            print("please try again, no numbers in names")         
    else:
        print("invalid input, no numbers in name")

start()



