import sys
instructions = []
finalStates = []
inputs = []

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

instructionInputArray=[]
for z in xrange(0,len(instructions)):
	instructionInputArray.append(instructions[z][0]+instructions[z][1])

instructionDict = {}
for i in xrange(0,len(instructionInputArray)):
	instructionDict[instructionInputArray[i]] = instructions[i]

found=False;
for inputArray in inputs:
	curState = 0
	head = 1
	found = False
	while not found:
		#get the instruction based on the current state and value of inputArray[head]
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
	print "".join(inputArray[1:len(inputArray)-1])
	if str(curState) in finalStates[0]:
		print "ACCEPTED"
	else:
		print "REJECTED"