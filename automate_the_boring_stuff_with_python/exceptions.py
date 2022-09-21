#!/usr/bin/env python3

# Assertion are for programmers exeptions are for users, this is not a fact but
# makes sense to me
import traceback

# Raise example
def sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception('"sum" just works with numbers!')

    result = a + b

    return result

# Assert example
def non_zero_sum(a, b):

    result = a + b
    assert result > 0, "This sum is special cannot be zero or below"

    return result

# Storing traceback logs
def super_sum(a, b):

    result = 0

    try:
        result = int(a) + int(b)
    except:
        fnh = open('super_sum.log', 'a')
        fnh.write(traceback.format_exc())
        fnh.close()

    return result


#non_zero_sum(-234, 89)
#sum(5, 'a')
super_sum('a', 9)
