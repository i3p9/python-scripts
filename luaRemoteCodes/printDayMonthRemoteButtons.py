month = ["January", "February", "March", "April", "May", "June", "July","August","September","October","November","December"]

tab = ' '

for x in range(12):
    if(x==0):
        print("Buttons for months")
    print("<button color=\"blue\" text=\"%s\" ontap=\"month%i\" />" %(month[x],x+1)) # priting month Buttons for layout.xml

for y in range(31):
    if(y==0):
        print("Buttons for days")
    print("<button color=\"green\" text=\"%s\" ontap=\"day%i\" />" %(y+1,y+1)) # printing date buttons for layout.xml