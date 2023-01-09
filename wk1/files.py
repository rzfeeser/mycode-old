

def file_creator(lines_to_write):
    """accepts a string and writes it into a file"""
    fo = open('myfile.txt', 'w')

    # functionally the same except for how the line is terminated
    print(lines_to_write, file=fo)   # ends with a "\n"
    fo.write(lines_to_write + "\n")  # does not end with a "\n"
    fo.close() # if you don't use with you must close your file

    # alternative way to create a file object
    with open('myfile.txt', 'a') as fo:
        print(lines_to_write, file=fo)
        fo.write(lines_to_write + "\n")
        # no need to close, closes automatically when the indentation ends

    # end of the function
    return


def file_reader():
    """returns the contents of our file"""
    with open('myfile.txt', 'r') as fileobject:
        x = fileobject.read()  # return a blob of text
        # x = fileobject.readlines() # returns a blob of text with each line in a list
    return x


def main():
    """run time"""

    file_creator("Rock and roll weekend")

    print(file_reader())   # General rule - we don't want our function to print
                           # we want main to do our prints


    # generally, the way we work across files is the following
    with open('startrek.txt', 'w') as sttng:
        sttng.write("These are the voyages of the starship, Enterprise \n")
        sttng.write("Its continuining mission is to explore strange new worlds, Enterprise \n")
        sttng.write("To seek out new life")
        sttng.write("To boldly go where no one, Enterprise \n")
    
    total = 0 # start a counter
    # this opens the file in read mode (r) this is the default
    with open('startrek.txt') as sttng:
        for line in sttng:
            if "Enterprise" in line:
                total += 1   # increase a counter by 1
    print("the total number of instances of the word 'Enterprise' is,", total)

if __name__ == "__main__":
    main()
