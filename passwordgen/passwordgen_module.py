import random
import string

def passwordgen():
    user_input = input("Would you like a strong os weak password? :")
    my_pass = []
    symbol_list = ["@", "?", "!", "%", "+", ">", "#", "^", "&" , "*", "(", ")"]
    if user_input == "strong":
        for i in range (4):
            my_pass.append(str(random.randint(1, 9)))
            my_pass.append (random.choice(string.ascii_letters))
            my_pass.append(random.choice(symbol_list))
        print("Your password is: " + "".join(my_pass))
        my_pass = str(my_pass)
        return (my_pass)
    else:
        mypass_easy = []
        easy = ["Easypass", "Youarehacked", "Lostdata", "Wikileak", "Busted", "Youarescrewed"]
        mypass_easy.append(random.choice(easy))
        print("Your password is: " + mypass_easy[0])
        mypass_easy = str(mypass_easy)
        
    return mypass_easy


def main():
    
    
    passwordgen()

    return


if __name__ == '__main__':
    main()
