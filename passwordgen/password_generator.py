import random


# shuffling function for characters
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return "".join(templist)


# main program starts here
upper1 = chr(random.randint(65, 90))  # chr function is used to turn integers into the designated characters askee code
upper2 = chr(random.randint(65, 90))
lower1 = chr(random.randint(97, 122))
lower2 = chr(random.randint(97, 122))
digit1 = str(random.randint(1, 9))
digit2 = str(random.randint(1, 9))
pun1 = chr(random.randint(35, 38))
pun2 = chr(random.randint(35, 38))

# combining the characters together
password = upper1 + upper2 + lower1 + lower2 + digit1 + digit2 + pun1 + pun2
# shuffling the characters
password = shuffle(password)

print(f"Generated Password: {password}")

