# this project will ask you to enter your (name) and (age)
# it will print a message telling you how many years left until you reach 100 years old

name= input("Enter your name please: ")
age= int(input("Enter your age please: "))
n= int(input("how many times do you want to see the message: "))
years= 100-age

# print (n*("Hi" + name + " you will turn 100 after "+years+" years.\n"))
# print (n*("Hi %s you will turn 100 after %d years.\n" (name, years)))
print (n*("Hi {} you will turn 100 after {} years.\n" .format(name, years) ))

