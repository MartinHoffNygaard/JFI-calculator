#Creates function which will take a list of throughputs and calculate the JFI. The task says the input should be a list
#with int or floats and we therefore dont need to handle exceptions.
def jainsall(tplist):
#Create two variables which will hold the summations of the summation symbols in the JFI formula
    sum1 = 0
    sum2 = 0
#Calculates and stores the first summation of JFI formula
    for tp in tplist:
        sum1 += tp
    sum1 = sum1**2
#Calculates and stores the second summation of JFI formula. Uses the len() command to find number of items in list for N
    for tp in tplist:
        sum2 += tp**2
    sum2 = sum2 * len(tplist)
#Calculates the JFI by dividing the two summation and stores it in the jfi variable
    jfi = sum1 / sum2
#Returns the JFI for the list og throughputs
    return jfi
