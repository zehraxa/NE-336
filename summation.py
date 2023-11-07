def summation(x, tolerance):
    if abs(x) >= 1:
        print("Error! Absolute value of x must be less than 1")

    result = 0
    value = 1
    n = 0

    while abs(value) > tolerance:
        result += value
        n += 1
        value *= x
    return result

x = float(input("Enter a value for X: "))
tolerance = float(input("Enter a value for tolerance (default will be 1e-5 if left empty): ") or 1e-5)

result = summation(x, tolerance)
print("Using x = " + str(x) + " and tolerance of " + str(tolerance) + " the summation is equal to " +str(result) )