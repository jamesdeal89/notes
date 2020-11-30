#bottle song

bottle = 9

while bottle > 0:
    print(str(bottle) + " green bottles sitting on the wall \n" + str(bottle) + " green bottles sitting on the wall \n" "and if one green bottle should accidentally fall. \n")
    bottle -= 1
    if bottle > 0:
        print("there will be " + str(bottle) + "green bottle sitting on the wall.")
    elif bottle == 0:
        print("there are no green bottles sitting on the wall")
	
