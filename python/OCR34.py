# OCR challenge 34 - what's the day?
print("this program checks whether a given date is possible and correct \n please give the details of the date when asked:")
day = input("what is the day?(xx fomat e.g 07)")
month = input("what is the month? (xx format e.g 02)")
year = input("what is the year?(xxxx format e.g 2004)")
monthLengths = [31,28,31,30,31,30,31,31,30,31,30,31]

# let's just say the date is correct for now and find ways to invalidate it
realDate = True

# first check will be that the length of the month and day is two digits and that the year is four digits.
if realDate == True:
    if len(day) != 2:
        realDate = False
    elif len(month) != 2:
        realDate = False
    elif len(year) != 4:
        realDate = False

# before we do this we need to check if it's a leap year or not as that affects if the date is correct or not. I'm using an eqaution I stole from the Microsoft website.
leap = (int(year) % 400 == 0) or (int(year) % 4 == 0 and int(year) % 100 != 0)

# next we will check that the number of days in that given month is no greater tthan the number which that month has. In addition, the month cannot be greater than 12
if realDate == True:
    if int(day) > monthLengths[int(month)-1]:
        if int(month) == 2 and leap == True and int(day) == 29:
            realDate = True
        else:
            realDate = False
        
    elif int(month) > 12:
        realDate = False

# tells the user if the date is real
if realDate:
    print("the date you gave me was legit")
if realDate == False:
    print("the date you gave me was false")


if realDate:

    YearCode = (int(year[3:4]) + (int(year[3:4]) / 4)) % 7
    MonthCodeList = [0,3,3,6,1,4,6,2,5,0,3,5]
    MonthCode = MonthCodeList[int(month)-1]
    CenturyCodeList = [4,2,0,6,4,2,0]
    firstYear = year[0:2]
    if firstYear == "17":
        CenturyCode = CenturyCodeList[0]
    elif firstYear == "18":
        CenturyCode = CenturyCodeList[1]
    elif firstYear == "19":
        CenturyCode = CenturyCodeList[2]
    elif firstYear == "20":
        CenturyCode = CenturyCodeList[3]
    if leap:
        LeapYearCode = 1
    else:
        LeapYearCode = 0
    # this is an equation to find the day of the week.
    WEEKDAY = ((YearCode + MonthCode + CenturyCode + int(day) - LeapYearCode) % 7) -2
    if WEEKDAY == 0:
        WEEKDAYconv = "Sunday"
    elif WEEKDAY == 1:
        WEEKDATconv = "Monday"
    elif WEEKDAY == 2:
        WEEKDATconv = "Tuesday"
    elif WEEKDAY == 3:
        WEEKDATconv = "Wednesday"
    elif WEEKDAY == 4:
        WEEKDATconv = "Thursday"
    elif WEEKDAY == 5:
        WEEKDATconv = "Friday"
    elif WEEKDAY == 6:
        WEEKDATconv = "Saturday"
    print("The weekday for that date is " + str(WEEKDATconv))
