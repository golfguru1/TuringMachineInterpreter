import sys
instructions = []
finalStates = []
inputs = []

#populate the list of instructions, final states and inputs
for line in sys.stdin:
    a = line.strip("\r\n").split(" ")
    if(a[0]=='t'):
    	instructions.append(a[1:])
    elif (a[0]=='f'):
    	finalStates.append(a[1:])
    elif(a[0]=='i'):
    	myList=list(line.strip("\r\n"))[2:]
    	myList.insert(0,"Z")
    	myList.append("Z")
    	inputs.append(myList)
print inputs
#get the list of all current state and input symbol combinations
instructionInputArray=[]
for z in xrange(0,len(instructions)):
	instructionInputArray.append(instructions[z][0]+instructions[z][1])

#use the above array to make a dictionary that maps each currentState+inputSymbol to the corresponding insruction
instructionDict = {}
for i in xrange(0,len(instructionInputArray)):
	instructionDict[instructionInputArray[i]] = instructions[i]

found=False;
#loop through every input line
for inputArray in inputs:
	#reset the current state and head for each set of inputs
	curState = 0
	head = 1
	found = False
	#loop until a Halt instruction is found, until there is no transition or until we reach a final state
	while not found:
		#get the instruction based on the current state and value of inputArray at the current head
		if(str(curState)+inputArray[head] in instructionInputArray):
			instructionSet = instructionDict.get(str(curState)+inputArray[head])
			curState=instructionSet[2]
			inputArray[head]=instructionSet[3]
			if(instructionSet[4]=='R'):
				head+=1
			elif (instructionSet[4]=='L'):
				head-=1
			elif (instructionSet[4]=='H'):
				found=True;
		else:
			found=True;
		if str(curState) in finalStates[0]:
			found=True
	#print the resulting input string
	print "".join(inputArray[1:len(inputArray)-1])
	#if the ending state is in the list of accepting state, print ACCEPTED
	if str(curState) in finalStates[0]:
		print "ACCEPTED"
	#otherwise print REJECTED
	else:
		print "REJECTED"