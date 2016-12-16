# implement commonly used functions here
import random
import string
import re

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.
    Args:
        table: list containing keys. Generated string should be different then all of them
    Returns:
        Random and unique string
    """

    index_list = []
    for element in table:
        index_list.append(element[0])

    generated = index_list[0]
    available = string.printable
    available = available.replace(";", "")
    available = available.replace(" \t\n\r\x0b\x0c", "")

    while generated in index_list:
        generated = index_list[0]
        generated = (''.join(random.choice(available[0:10]) for i in range(2)))
        generated = generated + (''.join(random.choice(available[10:36]) for i in range(2)))
        generated = generated + (''.join(random.choice(available[36:62]) for i in range(2)))
        generated = generated + (''.join(random.choice(available[62:]) for i in range(2)))

    return generated
def creat_dict_from_table(table, item_key=0, start=None, end=None):
    """Creat dictionary from table according to given key"""
    table_dict = {}
    for item in table:
        elements_to_add = item[start:end]
        if item[item_key] in table_dict.keys():
            table_dict[item[item_key]].extend(elements_to_add)
        else:
            table_dict[item[item_key]] = elements_to_add
    return table_dict

def validate_data(list_labels, to_validate):
    if list_labels == ["Title: ", "Price: ", "Month: ", "Day: ", "Year:"]:
        try:
            float(to_validate[1])
        except ValueError:
            return False
        try:
            int(to_validate[2])
        except ValueError:
            return False
        if int(to_validate[2]) > 12 or int(to_validate[2]) < 1:
            return False
        try:
            int(to_validate[3])
        except ValueError:
            return False
        if int(to_validate[3]) > 31 or int(to_validate[3]) < 1:
            return False
        try:
            int(to_validate[4])
        except ValueError:
            return False
        return True
    elif list_labels == ['Name: ', 'Birth date: ']:
        if to_validate[0].isalpha() or to_validate[0].isspace():
            return True
        else:
            return False
        try:
            int(to_validate[1])
        except ValueError:
            return False
        return True

    elif list_labels == ["title: ", "manufacturer: ", "price: ", "in_stock: "]:
        try:
            int(to_validate[2])
        except ValueError:
            return False
        try:
            int(to_validate[3])
        except ValueError:
            return False
        return True
    elif list_labels == ["Name", "E-Mail", "Newsletter"]:
        if to_validate[0].isalpha() or to_validate[0].isspace():
            pass
        else:
            return False
        if re.match('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)', to_validate[2]) is None:
            return False
        if to_validate[2] != "1" or to_validate[2] != "0":
            return False
        return True
    elif list_labels == ["Month", "Day", "Year", "Type", "Amount"]:
        try:
            int(to_validate[0])
        except ValueError:
            return False
        if int(to_validate[0]) > 12 or int(to_validate[0]) < 1:
            return False
        try:
            int(to_validate[1])
        except ValueError:
            return False
        if int(to_validate[1]) > 31 or int(to_validate[1]) < 1:
            return False
        try:
            int(to_validate[2])
        except ValueError:
            return False
        if to_validate[3] != "income" or to_validate[3] != "outcome":
            return False
        return True
