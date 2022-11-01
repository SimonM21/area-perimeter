# checks that users enter a number that is more than zero 
def num_check(question):
    valid = False
    while not valid:

        error = "please enter a number more than a zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:   
            print(error)

print()
print("*** are perimeter calculator ****")
print()


keep_going = ""
while keep_going == "":
    

    # get width and height, check if they are more than zero (using number checking function)
    width = num_check("width: ")
    height = num_check("height: ")

    # calculator and perimeter
    area = width * height

    perimeter= 2 * (width + height)
    

    # output answer, format to 2dp
    print("Perimeter: {:.2f} units".format(perimeter))
    print("Area: {:.2f} square units".format(area))
    print()

    keep_going = input("press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")