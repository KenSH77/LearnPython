
from sets import Set
from collections import deque
from sys import argv
import time

script, mode, initState = argv

path_to_goal = deque()

frontierQueue = deque()
exploredSet = set()

strgoalState = '0,1,2,3,4,5,6,7,8'



class PuzzleState(object):
    nodes_expanded = 0
    cost_of_path = 0
    fringe_size = 0
    def __init__(self, stateStr):
        print "init PuzzleState"
        self.stateString = stateStr
        self.parentAction = ''
        self.parentState = ''
        self.parentClassState = None
    def setParentState(self, state):
        self.parentState = state
    def setParentAction(self, action):
        self.parentAction = action
    def setStateString(self, str1):
        self.stateString = str1
    def setParentClassState(self, state):
        self.parentClassState = state

    def retrieveResult(self, state):
        print "printing result"
        rAction = ''
        while (state.parentClassState != None):
            PuzzleState.cost_of_path = PuzzleState.cost_of_path + 1
            rAction = "'" + state.parentAction + "'" + rAction
            state = state.parentClassState
        return rAction
    
    def expandNeighbor(self, state):
        print "entering in parent expanding %s", state.stateString
        nDeque = deque()
        rDeque = deque()
        lists = state.stateString.split(',')
        print "the list is %s", lists
        
        if (int(lists[0])==0):
            # For DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[0]=lists[3]
            tmpLists2[3]='0'
            stateD = PuzzleState(",".join(tmpLists2))
            stateD.setParentClassState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
            nDeque.append(stateD)
            #For RIGHT MOVE
            tmpLists1 = list(lists)
            tmpLists1[0]=lists[1]
            tmpLists1[1]='0'
            stateR = PuzzleState(",".join(tmpLists1))
            stateR.setParentClassState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists1))
            nDeque.append(stateR)
        elif (int(lists[1])==0):
            # FOR DOWN MOVE
            tmpLists3 = list(lists)
            tmpLists3[1]=lists[4]
            tmpLists3[4]='0'
            stateD = PuzzleState(",".join(tmpLists3))
            stateD.setParentClassState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists3))
            nDeque.append(stateD)            
            #FOR LEFT MOVE
            tmpLists1 = list(lists)
            tmpLists1[1]=lists[0]
            tmpLists1[0]='0'
            stateL = PuzzleState(",".join(tmpLists1))
            stateL.setParentClassState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists1))
            nDeque.append(stateL)
            # FOR RIGHT MOVE
            tmpLists2 = list(lists)
            tmpLists2[1]=lists[2]
            tmpLists2[2]='0'
            stateR = PuzzleState(",".join(tmpLists2))
            stateR.setParentClassState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists2))
            nDeque.append(stateR)
        elif (int(lists[2])==0):
            # FOR DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[2]=lists[5]
            tmpLists2[5]='0'
            stateD = PuzzleState(",".join(tmpLists2))
            stateD.setParentClassState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
            nDeque.append(stateD)
            #FOR LEFT MOVE
            tmpLists1 = list(lists)
            tmpLists1[2]=lists[1]
            tmpLists1[1]='0'
            stateL = PuzzleState(",".join(tmpLists1))
            stateL.setParentClassState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists1))
            nDeque.append(stateL)
        elif (int(lists[3])==0):
            # For UP MOVE
            tmpLists3 = list(lists)
            tmpLists3[3]=lists[0]
            tmpLists3[0]='0'
            stateU = PuzzleState(",".join(tmpLists3))
            stateU.setParentClassState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists3))
            nDeque.append(stateU)

            # For DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[3]=lists[6]
            tmpLists2[6]='0'
            stateD = PuzzleState(",".join(tmpLists2))
            stateD.setParentClassState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
            nDeque.append(stateD)
            #For RIGHT MOVE
            tmpLists1 = list(lists)
            tmpLists1[3]=lists[4]
            tmpLists1[4]='0'
            stateR = PuzzleState(",".join(tmpLists1))
            stateR.setParentClassState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists1))
            nDeque.append(stateR)
        elif (int(lists[4])==0):
            # For UP MOVE
            tmpLists3 = list(lists)
            tmpLists3[4]=lists[1]
            tmpLists3[1]='0'
            stateU = PuzzleState(",".join(tmpLists3))
            stateU.setParentClassState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists3))
            nDeque.append(stateU)
            # For DOWN MOVE
            tmpLists2 = list(lists)
            tmpLists2[4]=lists[7]
            tmpLists2[7]='0'
            stateD = PuzzleState(",".join(tmpLists2))
            stateD.setParentClassState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists2))
            nDeque.append(stateD)
            # For LEFT MOVE
            tmpLists4 = list(lists)
            tmpLists4[4]=lists[3]
            tmpLists4[3]='0'
            stateL = PuzzleState(",".join(tmpLists4))
            stateL.setParentClassState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists4))
            nDeque.append(stateL)
            #For RIGHT MOVE
            tmpLists1 = list(lists)
            tmpLists1[4]=lists[5]
            tmpLists1[5]='0'
            stateR = PuzzleState(",".join(tmpLists1))
            stateR.setParentClassState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists1))
            nDeque.append(stateR)
        elif (int(lists[5])==0):
            # For UP MOVE
            tmpLists2 = list(lists)
            tmpLists2[5]=lists[2]
            tmpLists2[2]='0'
            stateU = PuzzleState(",".join(tmpLists2))
            stateU.setParentClassState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists2))
            nDeque.append(stateU)
            # For DOWN MOVE
            tmpLists3 = list(lists)
            tmpLists3[5]=lists[8]
            tmpLists3[8]='0'
            stateD = PuzzleState(",".join(tmpLists3))
            stateD.setParentClassState(state)
            stateD.setParentAction('Down')
            stateD.setStateString(",".join(tmpLists3))
            nDeque.append(stateD)
            # For LEFT MOVE
            tmpLists1 = list(lists)
            tmpLists1[5]=lists[4]
            tmpLists1[4]='0'
            stateL = PuzzleState(",".join(tmpLists1))
            stateL.setParentClassState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists1))
            nDeque.append(stateL)
        elif (int(lists[6])==0):
            # For UP MOVE
            tmpLists1 = list(lists)
            tmpLists1[6]=lists[3]
            tmpLists1[3]='0'
            stateU = PuzzleState(",".join(tmpLists1))
            stateU.setParentClassState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists1))
            nDeque.append(stateU)

            # For RIGHT MOVE
            tmpLists2 = list(lists)
            tmpLists2[6]=lists[7]
            tmpLists2[7]='0'
            stateR = PuzzleState(",".join(tmpLists2))
            stateR.setParentClassState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists2))
            nDeque.append(stateR)
        elif (int(lists[7])==0):
            # For UP MOVE
            tmpLists1 = list(lists)
            tmpLists1[7]=lists[4]
            tmpLists1[4]='0'
            stateU = PuzzleState(",".join(tmpLists1))
            stateU.setParentClassState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists1))
            nDeque.append(stateU)

            # For LEFT MOVE
            tmpLists2 = list(lists)
            tmpLists2[7]=lists[6]
            tmpLists2[6]='0'
            stateL = PuzzleState(",".join(tmpLists2))
            stateL.setParentClassState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists2))
            nDeque.append(stateL)

            # For RIGHT MOVE
            tmpLists3 = list(lists)
            tmpLists3[7]=lists[8]
            tmpLists3[8]='0'
            stateR = PuzzleState(",".join(tmpLists3))
            stateR.setParentClassState(state)
            stateR.setParentAction('Right')
            stateR.setStateString(",".join(tmpLists3))
            nDeque.append(stateR)

        elif (int(lists[8])==0):
            # For UP MOVE
            tmpLists1 = list(lists)
            tmpLists1[8]=lists[5]
            tmpLists1[5]='0'
            stateU = PuzzleState(",".join(tmpLists1))
            stateU.setParentClassState(state)
            stateU.setParentAction('Up')
            stateU.setStateString(",".join(tmpLists1))
            nDeque.append(stateU)

            # For LEFT MOVE
            tmpLists2 = list(lists)
            tmpLists2[8]=lists[7]
            tmpLists2[7]='0'
            stateL = PuzzleState(",".join(tmpLists2))
            stateL.setParentClassState(state)
            stateL.setParentAction('Left')
            stateL.setStateString(",".join(tmpLists2))
            nDeque.append(stateL)

        print "nDeque is %s", nDeque
        for ittem in nDeque:
            if (ittem.stateString in exploredSet):
                print ""
            else:
                rDeque.append(ittem)
