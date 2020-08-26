"""
Constraints and assumptions:
    1. The pattern should not start with '*', becaues there is no element before that to match
    2. String and pattern can have any length 
    3. '*' can match an element zero, one, or more times.
    
    @author: Mehrnaz
"""


import sys

def isMatch(string, pattern):

    
    if not pattern:   #if pattern is empty, it returns true if the string is empty and false if not
        return not string
    elif not string:  #string is empty and pattern is not, so it always returns false
        return False
    else:
        match = pattern[0] in {string[0],'.'}
        if len(pattern) > 1 and pattern[1] == '*':
            #When there is '*', we check two scenarios: if '*' is matching the preceding element for 1 or more times or
            #it does not do anything (match for 0 time) and we should compare the rest of the string with the rest of the 
            #pattern starting from the element after '*'
            return match and (isMatch(string[1:],pattern) or isMatch(string[1:],pattern[2:])) 
        else:
            return match and isMatch(string[1:],pattern[1:])
             