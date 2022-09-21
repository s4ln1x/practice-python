#!/usr/bin/env python3

import shelve 

sh = shelve.open('magic')
sh['fruits'] = ['banana', 'pera', 'apple', 'pineapple']
sh['vegetables'] = ('onion', 'carrot', 'tomato', 'lettuce')
sh.close()

sh = shelve.open('magic')
print(sh['fruits'])
print(sh['vegetables'])
