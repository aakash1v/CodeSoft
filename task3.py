'''
TASK 3  -   PASSWORD GENERATOR
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the
password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen.
'''

import random
import string


nouns = ['Naruto','Madara','Kakashi','Itachi','Sakura','Vegeta','Asta','Eren','Gabimaru','Aizen']
adjectives = ['saringan','rasengan','rennigan','uchia','uzumaki','demon','king','hokage','genin','fool','funny','powerful']

#easy password 
def weak_pw():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    num = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)


    password = adjective + noun + str(num) + special_char
    return password


#strong password  
def strong_pw():
    
    print("Enter the length of the password :")
    pw_length = int(input())

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password = ""

    for i in range(pw_length):
        password += random.choice(characters)

    return password

    

while True:

    print("Enter the complexity of password : strong/weak ")
    if input().lower().startswith('s'):
        password = strong_pw()
    else:
        password = weak_pw()

    print("The password is %s"%password)

    #checking if user need other password
    print("Do you want more password suggestions ?")
    if not input().lower().startswith('y'):
        break
    
print("\nBye Bye...")



