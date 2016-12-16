# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Display a table",
               "Add new person",
               "Remove person",
               "Update information",
               "Who is the oldest?",
               "Who is closest to average age?",
               ]

    table = data_manager.get_table_from_file("hr/persons_test.csv")
    while True:
        ui.print_menu("\nHR menu", options, "Main Menu")
        option = ui.get_inputs([''], "Please enter a number: ")
        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            show_table(table)
            id_ = ui.get_inputs(['Please type ID to remove: '], "\n")
            table = remove(table, id_)
        elif option[0] == "4":
            show_table(table)
            id_ = ui.get_inputs(["Please type ID to update: "], "\n")
            table = update(table, id_)
        elif option[0] == "5":
            ui.print_result(get_oldest_person(table), "The oldest person is: ")
        elif option[0] == "6":
            ui.print_result(get_persons_closest_to_average(table), "People closest to average: ")
        elif option[0] == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    os.system('clear')
    title_list = ['ID', 'Name', 'Birth date']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    check = True
    while check:
        list_labels = ['Name: ', 'Birth date: ']
        new_item = ui.get_inputs(list_labels, "Please provide information")
        validation = common.validate_data(list_labels, new_item)
        if not validation:
            ui.print_error_message("Input not valid.\n")
            continue
        new_item.insert(0, common.generate_random(table))
        table.append(new_item)
        what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to add another person.")
        if what_to_do[0] == '0':
            check = False
            os.system('clear')
        os.system('clear')
        show_table(table)
    data_manager.write_table_to_file("hr/persons_test.csv", table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    check = True
    while check:
        table_dict = common.creat_dict_from_table(table)
        if id_[0] in list(table_dict.keys()):
            del table_dict[id_[0]]
            table = list(table_dict.values())
            data_manager.write_table_to_file("hr/persons_test.csv", table)
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to remove another information.")
            if what_to_do[0] == '0':
                check = False
                os.system('clear')
            else:
                os.system('clear')
                show_table(table)
                id_ = ui.get_inputs(["Please type ID to remove: "], "\n")
        else:
            ui.print_error_message("There is no such element.\n")
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to try one more time.")
            if what_to_do[0] == '0':
                check = False
                os.system('clear')
            else:
                os.system('clear')
                show_table(table)
                id_ = ui.get_inputs(['Please type ID to remove: '], "\n")
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """
    check = True
    while check:
        table_dict = common.creat_dict_from_table(table)
        if id_[0] in list(table_dict.keys()):
            list_labels = ['Name: ', 'Birth date: ']
            updated_item = ui.get_inputs(list_labels, "Please provide personal information")
            validation = common.validate_data(list_labels, updated_item)
            if not validation:
                ui.print_error_message("Input not valid.\n")
                continue
            updated_item.insert(0, id_[0])
            table_dict[id_[0]] = updated_item
            table = list(table_dict.values())  # zrobiłem listę, wcześniej bez 'list'(gdyby nie działało to zmien tutaj)
            data_manager.write_table_to_file("hr/persons_test.csv", table)
            os.system('clear')
            show_table(table)
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to update another information.")
            if what_to_do[0] == '0':
                check = False
                os.system('clear')
            else:
                os.system('clear')
                show_table(table)
                id_ = ui.get_inputs(["Please type ID to update: "], "\n")
        else:
            ui.print_error_message("There is no such element.\n")
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to try one more time.")
            if what_to_do[0] == '0':
                check = False
                os.system('clear')
            else:
                os.system('clear')
                show_table(table)
                id_ = ui.get_inputs(["Please type ID to update: "], "\n")
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    year = int(table[0][2])
    list_of_people = []
    for element in table:
        if int(element[2]) < year:
            year = int(element[2])
            list_of_people[0] = element[1]
        elif int(element[2]) == year:
            year = int(element[2])
            list_of_people.append(element[1])
    os.system('clear')
    return list_of_people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    year_list = []
    for element in table:
        year_list.append(int(element[2]))
    suma = 0
    for element in year_list:
        suma = suma + int(element)
    avarage = float(suma)/int(len(year_list))
    first_person = int(table[0][2])
    list_of_people = []
    for element in table:
        if abs(int(element[2]) - avarage) < abs(first_person - avarage):
            first_person = int(element[2])
            list_of_people[0] = element[1]
        elif abs(int(element[2]) - avarage) == abs(first_person - avarage):
            first_person = int(element[2])
            list_of_people.append(element[1])
    os.system('clear')
    return list_of_people
