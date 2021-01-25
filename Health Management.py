# health management system
import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food:"))
        if c == 1:
            value = input("Type which exercise have you do\n")
            with open("Suchitra-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("Type which food have you eat \n")
            with open("Suchitra-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 2:
        c = int(input("enter 1 for excersise and 2 for food\n"))
        if c == 1:
            value = input("type here\n")
            with open("saloni-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("saloni-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 3:
        c = int(input("enter 1 for excersise and 2 for food\n"))
        if c == 1:
            value = input("type here\n")
            with open("supriya-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("supriya-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Suchitra),2(saloni),3(supriya)")


def retrieve(k):
    if k == 1:  # Suchitra
        c = int(input("enter 1 for excersise and 2 for food\n"))
        if c == 1:
            with open("Suchitra-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Suchitra-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:  # saloni
        c = int(input("enter 1 for excersise and 2 for food\n"))
        if c == 1:
            with open("saloni-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("saloni-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:  # supriya
        c = int(input("enter 1 for excersise and 2 for food\n"))
        if c == 1:
            with open("supriya-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("supriya-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Suchitra, saloni, supriya)")


print("Health Management System: ")
a = int(input("press 1 for take the value and 2 for retrieve\n "))

if a == 1:
    b = int(input("press 1 for Suchitra 2 for saloni 3 for supriya\n "))
    take(b)
else:
    b = int(input("press 1 for Suchitra 2 for saloni 3 for supriya\n "))
    retrieve(b)
