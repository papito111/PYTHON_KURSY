"""
d = {"tom":66262, "rob": 8318138, "joe": 222234}
print(d["tom"])
name = str(input("napisz imie"))

if name in d:
    print(name, ": numer telefonu: ", d[name])
else:
    print("nie ma takiej osoby")


P = {"China":143,"india":136,"USA":32,"Pakistan":21}
pick = input("1. Print 2. Add 3.Remove")
while True:
    if pick == "1":
        for key in P:
            print(key, "==>", P[key])
    elif pick == "2":
        name = str(input("jaki kraj"))
        number = input("jaka populacja")
        P[name] = number
        for key in P:
            print(key, "==>", P[key])
    elif pick == "3":

        name2 = str(input("podaj nazwe do usuniecia"))
        if name2 in P:
            del P[name2]
            for key in P:
                print(key, "==>", P[key])
        else:
            print("nie ma tego w dictionary")
    elif pick == "4":
        name3 = str(input("wybierz 1 kraj"))
        print(P[name3])
    pick = input("1. Print 2. Add 3.Remove")
"""
import statistics
stocks = {"info":[600,630,620],"rill":[1430,1490,1567],"mtl":[234,180,160]}
def print_all():
    for stock,cena in stocks.items():
        avg = statistics.mean(cena)
        print(stock,"==",cena,"srednia z tego to", round(avg,2))
print_all()