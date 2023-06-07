#!/usr/bin/python3
def fizzbuzz():
    for ii in range(1, 101):
        if ii % 3 == 0 and ii % 5 == 0:
            print("FizzBuzz ", end="")
        elif ii % 3 == 0:
            print("Fizz ", end="")
        elif ii % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(ii), end="")
