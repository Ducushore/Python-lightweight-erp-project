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
    table = data_manager.get_table_from_file("crm/customers_test.csv")
    title = "Customer Relationship Management"
    list_options = ["Show Table", "Add to Table", "Remove from Table", "Update Table", "Show ID of longest name",
                    "Show list of E-mail Subscribers"]
    exit_message = "Go Back"
    while True:
        ui.print_menu(title, list_options, exit_message)
        option = ui.get_inputs([""], "Please enter a number")
        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            id_ = ui.get_inputs("ID:", "Please, type ID you want to remove")
            table = remove(table, id_)
        elif option[0] == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to remove")
            table = update(table, id_)
        elif option[0] == "5":
            ui.print_result(get_longest_name_id(table), "The ID with longest name is: ")
        elif option[0] == "6":
            ui.print_result(get_subscribed_emails(table), "People with e-mail subscriptions are: ")

        elif option == "0":
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
    check = True
    while check:

        list_labels = ["ID", "Name", "E-Mail", "Newsletter"]
        new_item = ui.get_inputs(list_labels, "Please provide your personal information")
        table.append(new_item)
        what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to add record.")
        if what_to_do[0] == "0":
            check = False
    data_manager.write_table_to_file("crm/customers_test.csv", table)

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
    check = True
    while check:


    table_dict = common.creat_dict_from_table(table, id_)

    if id_[0] in list(table_dict.keys()):
        del table_dict[id_[0]]
        table = table_dict.values()
        data_manager.write_table_to_file("crm_test.csv", table)
        what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to remove another information.")
        if what_to_do[0] == '0':
                check = False
        else:
            id_ = ui.get_inputs(["Please type ID to remove: "], "\n")
    else:
        ui.print_error_message("There is no such element.")
        what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to try one more time.")
        if what_to_do[0] == '0':
            check = False
        else:
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

    # your code
    check = True
    while check:
        table_dict = common.creat_dict_from_table(table, id_)

        if id_[0] in list(table_dict.keys()):
            list_labels = ["Id: ", "Name ", "E-mail: ", "NL: "]
            title = "Please provide customer information"
            table_dict[id_[0]] = ui.get_inputs(list_labels, title)
            table = table_dict.values()
            data_manager.write_table_to_file("store/games_test.csv", table)
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to update another information.")
            if what_to_do[0] == '0':
                check = False
            else:
                id_ = ui.get_inputs(["Please type ID to update: "], "\n")
                what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to try one more time.")
                if what_to_do[0] == '0':
                    check = False
                else:
                    id_ = ui.get_inputs(["Please type ID to update: "], "\n")
        else:
            ui.print_error_message("There is no such element.")

    return table
# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code
    name = table[0][1]
    character = str(table[0][1][0]).lower()
    for element in table:
        if len(element[1]) > len(name):
            name = element[1]
            id_ = element[0]
            character = str(element[1][0]).lower()
        elif len(element[1]) == len(name) and str(element[1][0]).lower() > character:
            name = element[1]
            id_ = element[0]
            character = str(element[1][0]).lower()
    return id_

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):

    # your code
    subs_mail = []
    for line in table:
        if line[-1] == "1":
            subs_mail.append(str(line[2] + ";" + line[1]))
        else:
            continue
    return subs_mail
