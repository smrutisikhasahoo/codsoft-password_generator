import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specific_characters = ['!','@','#','$','%','(',')','_']
print("!!!!!WELCOME TO PASSWORD GENERATOR PROJECT!!!!!\n")
A=int(input("ENTER THE NUMBER OF CHRACTER YOU WANT TO PRINT:--"))
C=int(input("ENTER THE NUMBER OF NUMBER YOU WANT TO PRINT:-- "))
D=int(input("ENTER THE NUMBER OF SPECIFIC CHARACTER YOU WANT TO PRINT:--"))
password = []
for i in range(1,A+1):
    s = random.choice(letters)
    password += s
for i in range(1,C+1):
    s = random.choice(numbers)

    password += s
for i in range(1,D+1):
    s = random.choice(specific_characters)
    password += s
print("THE LIST OD THE PASSWORD IS--",password)
random.shuffle(password)
password_shuffle=""
for i in password:
    password_shuffle += i
print("THE GENERATED PASSWORD IS--",password_shuffle)