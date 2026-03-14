str1= "My name is basit"
str2= "i am an Artificial Intelligence student"
print(str1 + " " + str2) #string concatenation
print(str1 * 3) #string repetition
print(str1[0]) #string indexing
print(str1[0:4]) #string slicing
print(len(str1)) #length of string
print(str1.upper()) #string method to convert to uppercase
print(str1.lower()) #string method to convert to lowercase
print(str1.split()) #string method to split string into list
print(str1.replace("is", "was")) #string method to replace substring
print(str1.find("is")) #string method to find substring
print(str1.count("a")) #string method to count occurrences of substring
print(str1.startswith("My")) #string method to check if string starts with substring
print(str1.endswith("basit")) #string method to check if string ends with substring
print(str1.isalpha()) #string method to check if string is alphabetic
print(str1.isdigit()) #string method to check if string is numeric
print(str1.isalnum()) #string method to check if string is alphanumeric
print(str1.strip()) #string method to remove whitespace from both ends
print(str1.lstrip()) #string method to remove whitespace from left end
print(str1.rstrip()) #string method to remove whitespace from right end
print(str1.center(20)) #string method to center string in a field of given width
print(str1.ljust(20)) #string method to left justify string in a field of
print(str1[::-1]) #string slicing to reverse string

str5="Life is full of surprises, and what is certain today is uncertain tomorrow.Happiness is a feeling that everyone seeks, but what is happiness for one person is not always happiness for another. The sky is blue, the grass is green, and the sun is bright. What is important is how we react to challenges. Every moment is precious, and every choice is a step toward the future. Learning is continuous, curiosity is natural, and growth is essential. What is yours is yours, and what is shared is love."
print(str5.count("is")) #counting occurrences of "is" in str5
print(str5.replace("is", "was")) #replacing "is" with "was" in str5
print(str5.replace("is","100")) #replacing "is" with "100" in str5
name=input("Please enter your name: ") #asking user for their name
print(len(name)) #printing length of user's name
print(name.upper()) #printing user's name in uppercase  