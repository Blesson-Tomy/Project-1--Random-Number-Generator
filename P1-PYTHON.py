import random

Name=str(input("Enter your name:"))
print("Welcome to RNG",Name,"!")

start=int(input("Enter the Min limit: "))
end=int(input("Enter the Max limit: "))

num1 = random.randrange(start,end)

print("Your range is from",start,"to",end,"and the number is",num1,".")
 
print("A project by: Blesson")
