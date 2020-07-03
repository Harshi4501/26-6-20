str = input("Enter a string: ")
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)
Enter a string: book
Length of the input string is: 4
In [16]:
input_string = "Data Science"
frequencies = {} 
for char in input_string: 
    if char in frequencies: 
        frequencies[char] += 1
    else: 
        frequencies[char] = 1
print ("Per char frequency in '{}' is :\n {}".format(input_string, (frequencies)))