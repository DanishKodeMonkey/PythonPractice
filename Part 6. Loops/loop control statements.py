# Loop control statements change a loops execution from its normal sequence

#   Break = used to terminate the loop entirely
#Note that != means "does not equal"
#This code therefor states that "While name does not equal an input, repeat until input has a name, then break the loop"
#while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

# Continue = skips to the next iteration of the loop.
#Here we will try to display a phone number without the dashes
phone_number = "123-456-7890"
#So for i, each character, in phone_number we check if we encounter a dash(-) if we do, continue and skip the itteration.
#Then we print the remaining digits. In other words if the loop encounters a dash(-) it will skip that iteration
#if it encounters a digit, or anything else, it will print it.
#in order to print all the digits in one line write end="".
#for i in phone_number:
#    if i =="-":
#        continue
#    print(i, end="")

#Pass does nothing, and acts as a placeholder.
#So when you use a pass it simply does not do it the thing.

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)