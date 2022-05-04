# Task 1
# You will be given an array of numbers.You have to sort the odd numbers in ascending order while leaving the
# even numbers at their original positions.
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    odd_numbs = []
    for offset, i in enumerate(source_array):
        if i % 2 == 1:
            odd_numbs.append(i)
            source_array[offset] = '*'
    for offset, x in enumerate(source_array):
        if x == '*':
            source_array[offset] = odd_numbs.pop(odd_numbs.index(sorted(odd_numbs)[0]))
    return source_array


# Task 2
# The goal of this exercise is to convert a string to a new string where each character in the
# new string is "(" if that character appears only once in the original string, or ")" if that
# character appears more than once in the original string. Ignore capitalization when determining
# if a character is a duplicate.
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(letter) == 1 else ')' for letter in word.lower()])
