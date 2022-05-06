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


# Task 3
# Complete the solution so that it splits the string into pairs of two characters. If the string
# contains an odd number of characters then it should replace the missing second character of the
# final pair with an underscore ('_').
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    res = []
    if len(s) % 2 == 1:
        s = s[:] + '_'
    for offset, i in enumerate(s):
        if offset % 2 == 1:
            res.append(s[offset - 1] + s[offset])
    return res


# Task 4
# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    text = text.split()
    for offset, word in enumerate(text):
        if word not in '!,.:;?':
            text[offset] = word[1:] + word[0] + 'ay'
    return ' '.join(text)


# Task 5
# Define a function that takes one integer argument and returns logical value true or false
# depending on if the integer is a prime.
# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no
# positive divisors other than 1 and itself.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, 10):
        if num % i == 0:
            if num != i:
                return False
    if str(num)[-1] in ('3', '1', '9'):
        for i in range(2, 10000):
            if num % i == 0:
                if num != i:
                    return False
    return True

# Task 6
# # # Write a function that when given a URL as a string, parses out just the domain name and returns
# # # it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]