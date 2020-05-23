a = float(input("число 1="))
b = float(input("число 2="))
c = float(input("число 3="))
if a > b:
    print("СВЕРШИЛОСЬ!!!")
elif a < b:
    print("ДА НУ!")
else:
    print("А если так?")
    print("a+c=", int(a+c))
    print("b-c=", int(b-c))
    if int(a+b) > int(b-c):
        print("СВЕРШИЛОСЬ!!!")
    elif int(a+b) < int(b-c):
        print("ДА НУ!")