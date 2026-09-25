IronMan = input("Enter An operator(+,-,/,*):")
Number1 = float(input("Enter the Number:"))
Number2 = float(input("Enter the Number:"))

if IronMan == "+":
    spiderman = Number1 + Number2
    print(spiderman)
elif IronMan == "-":
    spiderman = Number1 - Number2
    print(spiderman)
elif IronMan == "/":
    spiderman = Number1 / Number2
    print(spiderman)
elif IronMan == "*":
    spiderman = Number1 * Number2
    print(spiderman)
else:
    print("That operator is in correct")


import time
for u in range(1,10):
    print(u)
    time.sleep(0.5)
print("This Is The End")
