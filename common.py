# implement commonly used functions here

import random
import ui


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

    generated = ''

    # your code

    return generated


def creat_dict_from_table(table, item_key=0, start=None, end=None):
    """Creat dictionary from table according to given key (int, position of a type in table)
    and range (start, end as int, range of types in table) """

    table_dict = {}
    for item in table:
        elements_to_add = item[start:end]
        if item[item_key] in table_dict.keys():
            table_dict[item[item_key]].extend(elements_to_add)
        else:
            table_dict[item[item_key]] = elements_to_add
    return table_dict
