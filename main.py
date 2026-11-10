n = 1000

listaca = list(range(0, 1001))

print("Start")

for num in listaca:
    if listaca[num] % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

print("Done")