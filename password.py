import random
#---------Question Box-------
'''print("Hi, Welcome to our website")
A = input("Please enter your name: ")
B = input("Please enter your last name: ")
G = input("Please enter the length of your password string: ")'''
#--------------------------------------------------------------------------------
'''try:
    G = input("Please enter the length of your password string: ")
except AttributeError:
    print("Error")

if int(G) < 8:
    raise Exception("The length of the selected string must be more than 8 charactersn,Please try again")
    G = input("Please enter the length of your password string: ")'''
#--------------------------------------------------------------------------------


#--------random_list------------------
ls_1 = [chr(i) for i in range(65,90)]
ls_2 = [chr(i) for i in range(97,123)]
ls_3 = ['@', '.', '_', '/', '!', ',', '#']
ls_4 = ls_1 + ls_2 + ls_3

#----------Password Creation--------------
password = []

def choice_(G):   
    C = random.choice(ls_1)
    password.append(C)
    D = random.choice(ls_2)
    password.append(D)
    E = random.randint(0, 9)
    password.append(E)   
    F = random.choice(ls_3)
    password.append(F)
    if (int(G) - 4) > 0 :
        for i in range(int(G)-4):
            password.append(random.choice(ls_4))
    else:
        pass
    p = ''  
      
    for i in range(len(password)):
        p += str(password[i])
    return p
#----------------------------------------------------------------------------


if __name__ == "__main__":
    print(choice_())


