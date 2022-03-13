### Exercise 3 - q2: BFS ###

#import libraries:
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

#~~~  implementation of node class  ~~~
class Node():
	def __init__(self, item): 
		self.item = item 
		self.next = None

#~~~  implementation of queue class  ~~~
class Queue(): 
	def __init__(self): 
		self.head = None #the first in the queue
		self.tail = None #the last in the queue
		self.q_size = 0 #the queue size
        
	def front(self):
		return self.head
    
	def empty(self): 
		return self.head == None
    
	def enqueue(self, x): 
		temp = Node(x) #create a new node in the linked list
		if self.tail == None: #if the queue is empty
			self.head = temp
			self.tail = temp 
			self.q_size += 1
			return
		self.tail.next = temp # add the new node to the end of the queue
		self.tail = temp 
		self.q_size += 1
        
	def dequeue(self): 
		if self.empty(): #if the queue is empty there is nothing to return 
			return
		temp = self.head #take the first one in the queue
		self.head = temp.next #change the first one to be the one next to the current
		if(self.head == None): 
			self.tail = None
		self.q_size -= 1
		return temp.item

#a. plot the islands
def plot_islands(matrix):
	
    mat = np.array(matrix,dtype=np.uint8) 
    cmapmine = ListedColormap(['b', 'w'], N=2)  
    fig, ax1 = plt.subplots()
    ax1.imshow(mat, cmap=cmapmine, vmin=0, vmax=1) 
    plt.show()


    

#b. count islands algorithm using BFS
#~~~  implementation of count_islands function  ~~~
    
#check if we are inside matrix's limits 
def is_valid(mat , r, c):
        row, col = len(mat), len(mat[0])
        if r < 0 or c < 0 or r >= row or c >= col:
            return False
        return True
    
def bfs(mat, r, c):
        q = Queue()
        q.enqueue((r, c))
        mat[r][c] = 0 #we visited this cell
        while q.empty() == False:
            #possible cell's neighbours:
            directions = [(0,1), (0,-1), (-1,0), (1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
            r, c = q.dequeue()
            for d in directions:
                #checking all the neighbours
                new_r, new_c = r + d[0], c + d[1] 
                # ==1 meaning unvisited cells
                if is_valid(mat, new_r, new_c) and mat[new_r][new_c] == 1:
                    #marking we visited this cell
                    mat[new_r][new_c] = 0
                    q.enqueue((new_r, new_c))
                    
    
def count_islands(matrix):
	
    #converting np array into list of lists
    if type(matrix).__module__ == np.__name__:
        matrix = matrix.tolist()
    row, col = len(matrix), len(matrix[0])
    num_islands = 0 #initializing the counter
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                bfs(matrix, i, j)
                num_islands += 1
    return num_islands









