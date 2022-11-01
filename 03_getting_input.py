#ask the user for their name
username = input("what is your name? ")

#Ask the user for their favorite interger
fav_num = int(input("Favorite Number? "))

#double, halve and square the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

print()
#Greet the user
print("Hi {}, you favorite number is {}".format(username, fav_num))
print()
#output the result of doubling, halving 
# and squaring their favorite number
print("double {} is {}".format(fav_num, double))
print("half {} is {}".format(fav_num, half))
print("{} squared is {}".format(fav_num, squared))
print()