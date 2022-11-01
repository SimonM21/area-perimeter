# chechs that users enter a number that is more than zero

def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that us more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print("Didn't i tell to not put zero")

        except ValueError:   
            print(error)



width = num_check("What is the width? ")
height = num_check("What is blueeghh the height? ")

print()
print("The width is", width)
print("The height is", height)
