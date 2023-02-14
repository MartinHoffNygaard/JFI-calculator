import task2
#opens the text files containing the throughput values
file = open("lab1.2.txt")
#reads all the lines from the file and stores it in the lines variable
lines = file.readlines()
#Creates an empty list which will contain the throughput values
tplist = []
#Loop to go through each line in the lines variable. For each line we split the line where there is space and saves the
#items in a temporary list. We then check if the second item in each line includes K. If it includes k we have to convert
#the first item from Kbps to Mbps by dividing by 1000 and then add it to the tplist. If the second item does not include
#K we do not have to convert and can just add the value to tplist.
for line in lines:
    temp = (line.split(' '))
    if "K" in temp[1]:
        tplist.append(int(temp[0]) / 1000)
    else:
        tplist.append(int(temp[0]))
#calculates the JFI with the previously made JFI function from the list of throughput values found in the textfile.
result = task2.jainsall(tplist)

print(result)