##        print "rDeque is %s", rDeque
        for ittem in rDeque: print "item in rdeque %s", ittem.stateString
        for ittem2 in exploredSet: print "item in exploredSet %s", ittem2
        return rDeque


def start(mode, initState):
    print "the mode is %s", mode
    print "the initState is %s", initState

    if (mode=="bfs"):
        startBFS(initState)
    elif (mode=="dfs"):
        startDFS(initState)

def startBFS(initState):
    print "the initState is %s", initState
    
    _firstState = PuzzleState(initState)
    frontierQueue.append(_firstState)
    
    max_fringe_size = 0
    start_time = time.time()
    while len(frontierQueue)>0:
        max_fringe_size = max(max_fringe_size, len(frontierQueue))
        newState = frontierQueue.popleft()
        exploredSet.add(newState.stateString)

        if (newState.stateString == strgoalState):
            print "path to nodes_expanded, costofpath, size of frontierqueue, max fringesize"
            print "The fringe size is %s", len(frontierQueue)
            print PuzzleState.nodes_expanded
            print len(frontierQueue)
            print max_fringe_size
            print "The Action List is \n"
            print newState.retrieveResult(newState)
            print PuzzleState.cost_of_path
            print("Running Time--- %s seconds ---" % (time.time() - start_time))
            return True

        PuzzleState.nodes_expanded = PuzzleState.nodes_expanded + 1
        neighborsStateL = newState.expandNeighbor(newState)
        for neighborItem in neighborsStateL:
            inF = not (frontierQueue.count(neighborItem)>0)
            inEx = not(neighborItem.stateString in exploredSet)
            if (inF and inEx):
                frontierQueue.append(neighborItem)
    return False

