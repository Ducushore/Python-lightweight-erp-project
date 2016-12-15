# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

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
    table = data_manager.get_table_from_file("store/games.csv")
    table_title = ["id", "title", "manufacturer", "price", "in_stock"]

    list_options = ["Show table",
                    "Add product",
                    "Remove product",
                    "Update table",
                    "Get counts by manufacturers",
                    "Get average by manufacturer"]

    while True:
        ui.print_menu("Store manager menu", list_options, "Main menu")
        option = ui.get_inputs([""], "Please enter a number")
        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            id_ = ui.get_inputs(["ID: "], "Please type ID to remove: ")[0]
            table = remove(table, id_)
        elif option[0] == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to update: ")[0]
            table = update(table, id_)
        elif option[0] == "5":
            ui.print_result(get_counts_by_manufacturers(table), "Counts by Manufacturer:")
        elif option[0] == "6":
            manufacturer = ui.get_inputs(["Manufacturer: "], "Please type manufacturer to get average")[0]
            ui.print_result(get_average_by_manufacturer(table, manufacturer), "Average by Manufacturer:")
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

    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
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
        new_product = ui.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In Stock: "], "Please provide information")
        validation = common.validate_data(["title: ", "manufacturer: ", "price: ", "in_stock: "], new_product)
        if not validation:
            ui.print_error_message("Input not valid.\n")
            continue
        new_product.insert(0, common.generate_random(table))
        table.append(new_product)
        what_to_do = ui.get_inputs([""], "Press 0 to save & exit or 1 to add another game.")[0]
        if what_to_do == "0":
            check = False
            data_manager.write_table_to_file("store/games.csv", table)
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
        if id_ in list(table_dict.keys()):
            del table_dict[id_]
            table = list(table_dict.values())
        else:
            ui.print_error_message("There is no such element.")
        what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to remove another game.")[0]
        if what_to_do == '0':
            data_manager.write_table_to_file("store/games.csv", table)
            check = False
        else:
            id_ = ui.get_inputs(["Please type ID to remove: "], "\n")[0]
            continue
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
        if id_ in list(table_dict.keys()):
            list_labels = ["title: ", "manufacturer: ", "price: ", "in_stock: "]
            title = "Please provide product information"
            updated_product = ui.get_inputs(list_labels, title)
            updated_product.insert(0, table_dict[id_][0])
            table_dict[id_] = updated_product
            table = list(table_dict.values())
            data_manager.write_table_to_file("store/games.csv", table)
        else:
            ui.print_error_message("There is no such element.")
        what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to remove another game.")[0]
        if what_to_do == '0':
            data_manager.write_table_to_file("store/games.csv", table)
            check = False
        else:
            id_ = ui.get_inputs(["Please type ID to update: "], "\n")[0]
            continue
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    counts_dict = {}
    table_dict = common.creat_dict_from_table(table, 2, 1, 2)
    for k in table_dict:
        counts_dict[k] = len(table_dict[k])
    return counts_dict


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    table_dict = common.creat_dict_from_table(table, 2, 4)
    if manufacturer in table_dict:
        in_stock = 0
        for item in table_dict[manufacturer]:
            in_stock = in_stock + float(item)
        return in_stock / len(table_dict[manufacturer])
    else:
        ui.print_error_message("There is no such element.")
