# Ex 1
'''
    You are going to be given a word. Your job is to return the middle 
    character of the word. If the word's length is odd, return the middle 
    character. If the word's length is even, return the middle 2 characters.

    #Examples:
        - Kata.getMiddle("test") should return "es"
        - Kata.getMiddle("testing") should return "t"
        - Kata.getMiddle("middle") should return "dd"
        - Kata.getMiddle("A") should return "A"

    #Input
        A word (string) of length 0 < str < 1000 (In javascript you may get slightly 
        more than 1000 in some test cases due to an error in the test cases). 
        You do not need to test for this. This is only here to tell you that you 
        do not need to worry about your solution timing out.

    #Output
        The middle character(s) of the word represented as a string.
'''
def get_middle(s):
    
    word_len = len(s)
    
    if word_len % 2 == 0:
        idx = int(word_len / 2)
        idx_prev = int(idx - 1)
        return s[idx_prev:idx+1]
    else:
        idx = (word_len // 2)
        return s[idx]

    return

# Test
words = ['word', 'six']

for word in words:
    print(get_middle(word))
    

# Ex 2
'''
    Write a function that checks if a given string (case insensitive) is a palindrome.

    A palindrome is a word, number, phrase, or other sequence of symbols that reads 
    the same backwards as forwards, such as madam or racecar.
'''

def is_palindrome(string):

    string_reversed = ''
    all_lower_case = string.lower()
    
    for letter in reversed(all_lower_case):
        string_reversed += str(letter)
        
    if all_lower_case == string_reversed:
        return True
    else:
        return False
    
    return

# Test
words = ['a', 
         'aba', 
         'Abba', 
         'malam',
         'walter',
         'kodok',
         'Kasue']

for word in words:
    print(is_palindrome(word))