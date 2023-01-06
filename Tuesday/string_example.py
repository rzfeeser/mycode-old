#!/usr/bin/python3
"""RZFeeser | RZFeeser@alta3.com
Understanding String types and methods"""

def main():
    """runtime"""
    deep_space = input("What is the outpost number the Federation took over? ")

    # decision making with if/then logic
    if deep_space.isnumeric():  # if it evaluates as true
        deep_space = int(deep_space) + 1
        print(deep_space)
    else: # in all other cases...
        print("I cannot convert what you typed in")


    startrek = "next generation"
    print(startrek)        # entire string
    print(startrek[0:5])   # just "next"
    print(startrek[-10:])  # start @ g in generation and go to end

    print(startrek[-2])    # just display o in generation


if __name__ == "__main__":
    main()
