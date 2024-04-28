# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:51:46 2024

@author: shriy
"""

#Program to implement hill climbing algorithm.  
from random import randint 
 
#Random Solution generator 
''' 
For Hill climbing to work, it has to start with a random solution to our Travelling salesman 
problem. first create a list of identifiers of all cities and from there on iteratively pick a city 
from that list at random and add it to our solution. 
''' 
def randomSolution(tsp): 
    cities = list(range(len(tsp))) 
    solution = [] 
     
    for i in range(len(tsp)): 
        randomCity = cities[randint(0, len(cities) - 1)] 
        solution.append(randomCity) 
        cities.remove(randomCity) 
    return solution 
 
# function calculating the length of a route 
''' 
Since we want our Hill climber to find the shortest solution, we need a function calculating the 
length of a specific solution. 
''' 
def routeLength(tsp, solution): 
    routeLength = 0 
    for i in range(len(solution)): 
        routeLength += tsp[solution[i - 1]][solution[i]] 
    return routeLength 
 
# function generating all neighbours of a solution 
def getNeighbours(solution): 
    neighbours = [] 
    for i in range(len(solution)): 
        for j in range(i + 1, len(solution)): 
            neighbour = solution.copy() 
            neighbour[i] = solution[j] 
            neighbour[j] = solution[i] 
            neighbours.append(neighbour) 
    return neighbours 
 
#function finding the best neighbour 
def getBestNeighbour(tsp, neighbours): 
    bestRouteLength = routeLength(tsp, neighbours[0]) 
    bestNeighbour = neighbours[0] 
    for neighbour in neighbours: 
        currentRouteLength = routeLength(tsp, neighbour) 
        if currentRouteLength < bestRouteLength: 
            bestRouteLength = currentRouteLength 
            bestNeighbour = neighbour 
    return bestNeighbour, bestRouteLength 
 
def hillClimbing(tsp): 
    currentSolution = randomSolution(tsp) 
    currentRouteLength = routeLength(tsp, currentSolution) 
    neighbours = getNeighbours(currentSolution) 
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours) 
 
    while bestNeighbourRouteLength < currentRouteLength: 
        currentSolution = bestNeighbour 
        currentRouteLength = bestNeighbourRouteLength 
        neighbours = getNeighbours(currentSolution) 
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours) 
 
    return currentSolution, currentRouteLength 
 
def problemGenerator(nCities): 
    tsp = [] 
    for i in range(nCities): 
        distances = [] 
        for j in range(nCities): 
            if j == i: 
                distances.append(0) 
            elif j < i: 
                distances.append(tsp[j][i]) 
            else: 
                distances.append(randint(10, 1000)) 
        tsp.append(distances) 
    return tsp 
 
 
 
 
 
 
 
 
def main():  
    #Data for the Travelling Salesman Problem 
    '''the distance from each city to itself is zero, and the distance from city A to  
    city B is the same as the distance from city B to city A. 
    Suppose we've four cities so, we get a list as: 
    ''' 
         
    print("\t----Hill Climbing Algorithm----\n") 
    print("..Illustrated using Travelling Salesman problem...\n") 
 
    # print(hillClimbing(tsp)) 
    tsp = problemGenerator(10) 
    for i in range(10): 
        print(hillClimbing(tsp)) 
     
 
if __name__ == "__main__": 
    main() 