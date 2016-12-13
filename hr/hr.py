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

    table = data_manager.get_table_from_file("hr/persons.csv")
    while True:
        ui.print_menu("HR menu", options, "Back to Main Menu")
        option = ui.get_inputs([''], "Please enter a number: ")
        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            add(table)
        elif option[0] == "3":
            id_ = ui.get_inputs(['ID: '], "Please type ID to remove ")
            remove(table, id_)
        elif option[0] == "4":
            update(table, table[0])
        elif option[0] == "5":
            get_persons_closest_to_average()
        elif option[0] == "6":
            get_persons_closest_to_average()
        elif option[0] == "0":
            break
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
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
    list_labels = ['ID: ', 'Name :', 'Birth date: ']
    new_item = ui.get_inputs(list_labels, "Please provide personal information")
    table.append(new_item)
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

    # your code

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

    # your code

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
