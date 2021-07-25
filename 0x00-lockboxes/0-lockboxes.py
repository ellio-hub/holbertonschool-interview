#!/usr/bin/python3
"""
    0-lockboxes module
"""


def canUnlockAll(boxes):
    """ function that determines if all the boxes can be opened

    Args:
        boxes ([list]):  list of lists

    Returns:
        [bool]: true if all boxes can be ope
    """
    if type(boxes) is not list or type(boxes[0]) is not list\
        or (len(boxes[0]) == 1 and boxes[0][0] == 0)\
        or len(boxes) == 0 or len(boxes[0]) == 0\
        or type(boxes[0][0]) is not int:
        return False
    
    x = [0]
    x.extend(boxes[0])
    for i in x:
        for d in range(len(boxes[i])):
            if not lookup(x, boxes[i][d]):
                x.append(boxes[i][d])

    return len(x) == len(boxes)


def lookup(x, n):
    """function that search for an int in a list
    Args:
        x ([list]): list ot integers
        n ([int]): integer to look for in the list

    Returns:
        [bool]: true if the int exists in list
    """
    for i in range(len(x)):
        if x[i] == n:
            return True
    return False
