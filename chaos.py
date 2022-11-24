# Author: Kyle Freidhof
# File: chaos.py
# a simple program illustrating chaotic behavior 
# notes: this program is ment as a simple teaching program and explains how it can get more complicated simply


# gives you the option to enter any number and spits it out in 
# range of 20 times

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("How many numbers should i print? "))
    for i in range(20):
        #x = 3.9 * x * (1 - x)
        3.9 * ( x-x * x)
        print(x)
main()

# This one here allows the user to 
# enter any value from 0 an 1 
# and loops it 30 times 

def main():
    print("Another Chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(30):
        x = 3.9 * x * (1 - x)
        print(x)
main()

# This allows the user to enter a number 
# as the last chaotic function
# and loops it in range 
# of 40 times

def main():
    print("Another chaotic function")
    x = eval(input("Enter any number and see the chaos? "))
    for i in range(40):
        3.9 * x - 3.9 * x * x 
        print(x)
main()

def main():
    print("Chose a number")
    x = eval(input("Enter a number between 0 and 1 again? "))
    for i in range(10):
        2.0 * x * (1 - x)
        print(x)
main()

def main():
    print("These numbers are insane")
    x = eval(input("How many numbers do you wish to print? "))
    for i in range(20):
        2.0 * ( x - x * x)
        print(x)

main()


def main():
    print("The last chaotic function")
    x = eval(input("What is the last final number you want to print? "))
    for i in range(30):
        2.0 * x - 2.0 * x * x
        print(x)

main()

exit()