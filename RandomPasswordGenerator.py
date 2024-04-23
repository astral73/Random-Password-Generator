import random as rd

print("Welcome Random Password Generator (RpG) created by Astral")
while 1:
    try:
        passwordSize = int(input('Please Enter Password Size (Enter -1 for quitting): '))
    except:
        print("Are You Dumb? This is not a number asshole! Don't disturb me again, idiota >:|")
        quit()

    if passwordSize == -1:
        print("Bye Bye!")
        quit()

    elif passwordSize == 0:
        print("No Password Generated!!! Try Harder...")

    else:
        passwordList = []

        for i in range(0, passwordSize):
            passwordList.append(chr(rd.randint(33, 126)))
            
        converted_list = map(str, passwordList)
        password = ''.join(converted_list)

        print("Your password is:" + password)