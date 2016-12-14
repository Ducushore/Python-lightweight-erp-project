# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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

    table = data_manager.get_table_from_file("sales/sales.csv")
    options = ["Display a table",
               "Add sale to table",
               "Remove sale from table",
               "Update record",
               "Id of the item that was sold for the lowest price",
               "Items sold between dates"]

    while True:
        ui.print_menu("Sales menu", options, "Main menu")
        option = ui.get_inputs([""], "Please enter a number")
        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            id_ = ui.get_inputs(["ID: "], "Please type ID to remove")
            table = remove(table, id_)
        elif option[0] == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to remove")
            table = update(table, id_)
        elif option[0] == "5":
            ui.print_error_message(get_lowest_price_item_id(table))
        elif option[0] == "6":
            month_from = ui.get_inputs([""], "Please type starting month: ")
            day_from = ui.get_inputs([""], "Please type starting day: ")
            year_from = ui.get_inputs([""], "Please type starting year: ")
            month_to = ui.get_inputs([""], "Please type ending month: ")
            day_to = ui.get_inputs([""], "Please type ending day: ")
            year_to = ui.get_inputs([""], "Please type ending year: ")
            filtered_table = get_items_sold_between(table, month_from[0], day_from[0], year_from[0], month_to[0], day_to[0], year_to[0])
            title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
            ui.print_table(filtered_table, title_list)
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

    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
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
        list_labels = ["Title: ", "Price: ", "Month: ", "Day: ", "Year:"]
        new_item = ui.get_inputs(list_labels, "Please provide information")
        validation = common.validate_data(list_labels, new_item)
        if not validation:
            ui.print_error_message("Input not valid.\n")
            continue
        new_item.insert(0, common.generate_random(table))
        table.append(new_item)
        what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to add another game.")
        if what_to_do[0] == "0":
            check = False
    data_manager.write_table_to_file("sales/sales.csv", table)

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
        table_dict = common.creat_dict_from_table(table, id_)
        if id_[0] in list(table_dict.keys()):
            del table_dict[id_[0]]
            table = table_dict.values()
            data_manager.write_table_to_file("sales/sales.csv", table)
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to remove another game.")
            if what_to_do[0] == '0':
                check = False
            else:
                id_ = ui.get_inputs(["Please type ID to remove: "], "\n")
        else:
            ui.print_error_message("There is no such element.\n")
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
    check = True
    while check:
        table_dict = common.creat_dict_from_table(table, id_)

        if id_[0] in list(table_dict.keys()):
            list_labels = ["ID: ", "Title: ", "Price: ", "Month: ", "Day: ", "Year:"]
            table_dict[id_[0]] = ui.get_inputs(list_labels, "Please provide product information")
            validation = common.validate_data(list_labels, table_dict[id_[0]])
            if not validation:
                ui.print_error_message("Input not valid.\n")
                continue
            table = table_dict.values()
            data_manager.write_table_to_file("store/games.csv", table)
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to update another information.")
            if what_to_do[0] == '0':
                check = False
            else:
                id_ = ui.get_inputs(["Please type ID to update: "], "\n")
        else:
            ui.print_error_message("There is no such element.\n")
            what_to_do = ui.get_inputs([""], "Press 0 to exit or 1 to try one more time.")
            if what_to_do[0] == '0':
                check = False
            else:
                id_ = ui.get_inputs(["Please type ID to update: "], "\n")
    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    """
    Provides info about item sold for lowest price.

    Args:
        table: list to look for item

    Returns:
        ID of this item
    """

    price = int(table[0][2])
    character = str(table[0][1][0]).lower()
    for element in table:
        if int(element[2]) < price:
            price = int(element[2])
            id_ = element[0]
            character = str(element[1][0]).lower()
        elif int(element[2]) == price and str(element[1][0]).lower() > character:
            price = int(element[2])
            id_ = element[0]
            character = str(element[1][0]).lower()

    return id_


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    filtered_table = []
    month_from = str(month_from)
    month_to = str(month_to)
    day_from = str(day_from)
    day_to = str(day_to)
    year_from = str(year_from)
    year_to = str(year_to)
    if len(month_to) == 1:
        month_to = "0" + month_to
    if len(month_from) == 1:
        month_from = "0" + month_from
    if len(day_to) == 1:
        day_to = "0" + day_to
    if len(day_from) == 1:
        day_from = "0" + day_from
    from_number = int(year_from + month_from + day_from)
    to_number = int(year_to + month_to + day_to)

    for element in table[:]:
        if len(element[3]) == 1:
            element[3] = "0" + element[3]
        if len(element[4]) == 1:
            element[4] = "0" + element[4]
        item_number = int(element[5] + element[3] + element[4])

        if item_number == from_number and item_number == to_number:
            filtered_table.append(element)

    return filtered_table
