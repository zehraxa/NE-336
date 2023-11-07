# NE 336 Lab 1  Group 2 Sept 26 2023 - Linear System and Solve System
# Written by Zehra Ahmed - 20889523 

# imports 
import numpy as np 
import scipy as sp
import time

#solve_system.py function 
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

# ===== Warm up ======
print("==================== Warm up ====================")

# define arrays for numpy
A = np.array([[-3,2,-1],[6,-6,7],[3,-4,4]])
B = np.array([-1,-7,-6]).T

#define arrays for scipy
C = sp.array([[-3,2,-1],[6,-6,7],[3,-4,4]])
D = sp.array([-1,-7,-6]).T

#solve linear equations
print(np.linalg.solve(A,B))
print(sp.linalg.solve (C,D))

# == What is the difference? == 
# Numpy uses LAPACK through the SciPy library for linear equation solving. 
# Scypy builds on top of numpy but also includes additional functionality.

#Find inverse: costly computation power
Ainv = np.linalg.inv(A)
result = Ainv @ B 
print(result)

# == Is there a potential downside to this method?== 
# If A is ill-conditioned (condition number is large), small changes in the input data can 
# result in significant errors in the solution. If matrix A is singular it cannot be inversed therefore 
# this method would not work. 


#LU decomposition 
P,L,U = sp.linalg.lu(A)
D= (np.linalg.solve(P@L,B))
print(np.linalg.solve(U,D))

# == When would this method be superior to others?== LU Decomposition can be superior to other methods if you need to solve multiple linear systems with the 
# same coefficient matrix since  it can be faster by factoring the matrix once.  It also is less computationally 
# expensive as inverse. 

#Condition number
condA = np.linalg.cond(A, p ='fro')
print( "The condition number for A is ", condA)

#==What does this tell you about the system?==
# Condition number tells us the matrix's sensitivity to small changes in the input data.

print("==================== Solve System Tests ====================")
print()
# Example 4.2 arrays
A = np.array([[-3,2,-1],[6,-6,7],[3,-4,4]])
b= np.array([-1,-7,-6]).T


# Using built in function 
solution, time_taken = solve_system(A, b)
print("Solution using numpy.linalg.solve:", solution)
print("Time taken:", time_taken, "seconds")
print()

# Using inverse 
solution_inv, time_taken_inv = solve_system(A, b, "inv")
print("Solution using inverse method:", solution_inv)
print("Time taken:", time_taken_inv, "seconds")
print()

# Using LU decomposition 
solution_lu, time_taken_lu = solve_system(A, b, "lu")
print("Solution using LU decomposition:", solution_lu)
print("Time taken:", time_taken_lu, "seconds")
print()


#4.2 Q1 
A1 = np.array([[3, 18, 9], [2, 3, 3], [4, 1, 2]])
b1 = np.array([18, 117, 283])

solution, time_taken = solve_system(A1, b1)
print("Solution for Q1 is ", solution)
print("Time taken:", time_taken, "seconds")
print()

solution, time_taken = solve_system(A1, b1, "inv")
print("Solution for Q1 using inverse is ", solution)
print("Time taken:", time_taken, "seconds")
print()

solution, time_taken = solve_system(A1, b1, "lu")
print("Solution for Q1 using LU decomositon is ", solution)
print("Time taken:", time_taken, "seconds")
print()

#All three methods present the same answer so we can assume it is correct

#4.2 Q2 
A2 = np.array([[20, 15, 10], [-3, -2.24999, 7], [5, 1, 3]])
b2 = np.array([45, 1.751, 9])

solution, time_taken = solve_system(A2, b2)
print("Solution for Q2 is ", solution)
print("Time taken:", time_taken, "seconds")
print()

solution, time_taken = solve_system(A2, b2, "inv")
print("Solution for Q2 using inverse is ", solution)
print("Time taken:", time_taken, "seconds")
print()

solution, time_taken = solve_system(A2, b2, "lu")
print("Solution for Q2 using LU decomositon is ", solution)
print("Time taken:", time_taken, "seconds")
print()
