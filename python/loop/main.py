exp = [2340, 2500, 2100, 3100, 2980]
total = 0
for i in exp:
    total = total + i
   # print(total)
#print(total)
#print(sum(exp))

exp_sort = sorted(exp)
for z in range(len(exp)):
    print(f"Month",z+1,"cost",exp[z])
print("total expense",sum(exp))

for y in range(len(exp)):
    if exp[y] == 2100:
        print(f"znalezione na",y+1,"miejscu")
        break
else:
    print("nie znaleziono")
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for m in range(len(result)):
    if result[m] == "heads":
        count = count + 1

print(f"są", count, "glowy")
for v in range(1,11,2):
    print(v**2)
race = 5
for h in range(1,6):
    print('*' * h)
for km in range(1,race+1):

    answer = input("are you tired?")
    if answer == "yes":
        break
    print("jestes na ",km,"kilometrze")
    if km == 5:
        print("congratulation")
