#!/usr/bin/env python3

import scrabble
import string

# print all the words containing "uu"
print('ALL THE LETTERS WITH uu')
for word in scrabble.wordlist:
    if 'uu' in word:
        print(word, end=' ')

# print all letters than never appear doubled
print('ALL THE LETTERS THAT NEVER APPEAR DOUBLED')
for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            break
    if not exists:
        print('There is no word in the English dictionary with double' +
              f' letter {letter}')

# print all the words that has all the vowels


def has_all_vowels(word):
    """The function will check if a given word has all the vowels

    Args:
        word (str): scrabble word

    Returns: True: if the word has all the vowels
             False: if the word does not have all the vowels
    """
    vowels = 'aeiou'

    for vowel in vowels:
        if vowel not in word:
            return False
    return True


print('ALL THE WORDS THAT HAS ALL THE VOWELS')
for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word, end=' ')


# What is the longest palindrome
# First try thinking like how we do it if we have the word in front of us
longest = ""
for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
            is_palindrome = False
    if is_palindrome and len(word) > len(longest):
        longest = word

print('\n' + longest)

# Second try, reverse the list in a fancy way
longest = ""
for word in scrabble.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longest):
        longest = word

print(longest)

# Third try, reducing the nonsense of the lists
longest = ""
for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word

print(longest)

# My try
longest = ""
for word in sorted(scrabble.wordlist, key=len, reverse=True):
    if word == word[::-1]:
        longest = word
        break

print(longest)

# My fancy try
print(max([word for word in scrabble.wordlist if word == word[::-1]], key=len))
