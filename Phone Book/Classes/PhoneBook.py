from time import time, sleep
import datetime
from random import randrange
from simplejson import loads, dumps


# Color Coding Class
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PhoneBook:
    def __init__(self, name=None):
        try:
            phone_book = open('./{}.json'.format(name), 'r+')
            self.contacts_list = loads(phone_book.read())
            for keys in self.contacts_list.keys():
                self.update_inverse(keys)
        except FileNotFoundError:
            print('There was\'t existed any Phone book with that name {}'.format(name))
            self.contacts_list = {}
            self.inverse_contact = {}
        try:
            self.log_file = open('./log {}.txt'.format(name), 'r+')
            self.log_file.close()
        except FileNotFoundError:
            self.log_file = open('./log.txt', 'w+')
            self.log_file.close()

    def update_contacts(self, name, new_number):
        if type(self.contacts_list[name]) == list:
            self.contacts_list[name].append(str(new_number))
        else:
            self.contacts_list.update(({name: [self.contacts_list[name], str(new_number)]}))

    def update_inverse(self, name):
        try:
            self.inverse_contact = {v: k for k, v in self.contacts_list.items()}
        except TypeError:
            for i in range(len(self.contacts_list[name])):
                self.inverse_contact.update({self.contacts_list[name][i]: name})

    def record(self, name):
        t0 = time()
        print(BColors.FAIL + "Press 'e' whenever your call ends!" + BColors.ENDC)
        operation = input()
        space1 = ' '
        space2 = ' '
        if operation == "e":
            duration = int(time() - t0)
            print(BColors.OKGREEN + "Your call has finished" + BColors.ENDC)
            print(BColors.OKBLUE + "Your call took {} seconds long".format(duration) + BColors.ENDC)
            date = datetime.datetime.now()
            with open('./log.txt', 'a') as self.log_file:
                space1 *= (25 - len(name))
                space2 *= (25 - len(str(duration)))
                self.log_file.write('\n' + 'Called {}'.format(name) + space1 + 'duration: {}'.format(duration) +
                                    space2 + 'date: {}'.format(date))

    def add_phone(self):
        name = input(BColors.HEADER + BColors.BOLD + 'Please enter person name: ' + BColors.ENDC)
        if name in self.contacts_list:
            print(BColors.FAIL + "You have added {} in contact list previously. Would you like update contact details?"
                  .format(name) + BColors.ENDC)
            print(BColors.OKGREEN, "1. Yes \n 2. No, I want to add another {}".format(name), BColors.ENDC)
            choice = int(input(BColors.OKGREEN + "Please select an option: " + BColors.ENDC))
            if choice == 1:
                new_number = input(BColors.HEADER + "Please enter phone number: " + BColors.ENDC)
                print(BColors.FAIL + "If you want to replace phone number enter 1 else enter 0 to add it to {} contacts"
                      .format(name) + BColors.ENDC)
                op = int(input())
                if op == 1:
                    self.contacts_list.update({name: new_number})
                elif op == 0:
                    self.update_contacts(name, new_number)
            elif choice == 2:
                number = input(BColors.HEADER + "Please enter phone number: " + BColors.ENDC)
                self.contacts_list.update({name + str(1): number})
                print(BColors.OKGREEN + "Person {} was added to your phone book as {}!".format(
                    name, name + str(1)) + BColors.ENDC)
        else:
            phone_number = input(BColors.HEADER + BColors.BOLD + 'Please enter person phone number: ' + BColors.ENDC)
            self.contacts_list.update({name: phone_number})
            print(BColors.OKGREEN + "Person {} was added to your phone book successfully!".format(name) + BColors.ENDC)
        self.update_inverse(name)

    def call(self):
        print(BColors.OKBLUE + BColors.BOLD + "Please make a choice: " + BColors.ENDC)
        print(BColors.OKBLUE + "                    " + "1. Enter name" + "\n"
              + "                    " + "2. Enter phone number" + BColors.ENDC)
        choice = int(input(BColors.OKGREEN + 'Select an option: ' + BColors.ENDC))
        if choice == 1:
            name = input(BColors.HEADER + 'Please enter name: ' + BColors.ENDC)
            try:
                number = self.contacts_list[name]
                if type(number) == list:
                    print(BColors.HEADER + "{}".format(number) + BColors.ENDC)
                    for i in range(len(number)):
                        print(BColors.OKGREEN + "{}: {}".format(i + 1, number[i]))
                    index = int(input(BColors.WARNING + "Please make a choice between available phone numbers: "
                                      + BColors.ENDC)) - 1
                    print(BColors.OKBLUE + "Calling {} via {}....".format(name, number[index]) + BColors.ENDC)
                    sleep(randrange(0, 20))
                    print(BColors.OKGREEN + "{} has just answered the phone!".format(name) + BColors.ENDC)
                    self.record(name)
                else:
                    print(BColors.WARNING + "Would you mean {} with this phone number: {}".format(name, number)
                          + BColors.ENDC)
                    print(BColors.BOLD + "1. Yes" + "\n" + "2. No, I want to add another number for {}".format(name)
                          + BColors.ENDC)
                    choice3 = int(input(BColors.OKGREEN + 'Select an option: ' + BColors.ENDC))
                    if choice3 == 1:
                        print(BColors.OKBLUE + "Calling {} via {}....".format(name, number) + BColors.ENDC)
                        sleep(randrange(0, 20))
                        print(BColors.OKGREEN + "{} has just answered the phone!".format(name, number) + BColors.ENDC)
                        self.record(name)
                    else:
                        new_number = int(input(BColors.HEADER + "Please enter phone number: " + BColors.ENDC))
                        self.update_contacts(name, new_number)
                        self.update_inverse(name)
                        print(BColors.OKBLUE + "Calling {} via {}....".format(name, new_number) + BColors.ENDC)
                        sleep(randrange(0, 20))
                        print(BColors.OKGREEN + "{} has just answered the phone!".format(name) + BColors.ENDC)
                        self.record(name)
            except KeyError:
                print(BColors.FAIL + "Person {} was not found in Contact list. Would you like to add him?".format(name)
                      + BColors.ENDC)
                print(BColors.OKBLUE + "1. Yes add him to contact list." + "\n" + "2. No" + BColors.ENDC)
                choice2 = int(input(BColors.OKGREEN + 'Select an option: ' + BColors.ENDC))
                if choice2 == 1:
                    phone_num = input(BColors.HEADER + "Please Enter Phone number:" + BColors.ENDC)
                    self.contacts_list.update({name: phone_num})
                    self.update_inverse(name)
                    print(BColors.OKBLUE + "Calling {} via {}....".format(name, phone_num) + BColors.ENDC)
                    sleep(randrange(0, 20))
                    print(BColors.OKGREEN + "{} has just answered the phone!".format(name) + BColors.ENDC)
                    self.record(name)
                else:
                    phone_num = input(BColors.HEADER + "Please Enter Phone number:" + BColors.ENDC)
                    print(BColors.OKBLUE + "Calling {} via {}....".format(name, phone_num) + BColors.ENDC)
                    sleep(randrange(0, 20))
                    print(BColors.OKGREEN + "{} has just answered the phone!".format(name) + BColors.ENDC)
                    self.record(name)
        elif choice == 2:
            phone_number = input(BColors.HEADER + 'Please enter Phone number: ' + BColors.ENDC)
            try:
                name = self.inverse_contact[phone_number]
                print(BColors.OKBLUE + "Calling {} via {}....".format(name, phone_number) + BColors.ENDC)
                sleep(5)
                print(BColors.OKGREEN + "{} has just answered the phone!".format(name) + BColors.ENDC)
                self.record(name)
            except KeyError:
                print(BColors.FAIL +
                      "There was not any number in contact list matching {}.Would you like to add him?"
                      .format(phone_number) + BColors.ENDC)
                print(BColors.OKBLUE + "1. Yes add him to contact list." + "\n" + "2. No" + BColors.ENDC)
                choice2 = int(input(BColors.OKGREEN + 'Select an option: ' + BColors.ENDC))
                if choice2 == 1:
                    name = input(BColors.HEADER + "Please Enter a name: " + BColors.ENDC)
                    if name in self.contacts_list:
                        self.update_contacts(name, phone_number)
                        self.update_inverse(name)
                    else:
                        self.inverse_contact.update({phone_number: name})
                        self.contacts_list.update({name: phone_number})
                    print(BColors.OKBLUE, "Calling {} via {} ...."
                          .format(self.inverse_contact[phone_number], phone_number), BColors.ENDC)
                    sleep(randrange(0, 20))
                    print(BColors.OKGREEN + "{} has just answered the phone!".format(name) + BColors.ENDC)
                    self.record(name)
                else:
                    print(BColors.OKBLUE + "Calling {} via {} ....".format('Unknown', phone_number) + BColors.ENDC)
                    sleep(randrange(0, 20))
                    print(BColors.OKGREEN + "{} has just answered the phone!".format('Unknown') + BColors.ENDC)
                    self.record('Unknown')

    '''def open_book(self, name):
        try:
            phone_book = open('./{}.json'.format(name), 'r+')
            self.contacts_list = loads(phone_book.read())
            for keys in self.contacts_list.keys():
                self.update_inverse(keys)
        except FileNotFoundError:
            print('There was\'t existed any Phone book with that name {}'.format(name))'''

    def save_book(self, name):
        try:
            phone_book = open('./{}.json'.format(name), 'r+')
            phone_book.seek(0)
            phone_book.write(dumps(self.contacts_list))
            phone_book.close()
        except FileNotFoundError:
            phone_book = open('./{}.json'.format(name), 'w+')
            phone_book.seek(0)
            phone_book.write(dumps(self.contacts_list))
