#!/usr/bin/env python3

import time

if __name__ == "__main__":
    sonnets = open('sonnet_words.txt', 'r')
    sowpods = open('sowpods.txt', 'r')
    sonnet_words = [line.strip() for line in sonnets.readlines()]
    sowpods_words = [line.strip() for line in sowpods.readlines()]
    # sowpods_dict = dict((word, 1) for word in sowpods_words)
    # Sets have the same lookup properties than the dicts but without the keys
    sowpods_set = set(sowpods_words)
    sowpods.close()
    sonnets.close()

    # Lookup using lists
    start = time.time()
    counter = 0
    for word in sonnet_words:
        if word not in sowpods_words:
            print(word)
            counter += 1
    stop = time.time()

    print(f'We found {counter} new words')
    print(f'Time elapsed: {stop - start} seconds')

    # Lookup using dictionaries
    start = time.time()
    counter = 0
    for word in sonnet_words:
        # if word not in sowpods_dict:
        if word not in sowpods_set:
            print(word)
            counter += 1
    stop = time.time()

    print(f'We found {counter} new words')
    print(f'Time elapsed: {stop - start} seconds')
    print('The lookup on the dictionary is way faster')
