#!/usr/bin/env python3

# Created by: Cameron Diedrich
# Created on: Nov 2022
# This program finds the Highest Common Factor

import math

def main():
    # Input
    firstNumber = input("Enter first number: ")
    secondNumber = input("Enter second number: ")


    # process
    if firstNumber > secondNumber:
        largeNumber = firstNumber
        smallNumber = secondNumber
    else:
        largeNumber = secondNumber
        smallNumber = firstNumber

        largeNumber / smallNumber


    print ("the highest common factor is {0}.".format(largeNumber))

    print("\nDone.")

if __name__ == "__main__":
    main()
