import random

def listoverlap(list1, list2):
    set_list1 = set(list1)
    set_list2 = set(list2)
    list3 = set_list1 & set_list2
    print(list3)
    return list(list3)


def main():
    list1 = [random.randint(1,10) for i in range(10)]
    list2 = [random.randint(1,20) for i in range(20)]

    print(list1, list2)
    listoverlap(list1, list2)
    return


if __name__ == '__main__':
    main()
