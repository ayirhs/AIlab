#Program to implement the BFS search algorithm 
#initializing the queues 
front = -1 
rear=-1 
#List to hold the nodes that are to be processed. 
queue=[] 
#List to keep track of the origin of each node 
orig =[] 
 
#Our graph represented in form of adjacency list 
adj_list ={ 
    'A': ['B','C','D'], 
    'B': ['E'], 
    'C':['B','G'], 
    'D': ['C','G'], 
    'E': ['C','F'], 
    'F':['C','H'], 
    'G':['F','H','I'], 
    'H':['E','I'], 
    'I':['F']   
} 
''' 
If status is 1 -> ready state 
If status is 2 -> the node is enqueues and is said to be in waiting state.  
If status is 3 -> then then node is dequeued.  
''' 
status={'A': 1, 'B': 1, 'C':1, 'D': 1, 'E': 1, 'F':1, 'G':1, 'H':1, 'I':1} 
 
#-------------------------------- 
print("\t------BFS Search Algorithm------\n") 
 
#Display the adjacency list that is being used.  
print("Graph used is shown by the below adjacency list") 
print("Adjacency List: \n") 
for key,value in adj_list.items(): 
    print(key,':', value) 
 
start=input("\nEnter the starting vertex: ") 
dest =input("Enter the ending vertex: ") 
 
 
#Enquiying the first node in the list 
queue.append(start) 
orig.append( '0') 
 
front+=1 
rear+=1 
 
while True: 
    #Dequeing the first node  
    selected_node = queue[front] 
    #Set it's status to 3 
    status[selected_node] = 3 
    front+=1 
     
    #Selection of the adjacant nodes of the selected node 
    adj_nodes = adj_list[selected_node] 
    
   #For each node in the list of adjacant nodes 
    for node in adj_nodes: 
        #If the status of node is 1 i.e. the node is untouched then: 
        if status[node]==1: 
            #Enqueue the nodes and its origin in the queue 
            queue.append(node) 
            orig.append(selected_node) 
            #Set the status of the node to 2 i.e. waiting state.  
            status[node]=2 
            #Increment the rear index 
            rear+=1 
    #If the rear item on the queue is our destination then break the loop 
    if queue[rear]==dest: 
        break 
     
#-------Backtracking form destination using original list ---------------------- 
#List to store the final path results 
final_path = list()  
 
#This begins from the rearmost item in the queue 
node = queue[rear] #Stores the nodes in our path  
parent = orig[rear] #Stores the parent of the nodes in our path 
 
#Append the destination node in the queue.  
final_path.append(node) 

 
 
 
#Continue adding in the list 
while True: 
    #Get the index of the parent from the queue.  
    index = queue.index(parent) 
     
    # Set the node in our path to that inat index  
    node = queue[index] 
    #Set the new parent  
    parent= orig[index] 
    #Add that node in the final path list 
    final_path.append(node) 
      
    #If we reach the starting node then break the loop         
    if (parent == '0'): 
        break 
 
#Reverse the list so that it goes from source to destination 
final_path = final_path[::-1] 
 
#Displaying the result 
print(f"\nPath from {start} to {dest} is: \n",) 
for each in final_path: 
    print(each, ' -> ', end='')