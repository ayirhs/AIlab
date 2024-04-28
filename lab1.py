#---Imports--- 
from random import randint 
from random import choice 
from time import sleep 
 
#----------------------------GLOBAL VARIABLES----------------------------------- 
#setting the room A and room B's state 
env_dirty_state ={0:False, 1 :False } #inital setup for dictionary 
#vaccum location 
vaccum_location = 0 
 
#-------------------***-----FUNCTIONS-----****---------------------------------- 
 
#Create a random position for the vaccum cleaner at startup 
def set_vaccum_loc(): 
    global vaccum_location 
    #Setting the random initial vaccum location 
    vaccum_location = randint(0,1) 
 
#Function for generating random state for rooms 
def rand_state_generation(): 
    global env_dirty_state 
    #To create a random choice for dirty 
    state=[True, False] 
    #Setting the new choices 
    env_dirty_state[0] = choice(state)  # Creating a random state for room A 
    env_dirty_state[1] = choice(state) #Creating a random state for room B 
 
#Function to clean the rooms 
def clean_rooms(room): 
    #Code to clean the room A 
    if room==0: 
        print("Room A is DIRTY. Cleaning it up....") 
        sleep(3) 
        env_dirty_state[room] = False 
        print("Room A cleaned.\nMoving...") 
        sleep(3) 
 
    #Code to clean the room B 
    elif room == 1: 
        print("Room B is DIRTY. Cleaning it up....") 
        sleep(3) 
        env_dirty_state[room] = False 
        print("Room B cleaned.\nMoving...") 
        sleep(3) 
 
#----------------------AGENTS--------------------------------------------------------------- 
#--The simple reflex agent-- 
def simple_reflex_agent(): 
    global env_dirty_state, vaccum_location 
    name_of_room = {0: 'A', 1: 'B'} 
    iter_count=0 
 
    set_vaccum_loc() 
 
    rand_state_generation() 
    #List to see if both rooms are cleaned 
    cleaned_room = 0 
 
    #Simulation of sleeping 
    sleep(2) 
 
    #Simulates a continuous run of the cleaner machine. 
    while True: 
 
        #Creating a break condition for visualization 
        if iter_count>10 and cleaned_room==2: 
            print("Both room cleaned.") 
            break 
 
        iter_count+=1 
 
        #Checking if both rooms are cleaned 
        if cleaned_room == 2: 
            cleaned_room = 0 #Set cleaned rooms to zero 
            print("Both Room's Clean. ") 
            print("Robot Going to SLEEP. ") 
            sleep(5) 
            print("---Waking Up----\n") 
            #Generate new random location and data 
            set_vaccum_loc() 
            rand_state_generation() 
 
        #Display the status of iteration, rooms 
        if cleaned_room==0: 
            print(f"----Room Stats:---------") 
            print(f"Vaccum in Room {name_of_room[vaccum_location]}.\n") 
            print(f"Dirty State: \nA: {env_dirty_state[0]}, B: {env_dirty_state[1]}\n\n") 
            sleep(2) 
 
        #If vaccum is in room A 
        if vaccum_location==0: 
            #If room A is dirty 
            if env_dirty_state[vaccum_location]: 
                clean_rooms(vaccum_location) #Clean the room 
            #if room A is clean 
            else: 
                if cleaned_room !=2: 
                    print("Room A is clean. Moving to Room B...") 
 
            vaccum_location= 1  #Set the vaccum location to next room 
            cleaned_room += 1  #Increment the cleaned room as Room A is now cleaned or is clean. 
 
        #If vaccum is in room B 
        elif vaccum_location==1: 
            #If room B is dirty 
            if env_dirty_state[vaccum_location]: 
                clean_rooms(vaccum_location) 
            #if room B is clean 
            else: 
                if cleaned_room !=2: 
                    print("Room B is clean. Moving to Room A...") 
            vaccum_location= 0  #Set the vaccum location to next room 
            cleaned_room +=1 #Increment the cleaned room as Room B is now cleaned or is clean. 
 
 
#--------Creating a function like main---------- 
def main(): 
    print("\t-------Vaccum Cleaner AI Program--------\n\n") 
 
    simple_reflex_agent() 
 
#Run only if this program is not imported into another program. 
if __name__ != "main": 
    main() 
