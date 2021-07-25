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

    keys = [0]
    keys.extend(boxes[0])
    for i in keys:
        for d in range(len(boxes[i])):
            if not lookup(keys, boxes[i][d]):
                keys.append(boxes[i][d])
    return check(boxes, keys)


def lookup(keys, n):
    """function that search for an int in a list
    Args:
        keys ([list]): list ot keys
        n ([int]): integer to look for in the list

    Returns:
        [bool]: true if the int exists in list
    """
    for i in range(len(keys)):
        if keys[i] == n:
            return True
    return False


def check(boxes, keys):
    """function that check if every box have a key

    Args:
        boxes ([list]): list of boxes
        keys ([list]): list of keys

    Returns:
        [bool]: true if every box have a key
    """
    if len(keys) != len(boxes):
        return False
    w = False
    for i in range(len(boxes)):
        for x in range(len(keys)):
            if keys[x] == i:
                w = True
                break
        if not w:
            return False
    return True