def startDFS(initState):
    print "the DFS initState is %s", initState
    
    _firstState = PuzzleState(initState)
    frontierQueue.appendleft(_firstState)
    
    max_fringe_size = 0
    start_time = time.time()
    n = 0
    while len(frontierQueue)>0:
        n = n + 1
        for aitem in frontierQueue: print "frontierQueue Stack is - %s", aitem.stateString
        
        max_fringe_size = max(max_fringe_size, len(frontierQueue))
        newState = frontierQueue.popleft()
        exploredSet.add(newState.stateString)

        if (newState.stateString == strgoalState):
            print "path to nodes_expanded, costofpath, size of frontierqueue, max fringesize"
            print "The fringe size is %s", len(frontierQueue)
            print PuzzleState.nodes_expanded
            print len(frontierQueue)
            print max_fringe_size
            print "The Action List is \n"
            print newState.retrieveResult(newState)
            print PuzzleState.cost_of_path
            print("Running Time--- %s seconds ---" % (time.time() - start_time))
            return True

        PuzzleState.nodes_expanded = PuzzleState.nodes_expanded + 1
        neighborsStateL = newState.expandNeighbor(newState)
        for neighborItem in neighborsStateL:
            inF = not (frontierQueue.count(neighborItem)>0)
            inEx = not(neighborItem.stateString in exploredSet)
            if (inF and inEx):
                frontierQueue.appendleft(neighborItem)
    return False



start(mode,initState)
