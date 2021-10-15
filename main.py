from Student import Student

input_file = "files/data_file.txt"


def init_data():
    data_file = open(input_file)

    for single_data in data_file:
        if single_data.strip() != "":
            new_student = Student(single_data[1], single_data[2], single_data[3], single_data[4])

    data_file.close()


def view_data():
    print("")

    student_id = input("Enter Student Id : ")
    if student_id != "":

        data_file = open(input_file, "r")

        print("ID  |  F. Name  |  L. Name  |  Age  |  Country ")
        print("-----------------------------------------------")

        for single_data in data_file:

            if single_data.strip() != "":
                data_array = single_data.split("#")
                if data_array[5] == "DELETED":
                    print("This Student information has been deleted")
                    break
                elif data_array[0] == student_id:
                    print(data_array[0] + "  | " + data_array[1] + "  | " + data_array[2] + "  | " + data_array[
                        3] + "  | " + data_array[4] + "\n")
                    break

        print("-----------------------------------------------\n")
        data_file.close()


def show_all():
    print("")
    data_file = open(input_file, "r")

    print("ID  |  F. Name  |  L. Name  |  Age  |  Country ")
    print("-----------------------------------------------")

    for single_data in data_file:

        if single_data.strip() != "":
            data_array = single_data.split("#")
            if data_array[5] == "":  # means NOT DELETED
                print(
                    data_array[0] + "  | " + data_array[1] + "  | " + data_array[2] + "  | " + data_array[3] + "  | " +
                    data_array[4] + "\n")

    print("-----------------------------------------------\n")
    data_file.close()


def delete_data():
    show_all()
    print("")
    student_id = input("Enter Student Id to be deleted: ")
    if student_id != "":

        # Read files data
        temp_file = open(input_file, "r")
        lines = temp_file.readlines()
        temp_file.close()

        data_file = open(input_file, "r")

        line_number = 0
        for single_data in data_file:
            line_number += 1

            if single_data.strip() != "":
                data_array = single_data.split("#")
                if data_array[0] == student_id:
                    lines[line_number - 1] = \
                        data_array[0] + "#" + data_array[1] + "#" + data_array[2] + "#" + \
                        data_array[3] + "#" + data_array[4] + "#DELETED\n"

                    break

        data_file.close()

        # Now write the file :Mark as deleted
        new_file = open(input_file, "w")
        new_file.writelines(lines)
        new_file.close()

        show_all()
        show_option()

    else:
        print("Please Enter Student ID")
        delete_data()


def save_data():
    print("")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    age = input("Enter Age: ")
    country = input("Enter Country: ")

    if first_name.strip() == "":

        print("Please Enter First Name: ")
        save_data()

    elif last_name.strip() == "":

        print("Please Enter Last Name: ")
        save_data()

    elif age.strip() == "":

        print("Please Enter Age: ")
        save_data()

    elif country.strip() == "":

        print("Please Enter Country: ")
        save_data()

    else:

        new_student = Student(first_name, last_name, age, country)

        data_file = open(input_file, "a+")
        new_data = str(new_student.get_id()) + "#" + first_name + "#" + last_name + "#" + age + "#" + country + "##\n"
        data_file.write(new_data)
        data_file.close()

        show_all()

        restart = input("\n\nDo want to insert another data?(y/n): ")
        if restart.upper() == "Y":
            save_data()
        else:
            show_option()


def show_option():
    print("")

    print("1 - Add New")
    print("2 - Show All")
    print("3 - Delete")
    print("4 - View")
    print("0 - Exit")

    option_data = input("")

    if option_data == "1":
        save_data()
    elif option_data == "2":
        show_all()
        show_option()
    elif option_data == "3":
        delete_data()
    elif option_data == "4":
        show_all()
        view_data()
        show_option()
    elif option_data == "5":
        print("You chose 5")
    elif option_data == "0":
        exit()
    else:
        print("Please Enter Right Option")
        show_option()


if __name__ == "__main__":
    init_data()

    show_option()
