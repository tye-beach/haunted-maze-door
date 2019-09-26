import time

password = "12345"

entry=input("Enter the password: ")

while entry!=password:
    print("Try again")
    entry=input("Enter the pasword: ")

print("Password correct")
time.sleep(1)
print("You may exit")
time.sleep(10)
print("Door locked")