# Project Name - Random Password Generator 

import random
import string

pass_len = 4   #can change the length anyway
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Your random password is : ", password)
