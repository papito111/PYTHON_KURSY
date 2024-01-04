
sugar = int(input("whats your sugar level"))
if(sugar<80):
    print("malo")
elif(sugar >=80 and sugar <= 100):
    print("ok")
elif(sugar>100):
    print("za duzo")


x = int(input("Podaj liczbe"))
if (x%2 == 0):
    print("parzysta")
else:
    print("nieparzysta")

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
while True:
    y = input("what city is in that country")
    z = input("what city is in that country")

    if (y and z in india):
        print("they are from india")
    elif (y in pakistan and z in pakistan):
        print("they are from pakistan")
    elif (y and z in bangladesh):
        print("they are from bangladesh")
    else:
        print("there is no such a city")
        break

