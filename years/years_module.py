import datetime


def years(age):
    age_diff = 100 - age
    today = datetime.date.today()
    return int(today.year) + age_diff


def main():
    user_input = input("Please give me your name: ")
    user_input_2 = int(input("Please give me your age: "))
    print("Welcome " + user_input)
    years(user_input_2)
    print("Dear " + user_input + ", you will turn 100 in " + str(years(user_input_2)))
    return


if __name__ == '__main__':
    main()
