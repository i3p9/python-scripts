tab = ' ' #Prints the day actions in remote.lua

for x in range(31):
    print("actions.day%i = function ()" %(x+1))
    if(x<9):
        print("%skb.stroke(\"d0\",\"d%i\");" %(tab*4,x+1))
    elif(x<19):
        print("%skb.stroke(\"d1\",\"d%i\");" %(tab*4,x-9))
    elif(x<29):
        print("%skb.stroke(\"d2\",\"d%i\");" %(tab*4,x-19))
    else:
        print("%skb.stroke(\"d3\",\"d%i\");" %(tab*4,x-29))
    print("end")
    print("\n")