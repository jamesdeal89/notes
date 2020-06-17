positiveNumbers = 0
zeroNumbers = 0
countdown = 1000

while countdown > 1:
    chosen = int(input("input number"))
    if chosen == 0:
        zeroNumbers = zeroNumbers + 1
    elif chosen > 0:
        positiveNumbers = positiveNumbers + 1
    countdown = countdown -1


print("zeros: " + str(zeroNumbers))
print("positives: " + str(positiveNumbers))
