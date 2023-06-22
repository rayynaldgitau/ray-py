age = 18
if age < 18:
    print("True")
else:
    print("False")

x = 10
y = 20
if x < y and y > 30:
    print("True")
else:
    print("False")

if x > y or y < 50:
    print("TRUE")
else:
    print("FALSE")

marks = 90
if marks < 40:
    print("E")
elif marks < 50:
    print("D")
elif marks < 60:
    print("C")
elif marks < 70:
    print("B")
else:
    print("A")

bettingNumber = 4
if bettingNumber == 1:
    print("You Won a goat!!")
elif bettingNumber == 2:
    print("You won a Cow!!")
elif bettingNumber == 3:
    print("You won 3 cows!!")
elif bettingNumber == 4:
    print("You won 5 cows!!")
else:
    print("Please enter a number from 1 - 4 to bet.")


# assignment

p = 3000
r = 4
t = 60
interest = (p * r * t)/100
if interest < 1000:
    print("Scam")
elif interest < 5000:
    print("Bad loan")
else:
    print("Good loan")

weight = 70
height = 1.8
BMI = weight / (height * height)
if BMI <= 18:
    print("Underweight")
elif BMI <= 29:
    print("Normal weight")
elif BMI <= 34:
    print("Overweight")
else:
    print("Obese")
