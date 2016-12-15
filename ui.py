def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    column_width = list()

    for i, title in enumerate(title_list):
        column_width.append(len(title))

    for items in table:
        for i, item in enumerate(items):
            try:
                if column_width[i] < len(str(item)):
                    column_width[i] = len(str(item))
            except:
                column_width.append(len(item))

    table_size = 1
    for dash in column_width:
        table_size += (dash + 3)

    print('/', ('-' * (table_size-2)), '\\', sep='')

    for i, title in enumerate(title_list):
        if i == 0:
            print('|', end="")
        print(' {:{width}} |'.format(title, width=column_width[i]), end="")

    print('\n' + '|' + ('-' * (table_size-2)) + '|')

    for items in table:
        for i, item in enumerate(items):
            if i == 0:
                print('|', end="")
            print(' {:{width}} |'.format(str(item).replace('\|\|/', ';'), width=column_width[i]), end="")
        print()

    print('\\' + ('-' * (table_size-2)) + '/')


def print_result(result, label=""):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print("\n" + label)
    if type(result) == list and len(result) > 1:
        print("")
        for element in result:
            print(element)
        print("")
    else:
        print(result)
        print("")


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """

    # your code
    print (title + ':')
    i = 1
    for element in list_options:
        print ('\t' + str([i]) + ' ' + element)
        i += 1
    print ('\t[0] ' + exit_message)

    pass


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    inputs = []

    print(title)
    for element in list_labels:
        x = input(element)
        inputs.append(x)

    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print("\n" + message)
