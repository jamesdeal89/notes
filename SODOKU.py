#sodoku solver

sodoku = [
[1,0,0,4],
[0,2,1,0],
[3,0,0,2],
[2,0,3,0],
]

emptySqaures = []

def sodokuSolver():
        # runs for each item in the sodoku, whilst also finding the location in the list
	for i, row in enumerate(sodoku):
		for j, col  in enumerate(row):
			if col == 0:   
                            # adds empty sqaures to a list
                            location = [i,j]
                            emptySqaures.append(location)
sodokuSolver()

print(emptySqaures)
			
		
	
