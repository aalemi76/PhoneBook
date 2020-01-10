from Classes.PhoneBook import PhoneBook, BColors


print(BColors.BOLD + BColors.HEADER + 'Would you like to make a call from existing phone\
 book and update or you want to make a new phone book:' + BColors.ENDC)
operation = int(input(BColors.BOLD + BColors.HEADER + '1. Working with existing phone book \n2. Building a new one\n'
                      + BColors.ENDC))
if operation == 1:
    name = input(BColors.BOLD + BColors.OKGREEN + 'Enter the name of the Phone book: ' + BColors.ENDC)
    phone_book = PhoneBook(name)
    n = int(input(BColors.BOLD + BColors.HEADER + "Please enter the number of individuals you want to add to\
this phone book: " + BColors.ENDC))
    for i in range(n):
        phone_book.add_phone()
    for i in range(10):
        choice = int(input(BColors.OKGREEN + "If you want to make a call input 1 else enter 0:" + "\n" + BColors.ENDC))
        if choice == 0:
            print(BColors.OKGREEN + "Good Luck" + BColors.ENDC)
            phone_book.save_book(name)
            exit()
        else:
            phone_book.call()
    phone_book.save_book(name)
elif operation == 2:
    name = input(BColors.BOLD + BColors.OKGREEN + 'Enter the name of the Phone book: ' + BColors.ENDC)
    phone_book = PhoneBook()
    n = int(input(BColors.BOLD + BColors.HEADER + "Please enter the number of individuals you want to add to\
this phone book: " + BColors.ENDC))
    for i in range(n):
        phone_book.add_phone()
    for i in range(10):
        choice = int(input(BColors.OKGREEN + "If you want to make a call input 1 else enter 0:" + "\n" + BColors.ENDC))
        if choice == 0:
            print(BColors.OKGREEN + "Good Luck" + BColors.ENDC)
            phone_book.save_book(name)
            exit()
        else:
            phone_book.call()
    phone_book.save_book(name)

# print(BColors.OKBLUE + BColors.BOLD + "Phone Book:" + "\n" + str(phone_book.contacts_list) + BColors.ENDC)
# print(BColors.OKBLUE + BColors.BOLD + "Phone Book:" + "\n" + str(phone_book.inverse_contact) + BColors.ENDC)
