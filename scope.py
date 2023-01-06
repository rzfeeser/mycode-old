#!/usr/bin/python3


# the house main built
def main():
    x = "hello from main" 
    print(x)
    


    print(welcome(x))  # pass in the LOCAL value from main() to welcome()

    x = welcome(x)

    print(x)

    print(frog2)




# the house of welcome
def welcome(frog):  # the function expects the var "x" to be passed
    global frog2
    frog2 = frog + " and from welcome"




if __name__ == "__main__":
    main()
