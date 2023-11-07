# NE 336 Lab 1  Group 2 Sept 26 2023 - Solve System
# Written by Zehra Ahmed - 20889523 

#imports
import numpy as np
import scipy as sp
import time

def solve_system(A, b, method=None):
    '''
    (ndarray,ndarry,str)->(ndarray,float)
    This function will return the solution of [A][x] = [b], if one exists as well as the time taken to find it otherwise None.
    A is a square matrix which is nXn
    b is a column vector so it is nX1
    method is optional and can be :
     inv : for the inverse method
     lu : for the lu decomposition 
    '''
    
    start_time = time.time()

    #Error checking 
    if len(A) != len(A[0]):
       raise ValueError("Matrix [A] is not a square matrix!")
    
    if len(A[0]) != len(b):
        raise ValueError("Matrix dimension mismatch")
    
    if np.linalg.matrix_rank(A) != np.linalg.matrix_rank(np.column_stack((A, b))):
        raise ValueError("System of equations is inconsistent")

    # Use method according to input
    if method == None: 
        solution = (np.linalg.solve(A,b))
    elif method == "inv":
        Ainv = np.linalg.inv(A)
        solution = Ainv @ b 
    
    elif method == "lu":
        P,L,U = sp.linalg.lu(A)
        D= (np.linalg.solve(P@L,b))
        solution = np.linalg.solve(U,D) 
    else:
        raise ValueError("Error: Valid method not chosen. Use 'inv' or 'lu'.")
    
    time_difference = time.time() - start_time
    return solution, time_difference

   
# Example 4.2 arrays
A = np.array([[-3,2,-1],[6,-6,7],[3,-4,4]])
b= np.array([-1,-7,-6]).T


# Using built in function 
solution, time_taken = solve_system(A, b)
print("Solution using numpy.linalg.solve:", solution)
print("Time taken:", time_taken, "seconds")

# Using inverse 
solution_inv, time_taken_inv = solve_system(A, b, "inv")
print("Solution using inverse method:", solution_inv)
print("Time taken:", time_taken_inv, "seconds")

# Using LU decomposition 
solution_lu, time_taken_lu = solve_system(A, b, "lu")
print("Solution using LU decomposition:", solution_lu)
print("Time taken:", time_taken_lu, "seconds")


#4.2 Q1 
A1 = np.array([[3, 18, 9], [2, 3, 3], [4, 1, 2]])
b1 = np.array([18, 117, 283])

solution, time_taken = solve_system(A1, b1)
print("Solution for Q1 is ", solution)
print("Time taken:", time_taken, "seconds")

solution, time_taken = solve_system(A1, b1, "inv")
print("Solution for Q1 using inverse is ", solution)
print("Time taken:", time_taken, "seconds")

solution, time_taken = solve_system(A1, b1, "lu")
print("Solution for Q1 using LU decomositon is ", solution)
print("Time taken:", time_taken, "seconds")

#All three methods present the same answer so we can assume it is correct

#4.2 Q2 
A2 = np.array([[20, 15, 10], [-3, -2.24999, 7], [5, 1, 3]])
b2 = np.array([45, 1.751, 9])

solution, time_taken = solve_system(A2, b2)
print("Solution for Q2 is ", solution)
print("Time taken:", time_taken, "seconds")

solution, time_taken = solve_system(A2, b2, "inv")
print("Solution for Q2 using inverse is ", solution)
print("Time taken:", time_taken, "seconds")

solution, time_taken = solve_system(A2, b2, "lu")
print("Solution for Q2 using LU decomositon is ", solution)
print("Time taken:", time_taken, "seconds")
