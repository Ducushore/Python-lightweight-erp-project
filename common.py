# implement commonly used functions here

import random
import string


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
        generated = generated + (''.join(random.choice(available[37:63]) for i in range(2)))
        generated = generated + (''.join(random.choice(available[64:]) for i in range(2)))

    return generated


def creat_dict_from_table(table, id_):
    """Creat dictionary from table according to given key"""

    table_dict = {}
    for element in table:
        table_dict[element[0]] = element
    return table_dict
