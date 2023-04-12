#Slicing creates a substring by extracting elements from an existing string
#This method can also be applied to other operations, but string will be used here.

#When slicing there are 3 optional arguments to keep in mind regardless of the function used.
#[start:stop:step]
#depending on the where and how we want to slice a string

#The slice function
#The slice function creates a slice object which is reuseable, effectively "cutting out" a portion of a string
#Example, cutting out the word google from a link.

website1 = "http://google.com"
website2 = "http://wikipedia.com"
#The slice function uses commas instead of collons to seperate the optinal arguments, but works the same way otherwise.
#a useful tip is that you can also use a negative index to count BACK from the end of the string
#Think of it like a positive index, counting the number of letters to the right ->
#while a negative index counts the letters to the left <-
slice = slice(7,-4)
#We now have our slice object, and can use this further down the code.

print(website1[slice])

#Lets try again with another website to make sure it works, the other website being defined above
print(website2[slice])

#BOOM! it works, we effectively made our own tool(object) to use in the code.