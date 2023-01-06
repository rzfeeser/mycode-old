#!/usr/bin/python3
"""RZFeeser | RZFeeser@alta3.com
solution to challenge 18"""

def main():
    """run time"""

    # input asking for the user's name
    uname = input("What is your name? ")

    # input asking what day of the week it is
    dweek = input("What is the day of the week? ")

    # a print statement that reads as follows:
    # Hello, <name>! Happy <day of the week>!
    print(f"Hello, {uname}! Happy {dweek}!")
    
    print("Hello, " + uname + "! Happy " + dweek + "!")

    print("Hello, ", uname, "! Happy ", dweek, "!", sep="")


if __name__ == "__main__":
    main()
