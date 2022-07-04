
oll = []
while True:
    a = int(input("введите: "))
    if a in oll:
        print("error")
    else:
        oll.append(a)
        print(oll)

