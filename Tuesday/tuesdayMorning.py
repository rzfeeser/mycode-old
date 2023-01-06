#!/usr/bin/python3
"""rzfeeser@alta3.com | Tuesday morning review
Reviewing use of standard library. Also looking at best practice techniques."""

def main():

    # display this string to this screen
    print("Hello team")

    # collect user input
    user_name = input("What is your name? ") # input always collects a string

    # collect user color
    user_color = input("What is your favorite color? ")

    # display name
          # string        #string
    print("Your name: " + user_name) # if you're going to concatenate, all types must be the same!

          #string       #string
    print("Your name:", user_name) # if you're going to pass in a list of objects
    # the types don't all need to be the same

    # display color
    print("Your favorite color:", user_color)


# this condition is TRUE when someone calls the script directly
# this condition is FALSE when someone imports the script
if __name__ == "__main__":
    main()
