#Small Number guessing Name
import random
secret = random.randint(1,20)
guess = 0
atmept = 0
print("The Number is B/W 1 to 20")

while guess != secret:
    guess = int(input("Guess The Number:"))
    atmept+=1
    if guess > secret:
        print("The Number you Choose is Very High")
    if guess < secret:
        print("The number you Choose is Very low")
else:
    print(f"You Are the Winner and you atmept {atmept}")

#Small Calculator
Operators = input("Enter An operator(+,=,/,*):")
Number1 = float(input("Enter the Number:"))
Number2 = float(input("Enter the Number:"))

if Operators == "+":
    Answer = Number1+Number2
    print(Answer)
elif Operators == "-":
    Answer = Number1-Number2
    print(Answer)
elif Operators == "*":
    Answer = Number1 * Number2
    print(Answer)
elif Operators == "/":
    Answer = Number1/Number2
    print(Answer)
else:
    print("The Operator is Incorrect")



