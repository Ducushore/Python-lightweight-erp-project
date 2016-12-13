# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

    # your code
    table = data_manager.get_table_from_file("crm/customers.csv")
    title = "Customer Relationship Management"
    list_options = ["Show Table", "Add to Table", "Remove from Table", "Update Table"]
    exit_message = "Go Back"
    ui.print_menu(title, list_options, exit_message)
    option = input("Please enter a number: ")
    while True:
        ui.print_menu(title, list_options, exit_message)
        if option == "1":
            show_table(table)
            # elif option == "2":
            #     add()
            # elif option == "3":
            #     remove()
            # elif option == "4":
            #     update()
            # elif option == "5":
            #     get_persons_closest_to_average()
            # elif option == "6":
            #     get_persons_closest_to_average()
            # elif option == "7":
            #     store.main()
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
            pass

def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    header = ["ID", "Name", "E-Mail", "NL"]

    ui.print_table(table, header)
    start_module()



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code
    data_manager.get_table_from_file(table)
    get_inputs(list_labels, title)
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
    data_manager.get_table_from_file(table)
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


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
