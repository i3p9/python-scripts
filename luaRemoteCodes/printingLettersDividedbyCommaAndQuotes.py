months = "January" #Prints Foo to "F","o","o" [for printing words via remote.lua]
month = ["January", "February", "March", "April", "May", "June", "July","August","September","October","November","December"]
mon = []

for x in range(12):
    res = '\", \"'.join(month[x][i:i + 1] for i in range(0, len(month[x]), 1)) 
    print("\"%s\"" %(res))