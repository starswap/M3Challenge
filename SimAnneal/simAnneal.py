import random
import copy
import math

def getAcceptanceRate(old,new,temp):
        """Gets the acceptance probability for a solution with energy new, with an old solution of energy old, at temperature temp"""
        """Cost Function increases with worseness (i.e. not a fitness function)"""
        if new < old:
                return 1; # Always accept better solutions
        
        return math.exp((old - new) / temp) #The solution is worse but we accept it with probability p

       
    
def simAnneal(tempInit,initialSolution,costFunction,coolingRate):
        """Simulated Annealing algorithm for optimisation of a function, taking parameters initial temperature, initial solution, cost function,cooling rate"""

        #Initial conditions for the system
        temperature = tempInit
        solution = copy.copy(initialSolution)
        cost = costFunction(solution)

        #While the metal is still cooling
        while temperature > 1:
                #Select values to swap
                a = random.randint(0,len(solution)-1) 
                b = random.randint(0,len(solution)-1)                
                while (a == b):
                        #Select values to swap
                        a = random.randint(0,len(solution)-1) 
                        b = random.randint(0,len(solution)-1)

                        
                #Make sure that a is less than or equal to b
                if a > b:
                        temp = a
                        a = b
                        b = temp

                #perform the swap
                newSolution = solution[:a] + solution[b] + solution[a+1:b] + solution[a] + solution[b+1:]
                newCost = costFunction(newSolution)

                #accept solution with correct probability
                if random.random() < getAcceptanceRate(cost,newCost,temperature):
                        solution = copy.copy(newSolution)
                        cost = newCost

                #Cool system
                temperature *= (1-coolingRate)
                
        return solution
