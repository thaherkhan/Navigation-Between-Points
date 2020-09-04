
"""
Created on Wed Jun 17 11:47:47 2019

@author: Abid_Khan

"""

from operator import itemgetter
#import tkinter as tk
from tkinter import *

pair = []


window = Tk()
window.title("Nevigation Between Two Points")
window.geometry("400x300")


def close():
    window.destroy()    


 # Design Maps
r = 'blue'
ovp='blue'
ln='White'
ov='black'
lbfg='white'
lbbg='black'
wid=3
widln=6

c=Canvas(window,height=1500,width=1500,bg="Green")

Wk1 = Button(window, text='OK',fg='black', bg='red', height=2, width=8,font='Helvetica 15 bold',bd=5)
Wk1.place(x=1200,y=600)

#  First Raw
#  ---------  

c.create_oval(120,70,10,20,fill=ov,width=3)
widget = Label(c, text='Markaj Point',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(65,45, window=widget)

# Markaj Point Tooo Railghate
c.create_line(50,71,50,210,fill=ln,width=6)
# Markaj Point Tooo Jitu Miar Point
c.create_line(104,64,250,210,fill=ln,width=6)


c.create_oval(390,60,240,10,fill=ov,width=3)
widget = Label(c, text='Shek Ghat',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(315,35, window=widget)


#Shek Ghat Tooo Medical
c.create_line(391,37,639,37,fill=ln,width=6)
# Shek Ghat Tooo Jitu Miar Point
c.create_line(315,60,250,210,fill=ln,width=6)
# Shek Ghat Tooo Kuarpar
c.create_line(315,60,450,210,fill=ln,width=6)


c.create_oval(790,60,640,10,fill=ov,width=3)
widget = Label(c, text='Medical',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(715,35, window=widget)


# Medical Tooo Lamabazar
c.create_line(710,60,650,210,fill=ln,width=6)
# Medical Tooo Rikabibazar
c.create_line(710,60,840,210,fill=ln,width=6)


c.create_oval(950,60,850,10,fill=ov,width=3)
widget = Label(c, text='Miror Moydan',fg=lbfg,bg=lbbg,font='Helvetica 9 bold')
c.create_window(900,35, window=widget)


# Miror Moydan Tooo Rikabibazar
c.create_line(907,61,840,210,fill=ln,width=6)
# Miror Moydan Tooo Amborkana
c.create_line(910,61,910,410,fill=ln,width=6)


#  Second Raw
#  ----------

c.create_oval(100,270,3,210,fill=ov,width=3)
widget = Label(c, text='Railghate',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(50,240, window=widget)


# Rail Ghate Tooo City Point
c.create_line(50,272,50,410,fill=ln,width=6)


c.create_oval(300,270,190,210,fill=ov,width=3)
widget = Label(c, text='Jitu Miar Point',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(245,240, window=widget)


# Jitu Miar Point Tooo Taltola
c.create_line(250,272,250,409,fill=ln,width=6)
# Jitu Miar Point Tooo Kuarpar
c.create_line(301,245,390,245,fill=ln,width=6)


c.create_oval(500,270,390,210,fill=ov,width=3)
widget = Label(c, text='Kuarpar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(445,240, window=widget)


# Kuarpar Tooo Lamabazar
c.create_line(501,245,590,245,fill=ln,width=6)


c.create_oval(700,270,590,210,fill=ov,width=3)
widget = Label(c, text='Lamabazar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(645,240, window=widget)


# Lamabazar Tooo rikabibazar
c.create_line(701,245,790,245,fill=ln,width=6)
# Lamabazar Tooo Mirza Jangal
c.create_line(645,270,480,420,fill=ln,width=6)


c.create_oval(900,270,790,210,fill=ov,width=3)
widget = Label(c, text='Rikabibazar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(845,240, window=widget)


# Rikabibazar Tooo Chowhatta
c.create_line(840,272,675,414,fill=ln,width=6)



#  Third Raw
#  --------

c.create_oval(100,470,3,410,fill=ov,width=3)
widget = Label(c, text='City Point',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(50,440, window=widget)


# City Point Tooo Zindabazar
c.create_line(50,472,201,621,fill=ln,width=6)


c.create_oval(300,470,190,410,fill=ov,width=3)
widget = Label(c, text='Taltola',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(245,440, window=widget)


#  Taltola Tooo City Point
c.create_line(189,440,102,440,fill=ln,width=6)
#  Taltola Tooo Mirza Jangal
c.create_line(301,440,390,440,fill=ln,width=6)


c.create_oval(500,470,390,410,fill=ov,width=3)
widget = Label(c, text='Mirzajangal',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(445,440, window=widget)


# Mirza Jangal Tooo ZindaBazar
c.create_line(430,470,260,610,fill=ln,width=6)


#c.create_oval(900,500,790,410,fill="blue",width=3)
#widget = Label(c, text='Chowhatta',fg='blue',bg='black')
#c.create_window(845,455, window=widget)


c.create_oval(700,470,590,410,fill=ov,width=3)
widget = Label(c, text='Chowhatta',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(645,440, window=widget)


# Chowhatta Tooo Zindabazar
c.create_line(600,459,300,640,fill=ln,width=6)


c.create_oval(950,470,850,410,fill=ov,width=3)
widget = Label(c, text='Amborkana',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(900,440, window=widget)


# Amborkhana Tooo Chowhatta
c.create_line(849,440,702,440,fill=ln,width=6)


#  Fourth Raw
#  ---------


c.create_oval(300,670,190,610,fill=ov,width=3)
widget = Label(c, text='Zindabazar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
c.create_window(245,640, window=widget)


# Zindabazar Tooo Chowhatta
#c.create_line(700,660,790,660,fill='deeppink',width=6)





We = Button(window, text='Exit',fg='black', bg='red', height=2, width=8,font='Helvetica 15 bold',bd=5,command=close)
We.place(x=900,y=600)

    
    

# Add Source and Destination

SourceL1 = Label(c, text='Source',bg='red',fg='black',font='Helvetica 15 bold')
c.create_window(1000,300,window=SourceL1,height=30,width=110)
E1 = Entry(c, bd=5,font='Helvetica 15 bold')
#EntryE1.pack()
c.create_window(1200,300,window=E1)



DestiL2 = Label(c, text='Destination',bg='red',fg='black',font='Helvetica 15 bold')
c.create_window(1000,350, window=DestiL2,height=30,width=110)
E2 = Entry(c, bd=5,font='Helvetica 15 bold')
c.create_window(1200,350, window=E2)




'''
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   
var = IntVar()
'''


Algo = Label(window,text='Choose Algorithm',fg='black', bg='red', height=2, width=15,font='Helvetica 15 bold',bd=5)
Algo.place(x=1100,y=30)


# Add RadioButton








class Vertex:

    def __init__(self,vName,hValue):
        self.state = vName
        self.heuristicValue = hValue
        self.adjacencyList = {}
        
    def addNeighbour(self,targetNeighbour,weight):
        self.adjacencyList[targetNeighbour] = weight
        
    def successors(self):
        return list(self.adjacencyList.items())
    
    
class Graph:

    def __init__(self):
        self.vertices = {}
        self.numberOfVertex = 0

        
    def addVertex(self,key,heuristic):
        vertexObject = Vertex(key,heuristic)
        self.vertices[key] = vertexObject
        self.numberOfVertex += 1

        
    def addEdge(self,firstVertex,secondVertex,weight=0):
        
        if firstVertex not in self.vertices:
            s = 'Heuristic of "'+firstVertex+'": '
            h = eval(input(s))
            self.addVertex(firstVertex,h)
        
        if secondVertex not in self.vertices:
            s = 'Heuristic of "'+secondVertex+'": '
            h = eval(input(s))
            self.addVertex(secondVertex,h)
            
        self.vertices[firstVertex].addNeighbour(secondVertex, weight)

        
    def allVertexObjects(self):
        return list(self.vertices.values())

    
class Problem:

    def __init__(self,stateSpace,iState,gStates):
        self.stateSpace = stateSpace
        self.initialState = iState
        self.goalStates = gStates

        
    def goalTest(self,nodeState):
        
        if (self.goalStates == None):
            return False
        if(nodeState in self.goalStates):
            return True

        
class Node:

    def __init__(self,currentState,parentNode,pathCost):
        self.state = currentState
        self.parent = parentNode
        self.pathCost = pathCost
    

class Queue:

    def __init__(self):
        self.q = []
        
    def enqueue(self,node):
        self.q.append(node)
        
    def dequeue(self):
        return self.q.pop(0)
    
    def isEmpty(self):
        return (self.q==[])


    

class uninformedSearch():

    def printGraph(self,problem):
        print('The State Space Graph is :')
        print('-------------------------')
    
    
        for vertexObject in problem.stateSpace.allVertexObjects():
            print('(', vertexObject.state,',',vertexObject.heuristicValue,') -> ',end='')
            print(vertexObject.successors())
        print('----------------------------------')
        
    
    def createChildNode(self,childState,parentNode,stepCost):
        n = Node( currentState=childState, parentNode=parentNode,pathCost=(parentNode.pathCost+stepCost) )
        return n
    
    
    def solution(self,problem,goalNode):
        self.currentNode = goalNode
        self.solutionPath = []
        self.solutionPath.append(self.currentNode)
        
        
        while (self.currentNode.state != problem.initialState):
            
            for exploredNode in self.exploredSet:
                if (self.currentNode.parent.state == exploredNode.state):
                    self.currentNode = exploredNode
                    self.solutionPath.append(self.currentNode)
                    break
                
        self.solutionPath.reverse()
        print ('\nGoal Found !!!')
        print ('The path to the solution is: ',end='')
        for solution in self.solutionPath:
            pair.append(solution.state)   # Make Pair between Two Noods
            print('(',solution.state,',', solution.pathCost,')', end=' -> ')
        print (end='\n')
        
  
    def BFS(self,problem):
        self.node = Node(currentState = problem.initialState,parentNode=Node(None,None,None),pathCost=0)
        if (problem.goalTest(self.node.state)):
            return self.solution(problem,self.node)
        
        self.frontier = Queue()
        self.frontier.enqueue(self.node)
        self.frontierStates = []
        self.frontierStates.append(self.node.state)
        
        self.exploredSet = []
        self.exploredSetStates = []
        
        self.count = 0
        
        while (True):
            
            self.frontierStates = [x.state for x in self.frontier.q]
            print('Step', self.count,' : ', end=' ')
            print('Frontier: ', self.frontierStates,end='\n')
            print('\t Explored: ',self.exploredSetStates)
            self.count +=1
            
            
            if (self.frontier.isEmpty()):
                print("Failure, no solution to the goal found.")
                break
            self.node = self.frontier.dequeue()
            self.frontierStates = [x.state for x in self.frontier.q]
            self.exploredSet.append(self.node)
            self.exploredSetStates = [x.state for x in self.exploredSet]
            for childState,weight in problem.stateSpace.vertices[self.node.state].successors():
                self.child =self.createChildNode(childState,self.node,weight)
                if (self.child.state not in self.frontierStates):
                    if (self.child.state not in self.exploredSetStates):
                        if (problem.goalTest(self.child.state)):
                            print('Step', self.count,': ', end=' ')
                            print('Frontier', self.frontierStates, end='\n')
                            print('\t Explored: ', self.exploredSetStates)
                            return self.solution(problem,self.child)
                        self.frontier.enqueue(self.child)
                        

def createStateSpaceGraph():

    g = Graph()
    v = {'Shek Ghat' : 0, 'Medical':0, 'Lamabazar':0, 'Rikabibazar':0, 'Jitu Miar Point':0, 'Kuarpar':0, 'Markaj Point':0,
          'Railghate':0, 'City Point':0, 'Taltola':0, 'Zindabazar':0, 'Mirzajangal':0, 'Chowhatta':0, 'Amborkana': 0, 
          'Miror Moydan':0}
        
    for vertex,heuristic in v.items():
        g.addVertex(vertex,heuristic)
        
    # Graph Input
        
    
    
    g.addEdge('Medical','Lamabazar',10)
    g.addEdge('Lamabazar','Medical',10)
    
    g.addEdge('Medical','Rikabibazar',5)
    g.addEdge('Rikabibazar','Medical',5)
    
    g.addEdge('Shek Ghat','Medical',5)
    g.addEdge('Medical','Shek Ghat',5)
    
    g.addEdge('Shek Ghat','Jitu Miar Point',5)
    g.addEdge('Jitu Miar Point','Shek Ghat',5)
    
    g.addEdge('Shek Ghat','Kuarpar',5)
    g.addEdge('Kuarpar','Shek Ghat',5)
    
    g.addEdge('Markaj Point','Jitu Miar Point',1)
    g.addEdge('Jitu Miar Point','Markaj Point',1)
    
    g.addEdge('Markaj Point','Railghate',3)
    g.addEdge('Railghate','Markaj Point',3)
    
    g.addEdge('Railghate','City Point',3)
    g.addEdge('City Point','Railghate',3)
    
    g.addEdge('City Point','Taltola',5)
    g.addEdge('Taltola','City Point',5)
    
    g.addEdge('City Point','Zindabazar',3)
    g.addEdge('Zindabazar','City Point',3)
    
    g.addEdge('Jitu Miar Point','Taltola',1)
    g.addEdge('Taltola','Jitu Miar Point',1)
    
    g.addEdge('Jitu Miar Point','Kuarpar',5)
    g.addEdge('Kuarpar','Jitu Miar Point',5)
    
    g.addEdge('Taltola','Mirzajangal',1)
    g.addEdge('Mirzajangal','Taltola',1)
    
    g.addEdge('Mirzajangal','Lamabazar',1)
    g.addEdge('Lamabazar','Mirzajangal',1)
    
    g.addEdge('Zindabazar','Mirzajangal',1)
    g.addEdge('Mirzajangal','Zindabazar',1)
    
    g.addEdge('Chowhatta','Zindabazar',5)
    g.addEdge('Zindabazar','Chowhatta',5)
    
    g.addEdge('Amborkana','Chowhatta',5)
    g.addEdge('Chowhatta','Amborkana',5)
    
    g.addEdge('Chowhatta','Rikabibazar',5)
    g.addEdge('Rikabibazar','Chowhatta',5)
    
    g.addEdge('Amborkana','Miror Moydan',10)
    g.addEdge('Miror Moydan','Amborkana',10)
    
    g.addEdge('Rikabibazar','Miror Moydan',5)
    g.addEdge('Miror Moydan','Rikabibazar',5)
    
    g.addEdge('Rikabibazar','Lamabazar',5)
    g.addEdge('Lamabazar','Rikabibazar',5)
    
    g.addEdge('Lamabazar','Kuarpar',3)
    g.addEdge('Kuarpar','Lamabazar',3)
    

        

    return g

def check():

    
    #if __name__ == '__main__' :
    s1 = E1.get()
    d1 = E2.get()
    
    g = createStateSpaceGraph()
    #problem = Problem(stateSpace=g,iState=g.vertices['Shek Ghat'].state,gStates=[g.vertices['Amborkana'].state])
    
    uSearch = uninformedSearch()
    
    # print The Graph First
    print ()
    #uSearch.printGraph(problem)
    
    # Result of BFS

    print ('\nUniform Cost Search',end='\n-----------------------------\n')
    #problem1 = Problem(stateSpace=g,iState=g.vertices['Amborkana'].state,gStates=g.vertices['Markaj Point'].state)
    #uSearch.BFS(problem1)
    
    problem1 = Problem(stateSpace=g,iState=g.vertices[s1].state,gStates=g.vertices[d1].state)
    uSearch.BFS(problem1)


# Pair Indexing 


    indexLen= len(pair)  
#print(indexLen)
    for x in range (indexLen-1):
        #print(pair[x],pair[x+1])
        src=pair[x]
        des=pair[x+1]
        
        # Find Path
    #c.create_line(391,37,639,37,fill=ln,width=6)
        if(src=='Shek Ghat' and des=='Medical'):
            c.create_line(391,37,639,37,fill=r,width=widln)  
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
        elif( src=='Medical' and des=='Shek Ghat'):
            c.create_line(391,37,639,37,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
    
        elif(src=='Medical' and des=='Lamabazar'):
            c.create_line(710,60,650,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
        elif( src=='Lamabazar' and des=='Medical'):
            c.create_line(710,60,650,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
             
             
        elif(src=='Medical' and des=='Rikabibazar'):
            c.create_line(710,60,840,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        elif( src=='Rikabibazar' and des=='Medical'):
            c.create_line(710,60,840,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        
         
        elif(src=='Shek Ghat' and des=='Jitu Miar Point'):
            c.create_line(315,60,250,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
        elif( src=='Jitu Miar Point' and des=='Shek Ghat'):
            c.create_line(315,60,250,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
    
            
        elif(src=='Shek Ghat' and des=='Kuarpar'):
            c.create_line(315,60,450,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
        elif( src=='Kuarpar' and des=='Shek Ghat'):
            c.create_line(315,60,450,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
    
             
        elif(src=='Markaj Point' and des=='Jitu Miar Point'):
            c.create_line(104,64,250,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
        elif( src=='Jitu Miar Point' and des=='Markaj Point'):
            c.create_line(104,64,250,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
    
    
        elif(src=='Markaj Point' and des=='Railghate'):
            c.create_line(50,71,50,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
        elif( src=='Railghate' and des=='Markaj Point'):
            c.create_line(50,71,50,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
             
        
        elif(src=='Railghate' and des=='City Point'):
            c.create_line(50,272,50,410,fill=r,width=widln)
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
        elif( src=='City Point' and des=='Railghate'):
            c.create_line(50,272,50,410,fill=r,width=widln)
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
             
             
        elif(src=='City Point' and des=='Taltola'):
            c.create_line(189,440,102,440,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
        elif( src=='Taltola' and des=='City Point'):
            c.create_line(189,440,102,440,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
             
        
        elif(src=='City Point' and des=='Zindabazar'):
            c.create_line(50,472,201,621,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        elif( src=='Zindabazar' and des=='City Point'):
            c.create_line(50,472,201,621,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
             
             
        elif(src=='Jitu Miar Point' and des=='Taltola'):
            c.create_line(250,272,250,409,fill=r,width=widln)
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
        elif( src=='Taltola' and des=='Jitu Miar Point'):
            c.create_line(250,272,250,409,fill=r,width=widln)
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
             
        elif(src=='Jitu Miar Point' and des=='Kuarpar'):
            c.create_line(301,245,390,245,fill=r,width=widln)
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
        elif( src=='Kuarpar' and des=='Jitu Miar Point'):
            c.create_line(301,245,390,245,fill=r,width=widln) 
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
             
        elif(src=='Taltola' and des=='Mirzajangal'):
            c.create_line(301,440,390,440,fill=r,width=widln)
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
        elif( src=='Mirzajangal' and des=='Taltola'):
            c.create_line(301,440,390,440,fill=r,width=widln)
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
             
         
        elif(src=='Mirzajangal' and des=='Lamabazar'):
            c.create_line(645,270,480,420,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
        elif( src=='Lamabazar' and des=='Mirzajangal'):
            c.create_line(645,270,480,420,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
             
             
        elif(src=='Zindabazar' and des=='Mirzajangal'):
            c.create_line(430,470,260,610,fill=r,width=widln)
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        elif( src=='Mirzajangal' and des=='Zindabazar'):
            c.create_line(430,470,260,610,fill=r,width=widln)
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        
        elif(src=='Chowhatta' and des=='Zindabazar'):
            c.create_line(600,459,300,640,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        elif( src=='Zindabazar' and des=='Chowhatta'):
            c.create_line(600,459,300,640,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
             
         
        elif(src=='Amborkana' and des=='Chowhatta'):
            c.create_line(849,440,702,440,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
        elif( src=='Chowhatta' and des=='Amborkana'):
            c.create_line(849,440,702,440,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
             
             
        elif(src=='Chowhatta' and des=='Rikabibazar'):
            c.create_line(840,272,675,414,fill=r,width=widln)
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
        elif( src=='Rikabibazar' and des=='Chowhatta'):
            c.create_line(840,272,675,414,fill=r,width=widln)
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            
            
        elif(src=='Amborkana' and des=='Miror Moydan'):
            c.create_line(910,61,910,410,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
        elif( src=='Miror Moydan' and des=='Amborkana'):
            c.create_line(910,61,910,410,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
             
             
        elif(src=='Rikabibazar' and des=='Miror Moydan'):
            c.create_line(907,61,840,210,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        elif( src=='Miror Moydan' and des=='Rikabibazar'):
            c.create_line(907,61,840,210,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
             
         
        elif(src=='Rikabibazar' and des=='Lamabazar'):
            c.create_line(701,245,790,245,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        elif( src=='Lamabazar' and des=='Rikabibazar'):
            c.create_line(701,245,790,245,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)  # Lamabazar
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
             
             
        elif(src=='Lamabazar' and des=='Kuarpar'):
            c.create_line(501,245,590,245,fill=r,width=widln)
            c.create_oval(500,270,390,210,fill=ovp,width=wid)  # Kuarpar
            c.create_oval(700,270,590,210,fill=ovp,width=wid)  # Lamabazar
        elif( src=='Kuarpar' and des=='Lamabazar'):
            c.create_line(501,245,590,245,fill=r,width=widln)
            c.create_oval(500,270,390,210,fill=ovp,width=wid)  # Kuarpar
            c.create_oval(700,270,590,210,fill=ovp,width=wid)
            
    # Lamabazar

def rst(window):
    
    indexLen= len(pair)  
#print(indexLen)
    for x in range (indexLen-1):
        pair[x] = 0
    #  First Raw
    #  ---------
    
    
    c.create_oval(120,70,10,20,fill=ov,width=3)
    widget = Label(c, text='Markaj Point',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(65,45, window=widget)
    
    # Markaj Point Tooo Railghate
    c.create_line(50,71,50,210,fill=ln,width=6)
    # Markaj Point Tooo Jitu Miar Point
    c.create_line(104,64,250,210,fill=ln,width=6)
    
    
    c.create_oval(390,60,240,10,fill=ov,width=3)
    widget = Label(c, text='Shek Ghat',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(315,35, window=widget)
    
    
    #Shek Ghat Tooo Medical
    c.create_line(391,37,639,37,fill=ln,width=6)
    # Shek Ghat Tooo Jitu Miar Point
    c.create_line(315,60,250,210,fill=ln,width=6)
    # Shek Ghat Tooo Kuarpar
    c.create_line(315,60,450,210,fill=ln,width=6)
    
    
    c.create_oval(790,60,640,10,fill=ov,width=3)
    widget = Label(c, text='Medical',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(715,35, window=widget)
    
    
    # Medical Tooo Lamabazar
    c.create_line(710,60,650,210,fill=ln,width=6)
    # Medical Tooo Rikabibazar
    c.create_line(710,60,840,210,fill=ln,width=6)
    
    
    c.create_oval(950,60,850,10,fill=ov,width=3)
    widget = Label(c, text='Miror Moydan',fg=lbfg,bg=lbbg,font='Helvetica 9 bold')
    c.create_window(900,35, window=widget)
    
    
    # Miror Moydan Tooo Rikabibazar
    c.create_line(907,61,840,210,fill=ln,width=6)
    # Miror Moydan Tooo Amborkana
    c.create_line(910,61,910,410,fill=ln,width=6)
    
    
    #  Second Raw
    #  ----------
    
    c.create_oval(100,270,3,210,fill=ov,width=3)
    widget = Label(c, text='Railghate',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(50,240, window=widget)
    
    
    # Rail Ghate Tooo City Point
    c.create_line(50,272,50,410,fill=ln,width=6)
    
    
    c.create_oval(300,270,190,210,fill=ov,width=3)
    widget = Label(c, text='Jitu Miar Point',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(245,240, window=widget)
    
    
    # Jitu Miar Point Tooo Taltola
    c.create_line(250,272,250,409,fill=ln,width=6)
    # Jitu Miar Point Tooo Kuarpar
    c.create_line(301,245,390,245,fill=ln,width=6)
    
    
    c.create_oval(500,270,390,210,fill=ov,width=3)
    widget = Label(c, text='Kuarpar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(445,240, window=widget)
    
    
    # Kuarpar Tooo Lamabazar
    c.create_line(501,245,590,245,fill=ln,width=6)
    
    
    c.create_oval(700,270,590,210,fill=ov,width=3)
    widget = Label(c, text='Lamabazar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(645,240, window=widget)
    
    
    # Lamabazar Tooo rikabibazar
    c.create_line(701,245,790,245,fill=ln,width=6)
    # Lamabazar Tooo Mirza Jangal
    c.create_line(645,270,480,420,fill=ln,width=6)
    
    
    c.create_oval(900,270,790,210,fill=ov,width=3)
    widget = Label(c, text='Rikabibazar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(845,240, window=widget)
    
    
    # Rikabibazar Tooo Chowhatta
    c.create_line(840,272,675,414,fill=ln,width=6)
    
    
    
    #  Third Raw
    #  --------
    
    c.create_oval(100,470,3,410,fill=ov,width=3)
    widget = Label(c, text='City Point',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(50,440, window=widget)
    
    
    # City Point Tooo Zindabazar
    c.create_line(50,472,201,621,fill=ln,width=6)
    
    
    c.create_oval(300,470,190,410,fill=ov,width=3)
    widget = Label(c, text='Taltola',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(245,440, window=widget)
    
    
    #  Taltola Tooo City Point
    c.create_line(189,440,102,440,fill=ln,width=6)
    #  Taltola Tooo Mirza Jangal
    c.create_line(301,440,390,440,fill=ln,width=6)
    
    
    c.create_oval(500,470,390,410,fill=ov,width=3)
    widget = Label(c, text='Mirzajangal',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(445,440, window=widget)
    
    
    # Mirza Jangal Tooo ZindaBazar
    c.create_line(430,470,260,610,fill=ln,width=6)
    
    
    #c.create_oval(900,500,790,410,fill="blue",width=3)
    #widget = Label(c, text='Chowhatta',fg='blue',bg='black')
    #c.create_window(845,455, window=widget)
    
    
    c.create_oval(700,470,590,410,fill=ov,width=3)
    widget = Label(c, text='Chowhatta',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(645,440, window=widget)
    
    
    # Chowhatta Tooo Zindabazar
    c.create_line(600,459,300,640,fill=ln,width=6)
    
    
    c.create_oval(950,470,850,410,fill=ov,width=3)
    widget = Label(c, text='Amborkana',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(900,440, window=widget)
    
    
    # Amborkhana Tooo Chowhatta
    c.create_line(849,440,702,440,fill=ln,width=6)
    
    
    #  Fourth Raw
    #  ---------
    
    
    c.create_oval(300,670,190,610,fill=ov,width=3)
    widget = Label(c, text='Zindabazar',fg=lbfg,bg=lbbg,font='Helvetica 10 bold')
    c.create_window(245,640, window=widget)





Wr = Button(window, text='Reset',fg='black', bg='red', height=2, width=8,font='Helvetica 15 bold',bd=5,command=lambda:rst(window))
Wr.place(x=1050,y=600)

def ucs():
    
        
    Wk = Button(window, text='OK',fg='black', bg='red', height=2, width=8,font='Helvetica 15 bold',bd=5,command=check)
    Wk.place(x=1200,y=600)

    

R1 = Radiobutton(c, text='UCS',bg='red',fg='black',font='Helvetica 15 bold',value=1,width=5,command=ucs)
c.create_window(1200,130,window=R1)



# A* Algorithm


class Graph2:

    
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]


    def h(self, n):
        H = {
            'Markaj Point': 1,'Shek Ghat': 1,'Medical': 1,'Miror Moydan': 1,'Railghate': 1,
            'Jitu Miar Point': 1,'Kuarpar': 1,'Lamabazar': 1,'Rikabibazar': 1,'City Point': 1,
            'Taltola': 1,'Mirzajangal': 1,'Chowhatta': 1,'Amborkana': 1,'Zindabazar': 1
        }

        return H[n]

    def RBFS_Algo(self, start_node, stop_node):

        
        open_list = set([start_node])
        closed_list = set([])


        g = {}

        g[start_node] = 0

        
        
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;
            
            print()
            if n == None:
                print('Path does not exist!')
                return None


            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    pair.append(n)
                    reconst_path.append(n)
                    n = parents[n]
                pair.append(n)

                reconst_path.append(start_node)

                reconst_path.reverse()
                
                print('Path found for RBFS: {}'.format(reconst_path))
                    
                return reconst_path

            
            for (m, weight) in self.get_neighbors(n):

                
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight



                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)


            open_list.remove(n)
            closed_list.add(n)


        print('Path does not exist!')
        return None
    
adjacency_list = {
        
    'Markaj Point': [('Railghate', 3), ('Jitu Miar Point', 1)],
    
    'Shek Ghat': [('Jitu Miar Point', 5), ('Kuarpar', 5), ('Medical', 5)],
    
    'Medical': [('Shek Ghat', 5), ('Lamabazar', 10), ('Rikabibazar', 5)],
    
    'Miror Moydan': [('Rikabibazar', 5), ('Amborkana', 10)],
    
    'Railghate': [('Markaj Point', 3), ('City Point', 3)],
    
    'Jitu Miar Point': [('Markaj Point', 1), ('Shek Ghat', 5), ('Kuarpar', 5), ('Taltola', 1)],
    
    'Kuarpar': [('Shek Ghat', 5), ('Jitu Miar Point', 5), ('Lamabazar', 3)],
    
    'Lamabazar': [('Medical', 10), ('Kuarpar', 3), ('Rikabibazar', 5), ('Mirzajangal', 1)],
    
    'Rikabibazar': [('Medical', 5), ('Miror Moydan', 5), ('Lamabazar', 5),('Chowhatta', 5)],
    
    'City Point': [('Railghate', 3), ('Taltola', 5), ('Zindabazar', 3)],
    
    'Taltola': [('Jitu Miar Point', 1), ('City Point', 5), ('Mirzajangal', 1)],
    
    'Mirzajangal': [('Lamabazar', 1), ('Taltola', 1), ('Zindabazar', 1)],
    
    'Chowhatta': [('Rikabibazar', 5), ('Amborkana', 5), ('Zindabazar', 5)],
    
    'Amborkana': [('Miror Moydan', 10), ('Chowhatta', 5)],
    
    'Zindabazar': [('City Point', 3), ('Mirzajangal', 1), ('Chowhatta', 5)]
    
        
}

r = 'blue'
ovp='blue'
ln='White'
ov='black'
lbfg='white'
lbbg='black'
wid=3
widln=6

def check2():
    
    src = E1.get()
    des = E2.get()
    
    
    
    graph1 = Graph2(adjacency_list)
    graph1.RBFS_Algo(src, des)
    
    #print(src,  des)
    
    indexLen= len(pair)  
    #print(indexLen)
    for x in range (indexLen-1):
        #print(pair[x],pair[x+1])
        src=pair[x]
        des=pair[x+1]
    
    
    
        if(src=='Shek Ghat' and des=='Medical'):
            c.create_line(391,37,639,37,fill=r,width=widln)  
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
        elif( src=='Medical' and des=='Shek Ghat'):
            c.create_line(391,37,639,37,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
    
        elif(src=='Medical' and des=='Lamabazar'):
            c.create_line(710,60,650,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
        elif( src=='Lamabazar' and des=='Medical'):
            c.create_line(710,60,650,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
             
             
        elif(src=='Medical' and des=='Rikabibazar'):
            c.create_line(710,60,840,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        elif( src=='Rikabibazar' and des=='Medical'):
            c.create_line(710,60,840,210,fill=r,width=widln)
            c.create_oval(790,60,640,10,fill=ovp,width=wid)     # Medical
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        
         
        elif(src=='Shek Ghat' and des=='Jitu Miar Point'):
            c.create_line(315,60,250,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
        elif( src=='Jitu Miar Point' and des=='Shek Ghat'):
            c.create_line(315,60,250,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
    
            
        elif(src=='Shek Ghat' and des=='Kuarpar'):
            c.create_line(315,60,450,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
        elif( src=='Kuarpar' and des=='Shek Ghat'):
            c.create_line(315,60,450,210,fill=r,width=widln)
            c.create_oval(390,60,240,10,fill=ovp,width=wid)     # Shek Ghat
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
    
             
        elif(src=='Markaj Point' and des=='Jitu Miar Point'):
            c.create_line(104,64,250,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
        elif( src=='Jitu Miar Point' and des=='Markaj Point'):
            c.create_line(104,64,250,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
    
    
        elif(src=='Markaj Point' and des=='Railghate'):
            c.create_line(50,71,50,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
        elif( src=='Railghate' and des=='Markaj Point'):
            c.create_line(50,71,50,210,fill=r,width=widln)
            c.create_oval(120,70,10,20,fill=ovp,width=wid)      # Markaj Point
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
             
        
        elif(src=='Railghate' and des=='City Point'):
            c.create_line(50,272,50,410,fill=r,width=widln)
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
        elif( src=='City Point' and des=='Railghate'):
            c.create_line(50,272,50,410,fill=r,width=widln)
            c.create_oval(100,270,3,210,fill=ovp,width=wid)     # Rail Ghate
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
             
             
        elif(src=='City Point' and des=='Taltola'):
            c.create_line(189,440,102,440,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
        elif( src=='Taltola' and des=='City Point'):
            c.create_line(189,440,102,440,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
             
        
        elif(src=='City Point' and des=='Zindabazar'):
            c.create_line(50,472,201,621,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        elif( src=='Zindabazar' and des=='City Point'):
            c.create_line(50,472,201,621,fill=r,width=widln)
            c.create_oval(100,470,3,410,fill=ovp,width=wid)     # City Point
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
             
             
        elif(src=='Jitu Miar Point' and des=='Taltola'):
            c.create_line(250,272,250,409,fill=r,width=widln)
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
        elif( src=='Taltola' and des=='Jitu Miar Point'):
            c.create_line(250,272,250,409,fill=r,width=widln)
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
             
        elif(src=='Jitu Miar Point' and des=='Kuarpar'):
            c.create_line(301,245,390,245,fill=r,width=widln)
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
        elif( src=='Kuarpar' and des=='Jitu Miar Point'):
            c.create_line(301,245,390,245,fill=r,width=widln) 
            c.create_oval(300,270,190,210,fill=ovp,width=wid)   # Jitu Miar Point
            c.create_oval(500,270,390,210,fill=ovp,width=wid)   # Kuarpar
             
        elif(src=='Taltola' and des=='Mirzajangal'):
            c.create_line(301,440,390,440,fill=r,width=widln)
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
        elif( src=='Mirzajangal' and des=='Taltola'):
            c.create_line(301,440,390,440,fill=r,width=widln)
            c.create_oval(300,470,190,410,fill=ovp,width=wid)   # Taltola
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
             
         
        elif(src=='Mirzajangal' and des=='Lamabazar'):
            c.create_line(645,270,480,420,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
        elif( src=='Lamabazar' and des=='Mirzajangal'):
            c.create_line(645,270,480,420,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
             
             
        elif(src=='Zindabazar' and des=='Mirzajangal'):
            c.create_line(430,470,260,610,fill=r,width=widln)
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        elif( src=='Mirzajangal' and des=='Zindabazar'):
            c.create_line(430,470,260,610,fill=r,width=widln)
            c.create_oval(500,470,390,410,fill=ovp,width=wid)   # Mirzajangal
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        
        elif(src=='Chowhatta' and des=='Zindabazar'):
            c.create_line(600,459,300,640,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
        elif( src=='Zindabazar' and des=='Chowhatta'):
            c.create_line(600,459,300,640,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(300,670,190,610,fill=ovp,width=wid)   # Zindabazar
             
         
        elif(src=='Amborkana' and des=='Chowhatta'):
            c.create_line(849,440,702,440,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
        elif( src=='Chowhatta' and des=='Amborkana'):
            c.create_line(849,440,702,440,fill=r,width=widln)
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
             
             
        elif(src=='Chowhatta' and des=='Rikabibazar'):
            c.create_line(840,272,675,414,fill=r,width=widln)
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
        elif( src=='Rikabibazar' and des=='Chowhatta'):
            c.create_line(840,272,675,414,fill=r,width=widln)
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
            c.create_oval(700,470,590,410,fill=ovp,width=wid)   # Chowhatta
            
            
        elif(src=='Amborkana' and des=='Miror Moydan'):
            c.create_line(910,61,910,410,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
        elif( src=='Miror Moydan' and des=='Amborkana'):
            c.create_line(910,61,910,410,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(950,470,850,410,fill=ovp,width=wid)   # Amborkana
             
             
        elif(src=='Rikabibazar' and des=='Miror Moydan'):
            c.create_line(907,61,840,210,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        elif( src=='Miror Moydan' and des=='Rikabibazar'):
            c.create_line(907,61,840,210,fill=r,width=widln)
            c.create_oval(950,60,850,10,fill=ovp,width=wid)     # Miror Moydan
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
             
         
        elif(src=='Rikabibazar' and des=='Lamabazar'):
            c.create_line(701,245,790,245,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)   # Lamabazar
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
        elif( src=='Lamabazar' and des=='Rikabibazar'):
            c.create_line(701,245,790,245,fill=r,width=widln)
            c.create_oval(700,270,590,210,fill=ovp,width=wid)  # Lamabazar
            c.create_oval(900,270,790,210,fill=ovp,width=wid)   # Rikabibazar
             
             
        elif(src=='Lamabazar' and des=='Kuarpar'):
            c.create_line(501,245,590,245,fill=r,width=widln)
            c.create_oval(500,270,390,210,fill=ovp,width=wid)  # Kuarpar
            c.create_oval(700,270,590,210,fill=ovp,width=wid)  # Lamabazar
        elif( src=='Kuarpar' and des=='Lamabazar'):
            c.create_line(501,245,590,245,fill=r,width=widln)
            c.create_oval(500,270,390,210,fill=ovp,width=wid)  # Kuarpar
            c.create_oval(700,270,590,210,fill=ovp,width=wid)  # Lamabazar
        
    
    
    
    
def rbfs():
    

    Wk2 = Button(window, text='OK',fg='black', bg='red', height=2, width=8,font='Helvetica 15 bold',bd=5,command=check2)
    Wk2.place(x=1200,y=600)

R2 = Radiobutton(c, text='RBFS',bg='red',fg='black',font='Helvetica 15 bold',value=2,width=5,command=rbfs)
c.create_window(1200,180,window=R2)

c.pack()

window.mainloop()


    
