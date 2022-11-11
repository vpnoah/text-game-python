def interestCalculator (amount, rate, iterations):

    for x in range(iterations):
        amount = amount*rate
    
    return amount

def fibbonaci (x):
    first = 1
    second = 1
    num = 0

    if(x<=2):
        return 1
    
    for b in range(x-2):

        num = first+second
        first = second
        second = num

    return num



    





