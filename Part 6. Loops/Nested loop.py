#Nested loops is a general concept of having one loop inside another loop
#The inner loop will finish all of its iterations before finishing one iteration of the "outer loop"

#To demonstrate we draw a rectangle with symbols by using inner and outer loops to determine a witdh and  height of a cube
#First we create a few variables the user can determine
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

#Now we create the nested loops
#The outer for loop will be in charge of the rows
#The inner for loops will be in charge of the columns

#The outer loop i, will only run after the inner loop j, has finished its itterations.
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()