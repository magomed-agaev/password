# def create_password():
#     password = input("Enter your password: ")
#     return password
    

# mdp = create_password()

# while len(mdp) == 0:
#     create_password()


password = input("Enter your password")

def check(s):
    check_pass = [False, False, False, False, False]

    if len(s) >= 8:
        check_pass[0] = True
    for i in s:
        if i in "azertyuiopqsdfghjklmwxcvbn":
            check_pass[1] = True
        if i in "AZERTYUIOPQSDFGHJKLMWXCVBN":
            check_pass[2] = True
        if i in "1234567890":
            check_pass[3] = True
        if i in ":/!§;.,?%$£*¨^-+":
            check_pass[4] = True
    if sum(check_pass) == 5:
        print("Password is good")
        return True
    else:
        print("Password not good")
        return False

check(password)




