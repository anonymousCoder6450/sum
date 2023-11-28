def sum_numbers(text):
   list_word = text.split()
   total = 0
   for word in list_word:
       if word.isdigit():
           total += int(word)

   return total
#in this code we use the isdigit() function to check if the element in the string is an integer. Imagine every space, letter and number as an element in the string
#it'll iterate through every single element and see which one is a digit in this case we have 1 and 3 and it will exclude things like "1st", "3rd", etc.


y = sum_numbers("Hello 1 1st, I like 3 apples")

print(y)
