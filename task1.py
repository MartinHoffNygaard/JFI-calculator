#Creates the function with two inputs which are meant to be throughput vlaues. The function calculates the JFI.
#The function does not handle any exception as the task says is should take in two values which is int or float.
def jains(tp1, tp2):
    #Creates the jfi variable which will contain the JFI. Calculates the JFI my completing the JFI formula with the two
    #input values.
    jfi = ((tp1 + tp2)**2) / (2*(tp1**2 + tp2**2))
    #Returns the JFI.
    return jfi





