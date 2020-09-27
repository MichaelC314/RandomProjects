import random as r

lengthOfPassword = int(input("Enter how long you want the password to be: "))

# Variables
charStr = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./`!@#$%^&*()_+QWERTYUIOP|ASDFGHJKL:ZXCVBNM<>?"
allPossibleIndexes = len(charStr) - 1
password = ""

for _ in range(lengthOfPassword):
    index = r.randint(0, allPossibleIndexes)
    password += charStr[index]

print(f"Here is your password: {password}")