# the Algorithm
##function BREADTH-FIRST-SEARCH(initState, goalTest)
##	returns SUCCESS or FAILURE:
##	frontier = Queue.new(initialState)
##	explored = Set.new()
##	
##	while not froniter.isEmpty():
##		state = frontier.dequeue()
##		explored.add(state)
##
##		if goalTest(state):
##			return SUCCESS(state)
##
##		for neighbor in state.neighbors():
##			if neighbor not in fronter or explored:
##				frontier.enqueue(neighbor)
##
##	return FAILURE


from sets import Set
from collections import deque
from sys import argv

script, mode, initState = argv
exploredSet = set()
path_to_goal = deque()
nodes_expanded = 0

goalState = '0,1,2,3,4,5,6,7,8'

class PuzzleState(object):
    
    def __init__(self):
        print "init PuzzleState"
    def setParentState(state):
        self.parentState = state
    def getParentState():
        return self.parentState
    def setParentAction(action):
        self.parentAction = action
    def getParentAction():
        return self.parentAction

    def setStateString(str):
        self.stateString = str
    def getStateString():
        return self.stateString

    
    def expandNeighbor(state):
        nDeque = deque()
        lists = newState.split(',')
        
        print "newstate is %s", newState
        print "the list is %s", lists
        rDeque = deque()
        if (int(lists[0])==0):
            #For RIGHT MOVE
            tmpLists1 = list(lists)
            tmpLists1[0]=lists[1]
            tmpLists1[1]='0'
            stateR = PuzzleState()
            stateR.setParentState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists1))
            # For DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[0]=lists[3]
            tmpLists2[3]='0'
            stateD = PuzzleState()
            stateD.setParentState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
        elif (int(lists[1])==0):
            #FOR LEFT MOVE
            tmpLists1 = list(lists)
            tmpLists1[1]=lists[0]
            tmpLists1[0]='0'
            stateL = PuzzleState()
            stateL.setParentState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists1))
            # FOR RIGHT MOVE
            tmpLists2 = list(lists)
            tmpLists2[1]=lists[2]
            tmpLists2[2]='0'
            stateR = PuzzleState()
            stateR.setParentState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists2))
            # FOR DOWN MOVE
            tmpLists3 = list(lists)
            tmpLists3[1]=lists[4]
            tmpLists3[4]='0'
            stateD = PuzzleState()
            stateD.setParentState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists3))
        elif (int(lists[2])==0):
            #FOR LEFT MOVE
            tmpLists1 = list(lists)
            tmpLists1[2]=lists[1]
            tmpLists1[1]='0'
            stateL = PuzzleState()
            stateL.setParentState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists1))
            # FOR DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[2]=lists[5]
            tmpLists2[5]='0'
            stateD = PuzzleState()
            stateD.setParentState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
        elif (int(lists[3])==0):
            #For RIGHT MOVE
            tmpLists1 = list(lists)
            tmpLists1[3]=lists[4]
            tmpLists1[4]='0'
            stateR = PuzzleState()
            stateR.setParentState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists1))
            # For DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[3]=lists[6]
            tmpLists2[6]='0'
            stateD = PuzzleState()
            stateD.setParentState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
            # For UP MOVE
            tmpLists3 = list(lists)
            tmpLists3[3]=lists[0]
            tmpLists3[0]='0'
            stateU = PuzzleState()
            stateU.setParentState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists3))
        elif (int(lists[4])==0):
            #For RIGHT MOVE
            tmpLists1 = list(lists)
            tmpLists1[4]=lists[5]
            tmpLists1[5]='0'
            stateR = PuzzleState()
            stateR.setParentState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists1))
            # For DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[4]=lists[7]
            tmpLists2[7]='0'
            stateD = PuzzleState()
            stateD.setParentState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
            # For UP MOVE
            tmpLists3 = list(lists)
            tmpLists3[4]=lists[1]
            tmpLists3[1]='0'
            stateU = PuzzleState()
            stateU.setParentState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists3))
            # For LEFT MOVE
            tmpLists4 = list(lists)
            tmpLists4[4]=lists[3]
            tmpLists4[3]='0'
            stateL = PuzzleState()
            stateL.setParentState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists4))
            
        elif (int(lists[5])==0):
            # For LEFT MOVE
            tmpLists1 = list(lists)
            tmpLists1[5]=lists[4]
            tmpLists1[4]='0'
            nDeque.append(",".join(tmpLists1))
            stateL = PuzzleState()
            stateL.setParentState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists1))
            # For UP MOVE
            tmpLists2 = list(lists)
            tmpLists2[5]=lists[2]
            tmpLists2[2]='0'
            stateU = PuzzleState()
            stateU.setParentState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists2))
            # For DOWN MOVE
            tmpLists3 = list(lists)
            tmpLists3[5]=lists[8]
            tmpLists3[8]='0'
            stateD = PuzzleState()
            stateD.setParentState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists3))
            rDeque.append(stateL,stateU,stateD)
        elif (int(lists[6])==0):
            # For UP MOVE
            tmpLists1 = list(lists)
            tmpLists1[6]=lists[3]
            tmpLists1[3]='0'
            stateU = PuzzleState()
            stateU.setParentState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists1))
            # For RIGHT MOVE
            tmpLists2 = list(lists)
            tmpLists2[6]=lists[7]
            tmpLists2[7]='0'
            stateR = PuzzleState()
            stateR.setParentState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists2))
            rDeque.append(stateU,stateD)

        elif (int(lists[7])==0):
            # For UP MOVE
            tmpLists1 = list(lists)
            tmpLists1[7]=lists[4]
            tmpLists1[4]='0'
            stateU = PuzzleState()
            stateU.setParentState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists1))
            # For LEFT MOVE
            tmpLists2 = list(lists)
            tmpLists2[7]=lists[6]
            tmpLists2[6]='0'
            stateL = PuzzleState()
            stateL.setParentState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists2))
            # For RIGHT MOVE
            tmpLists3 = list(lists)
            tmpLists3[7]=lists[8]
            tmpLists3[8]='0'
            stateR = PuzzleState()
            stateR.setParentState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists3))
        elif (int(lists[8])==0):
            # For UP MOVE
            tmpLists1 = list(lists)
            tmpLists1[8]=lists[5]
            tmpLists1[5]='0'
            stateU = PuzzleState()
            stateU.setParentState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists1))

            # For LEFT MOVE
            tmpLists2 = list(lists)
            tmpLists2[8]=lists[7]
            tmpLists2[7]='0'
            stateL = PuzzleState()
            stateL.setParentState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists2))

        print "nDeque is %s", nDeque
        rDeque = deque()
        for duplicateItem in nDeque:
            if (duplicateItem in exploredSet):
                print "remove one dupliate item %s", duplicateItem
            else:
                rDeque.append(duplicateItem)
        print "rDeque is %s", rDeque
        return rDeque



def start(mode, initState):
    print "the mode is %s", mode
    print "the initState is %s", initState

    frontierQueue = deque()
    frontierQueue.append(initState)
    

    # check frontierQueue= empty
    n=0
    while len(frontierQueue)>0:

        newState = frontierQueue.popleft()
        exploredSet.add(newState)

        if (newState == goalState):
            print path_to_goal
            print n
            return True
        print "in loop %s", newState
        print "The frontierQueue %s", frontierQueue
        n = n + 1
        neighborsState = getStateNeighbor(newState)
        #TODO to check this local var nodes_expanded error
        #nodes_expanded = nodes_expanded + len(neighborsState)
        for neighborItem in neighborsState:
            inF = not (frontierQueue.count(neighborItem)>0)
            inEx = not (neighborItem in exploredSet)
            if (inF and inEx):
                frontierQueue.append(neighborItem)

    return False
start(mode,initState)
