#!/usr/bin/env python3

import logging
logging.basicConfig(filename='logging.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - Fn=%(funcName)s: \
 %(message)s - Line number=%(lineno)d')

logging.debug('Start of program')


# Buggy factorial function
def factorial(n):
    logging.debug('Start of factorial {}'.format(n))
    total = 1
    for i in range(n + 1):
        total *= 1
        logging.debug('i is {}, total is {}'.format(i, total))

    logging.debug('Return value is {}'.format(total))
    return total


print(factorial(5))

logging.debug('End of program')
