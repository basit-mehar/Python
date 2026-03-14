"""age = int(input("Write your age : "))
if(age >= 18):
    print("You are an adult."  )
elif(age > 13 and age < 18):
    print("You are a teenager.")
else:
    print("You are a child.")
    
    
color = input("write the color : ")
if(color == "red"):
    print("The color is red.")
elif(color == "blue"):
    print("The color is blue.") 
else:
    print("The color is not red or blue.")  
print("The color is :", color)
marks = int(input("Write your marks : "))
if(marks >= 90):
    if(marks >= 95):
        if(marks >= 98):
            print("You got A+ grade.")
        else:
            print("You got A grade.")
    else:
        print("You got B grade.")
if(marks < 90):
            print("passed")
            
#check if a is positive, negative or zero
a = int(input("Write a number : "))
if(a > 0):
    print("The number is positive.")    
elif(a < 0):
    print("The number is negative.")
else:
    print("The number is zero.")
    
#if a is divisible by 2 and 3
a = int(input("Write a number : "))
if(a % 2 == 0 and a % 3 == 0):
    print("The number is divisible by 2 and 3.")
else:    print("The number is not divisible by 2 and 3.")
if(a%2==0):
    print("its Divisible by only 2")
elif(a%3==0):
        print("its Divisible by only 3")
else:
    print("Not divisible by 2 or 3")
#largest of 4 numbers
num1 = int(input("Write a number first :"))
num2 = int(input("Write a number second :"))
num3 = int(input("Write a number third :"))
num4 = int(input("Write a number fourth :"))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("The largest number is : ",num1)
elif(num2 > num3 and num2 > num4):
    print("The largest number is : ",num2)
elif(num3 > num4):
    print("The largest number is : ",num3)
else:
    print("The largest number is : ",num4)"""
    
a=70
if(a%7==0):
        print("its divisible by 7")
else:
        print("not divisible by 7")