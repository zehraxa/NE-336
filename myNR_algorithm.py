# NE 336 Lab 1  Group 2 Sept 26 2023 - myNR
# Written by Zehra Ahmed - 20889523 

def myNR(myfun, x0, myfund = None):
    tolerance = 1e-6
    error = 1
    i = 0 
    x_list = [x0]

    if myfund == None:
        #Using secant methond to find derivative and then NR method for roots
        while error > tolerance and i < 1000:
            x1 = x_list[i] + x_list[i]*0.01
            #Approx derivative: 
            myfundapprox = (myfun(x_list[i]) - myfun(x1))/ (x_list[i]-x1)
            #NR method: 
            xnew = x_list[i] - (myfun(x_list[i])/myfundapprox)
            x_list.append(xnew)
            #Find error
            error = abs((x_list[i+1] - x_list[i])/x_list[i+1])
            i+=1


    else:
         while error > tolerance and i < 1000:
            #Using provided derivative and NR method for roots
            xnew = x_list[i] - (myfun(x_list[i])/myfund(x_list[i]))
            x_list.append(xnew)
            #Find error
            error = abs((x_list[i+1] - x_list[i])/x_list[i+1])
            i+=1

    if i == 1000: 
        print("No roots found")
    else: 
        print(f"Root found after {i} iterations")

    return (xnew, error)
                
   

if '__name__' == '__main__': 
    f = lambda x: x**5 - 11*x**4 + 43*x**3 - 73*x**2 +56*x -16
    fd= lambda x: 5*x**4 - 44*x**3 + 129*x**2 - 146*x + 56
    x0 = -2
    print(myNR(f , x0))
