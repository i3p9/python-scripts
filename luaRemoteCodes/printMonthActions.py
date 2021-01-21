tab = ' ' #Prints the actions for the month section

for x in range(12):
    print("actions.month%i = function ()" %(x+1)) #For the month actions in remote.lua
    if(x<9):
        print("%skb.stroke(\"d0\",\"d%i\");" %(tab*4,x+1))
    else:
        print("%skb.stroke(\"d1\",\"d%i\");" %(tab*4,x-9))
    print("end")
    print("\n")