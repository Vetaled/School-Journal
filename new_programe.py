class School(object):
    """Класс - школа"""

    amount = 0

    @staticmethod
    def amounting():
        print("Cейчас учеников: ", School.amount)

    def __init__(self, name, phone, marks_m, marks_l, marks_p):
        self.name = name
        School.amount += 1
        self.__phone = phone
        self.__marks_m = marks_m
        self.__marks_l = marks_l
        self.__marks_p = marks_p

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone
        print("Phone changed successfully.\n")

    @property
    def mark_m(self):
        return self.__marks_m

    @mark_m.setter
    def mark_m(self, new_marks):
        self.__marks_m = new_marks
        print("Math mark changed successfully.\n")

    @property
    def mark_l(self):
        return self.__marks_l


    @mark_l.setter
    def mark_l(self, new_marks):
        self.__marks_l = new_marks
        print("Language mark changed successfull.\n")

    @property
    def mark_p(self):
        return self.__marks_p

    @mark_p.setter
    def mark_p(self, new_marks):
        self.__marks_p = new_marks
        print("Physics mark changed successfully.\n")

    def __str__(self):
        rep = "Ученик " + self.name + " имеет номер " + str(self.__phone) + " .\n" + "Math - " + str(
            self.__marks_m) + "\n" + "Language - " + str(self.__marks_l) + "\n" + "Physics - " + str(
            self.__marks_p) + "\n"
        return rep


a = School("Garik", 689010, 1, 2, 3)
b = School("Vasiliy", 706765, 1, 2, 3)
c = School("Viktor", 323443, 1, 2, 3)
students = [a, b, c]


def Exit():
    print("\nThanks for using our school system.\n")
    print("\nPush 'Enter' for close this programme.\n")
    exit()


def Edit(password):
    if password == 551408:
        print("What do you want to edit?")
        print("1 - Phone")
        print("2 - Marks")
        print("3 - Back")
        choice = input()
        if choice == "1":
            Edit_phones()
        elif choice == "2":
            Edit_marks()
        elif choice == "3":
            print("Go back to menu.\n")
        else:
            print("Not correct.\n")
            Edit(551408)
    else:
        print("Error")


def Edit_marks():
    print("Choice the NUMBER of student.\n")
    for i in range(len(students)):
        print(str(i + 1) + ")", students[i].name)
    try:
        index = int(input(" "))
        a = students[index - 1]
    except IndexError:
        print("Error NUMBER!\n")
        Edit_marks()
    except ValueError:
        print("Error NUMBER!\n")
        Edit_marks()
    else:
        if students[index-1]:
            try:
                new_marks = int(input("Enter the mark that you want to put.\n"))
            except ValueError:
                Edit_marks()
            else:
                if 0 <= new_marks <= 10:
                    print("What subject will you want to change?\n")
                    print("m/l/p\n")
                    subject = input()
                    if subject.lower() == "m" and new_marks != "":
                        students[index - 1].mark_m = new_marks
                    elif subject.lower() == "l" and new_marks != "":
                        students[index - 1].mark_l = new_marks
                    elif subject.lower() == "p" and new_marks != "":
                        students[index - 1].mark_p = new_marks
                    else:
                        print("Error.\n")
                        Edit_marks()
                else:
                    print("Wrong mark.\n")
                    Edit_marks()
        else:
            print("Student not found\n")


def Edit_phones():
    print("Choice the NUMBER of student.\n")
    for i in range(len(students)):
        print(str(i + 1) + ")", students[i].name)
    try:
        index = int(input("Number - "))
        a = students[index - 1]
    except IndexError:
        print("Error NUMBER!\n")
        Edit_phones()
    except ValueError:
        print("Error NUMBER!\n")
        Edit_phones()
    else:
        if students[index - 1]:
            try:
                new_phone = int(input("Enter new phone.\n"))
            except ValueError:
                print("Error phone!\n")
                Edit_phones()
            else:
                if len(str(new_phone)) == 6:
                    students[index - 1].phone = new_phone
                else:
                    print("Phone isn`t correct.\n")
                    Edit_phones()


def Students_INFO():
    print("\nName of student - Phone\n")
    print("Marks...\n")
    for i in range(len(students)):
        print(str(i + 1) + ")", end=" ")
        print(students[i])


def Amount_of_sudents():
    print(School.amount, " - amount of students in the class.\n")


def main():
    print("""Hellow. This is an electronic journal of our class.""")
    while True:
        print("""\t\t\tWhat can you find here?
        1 - Amount of persons in the class.
        2 - Marks,name,phones of all children in the class.
        3 - Only for teacher!(Edit marks and phones)
        4 - Exit\n""")

        try:
            choice = int(input("Select menu item:\n"))
        except ValueError:
            print("Error.\n")
        else:
            if choice == 1:
                Amount_of_sudents()
            elif choice == 2:
                Students_INFO()
            elif choice == 3:
                print("Enter a teacher`s password.\n")
                try:
                    password = int(input())
                except ValueError:
                    print("Error.")
                else:
                    Edit(password)
            elif choice == 4:
                Exit()
            else:
                print("Item not found.\n")


main()
