

def num_check(question):

    # loop code until something is returned
    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("oops you did not enter a number")

fav_num = num_check("What is your favourite number? ")
print("You chose", fav_num)

