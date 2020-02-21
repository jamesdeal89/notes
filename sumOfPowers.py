#finds a three digit number that is the sum of it's digits cubed

start = "100"
end = 999
found = []

while int(start) <= end:
    #separates them into 3 individual digits
    digit1=str(start)[0]
    digit2=str(start)[1]
    digit3=str(start)[2]
    start = int(start)
    print(digit1, digit2, digit3)
    digit1=int(digit1)
    digit2=int(digit2)
    digit3=int(digit3)
    if digit1**3 + digit2**3 + digit3**3 == start:
        found.append(start)
        start = start + 1
    else:
        start = start + 1

print(found)
