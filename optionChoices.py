#creates option choices for students at a school
subject = ["biology", "chemistry", "history", "geography", "computer science"]
biology = []
chemistry = []
history = []
geography = []
computerScience = []
while True:
    name = input("what is your name?")
    if name.isalpha():
        choice1 = input("what is your first choice?")
        choice2 = input("what is your second choice?")
    else:
        print("invalid input, no numbers in name")

    
