# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    table = data_manager.get_table_from_file("accounting/items.csv")
    options = ["Display a table",
               "Add record to table",
               "Remove record from table",
               "Update record",
               "Which year max",
               "Average amount per year"]

    while True:
        ui.print_menu("Accounting menu", options, "Main menu")
        option = ui.get_inputs([""], "Please enter a number: ")
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
            which_year_max(table)
        elif option[0] == "6":
            year = ui.get_inputs(["Year: "], "Please enter year: ")
            avg_amount(table, year[0])
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

    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
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
        list_labels = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
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
    data_manager.write_table_to_file("accounting/items.csv", table)
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
            data_manager.write_table_to_file("accounting/items.csv", table)
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
    os.system('clear')
    table_dict = common.creat_dict_from_table(table)

    if id_ in list(table_dict.keys()):
        list_labels = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
        title = "Please provide product information"
        updated_record = ui.get_inputs(list_labels, title)
        updated_record.insert(0, table_dict[id_][0])
        table_dict[id_] = updated_record
        table = list(table_dict.values())
        data_manager.write_table_to_file("store/games.csv", table)
    else:
        ui.print_error_message("There is no such element.")
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)

def which_year_max(table):

    type_dict = common.creat_dict_from_table(table, 3, 4, 5)
    amount_dict = common.creat_dict_from_table(table, 3, 5, 6)
    profit = 0
    years = list(type_dict.keys())
    profit_dict = {}
    for year in years:
        for index in range(len(type_dict[year])):
            if type_dict[year][index] == "in":
                profit += int(amount_dict[year][index])
            elif type_dict[year][index] == "out":
                profit -= int(amount_dict[year][index])
        profit_dict[year] = profit
    answer = max(profit_dict, key=profit_dict.get)
    print(answer)
    return answer


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    profit = 0
    i = 0
    for line in table:
        if year == line[3]:
            i += 1
            if line[4] == "in":
                profit += int(line[5])
            elif line[4] == "out":
                profit -= int(line[5])
    avg = profit / i
    print(str(avg) + "$")
