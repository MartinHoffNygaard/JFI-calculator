import task2
#opens the text files containing the throughput values
file = open("lab1.txt")
#reads all the lines from the file and stores it in the lines variable
lines = file.readlines()
#Creates an empty list which will contain the throughput values
tplist = []
#Loop to go through each line in the lines variable. For each line we split the line where there is space and only saves
#the first item on each lines in the tplist. Makes the first item in to an integer.
for line in lines:
    tplist.append(int(line.split(' ')[0]))
file.close()
#calculates the JFI with the previously made JFI function from the list of throughput values found in the textfile.
result = task2.jainsall(tplist)




