def palindrome(str):
    text = str
    text = text.upper()
    text = text.replace(" ", "")
    j = 1
    for i in text:
        if i == text[-j]:
            j += 1

        else:
            return False
    return True


def main():
    user_input = input("Text: ")
    if palindrome(user_input):
        print("palindrome")
    else:
        print("not palindrome")
    return


if __name__ == '__main__':
    main()
