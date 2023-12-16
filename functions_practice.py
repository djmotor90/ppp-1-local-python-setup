# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print("Hello")


# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(arg1, arg2, arg3):
    return[arg1, arg2, arg3]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + lunch[0])
        for i in range(1, len(lunch)):
            print("Next I eat " + lunch[i])

# result

if __name__ == "__main__":
    hello()
    print(pack(1, 2, 3))
    print(pack("a", "b", "c"))
    eat_lunch(["apple", "banana", "orange"])
    eat_lunch([])