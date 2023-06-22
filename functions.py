import math


def motto():
    print("Hello this is our motto")
motto()
def vision():
    print("Hello, this is our Vision")
vision()

def add():
    x = 10
    y = 20
    z = x + y
    print(z)
add()

def avg(x, y, z):
    average = (x + y + z)/3
    print("Your average is "+str(average))
avg(12, 34, 56)

def bmiCalc(weight, height):
# pow means power
    bmi = weight / pow(height, 2)
    if bmi <= 18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal Weight")
    elif bmi <= 34:
        print("Overweight")
    else:
        print("Obese")
bmiCalc(90, 1.8)
# create a function to implement a simple grading system
def gradingSystem(marks):
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
gradingSystem(40)

# create a function to implement a simple login system to ascertain the user has
# entered "user@example.com" as email and "user123" as password.
# henceforth,invoke the grading function above to perform the grading functionality

def login():
    user_database = {
        'user@example.com': 'user123'
    }
    email = input("Enter Email: ")
    password = input("Enter password: ")

    if email in user_database:
        if password == user_database[email]:
            def gradingSystem(marks):
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
            gradingSystem(80)
        else:
            print("incorrect")
    else:
        print("Incorrect")


def areaOfACircle(radius):
    area = math.pi * pow(radius, 2)
    return area
print(areaOfACircle(20))