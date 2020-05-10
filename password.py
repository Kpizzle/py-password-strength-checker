isMatch = False
while isMatch == False:
    userPassword = input("Enter Password: ")
    confirmPassword = input("Confirm Password: ")
    # print(userPassword)
    # print(confirmPassword)
    if userPassword == confirmPassword:
        isMatch = True
    else:
        print("Passwords do not match, please try again")
#check password length
passwordCount = len(userPassword)
# print("password length is: " + str(passwordCount))

if passwordCount <= 5:
    print("password is weak")
elif passwordCount > 5 and passwordCount <= 8:
    print("password is medium")
elif passwordCount > 8:
    print("password is strong")
else:
    print("cant decode password")

#check for number

#check for special char
