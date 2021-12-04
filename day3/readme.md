# Day 3

## a)
### Reduce 2D array aof bits vertical to two binary numbers according to the most and least used bit in the column

Take 2D array, iterate over lines and count the binary numbers for each position.

After that extrapolate the count into two binary numbers according to which binary digit was used more often.

Convert these binaries to base10 and return their product


## b)
### Multiply two specific numbers: The first number is computed by reducing the set of numbers to only numbers where their digit at that coulumn is the same as the most common digit at the coulumn, traversing the coulmns from left to right, the second number is generated accordingly by reducing over the least common digit 

Iterate over coulumns from left to right:

Count the digits at this coulumn, then determine the most and least used one.

Filter the two sets for the least and most used digit-numbers where the number has that digit at the considered position.

Return the product of the two sets when they were reduced to only containing one element.

## Learinigns
- operations on binary numbers like masking a number to one numerical digit
- using the global keyword
- using functions
- conversions from string to binary and back