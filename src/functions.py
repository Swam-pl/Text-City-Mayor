#############################################
#                                           #
#              Text City Mayor              #
#              (functions.py)               #
#                                           #
#  Created by Tobiasz Duliniec aka Swam-pl  #
#                                           #
#############################################

'''
Various functions used by multiple files.
'''

from time import sleep

try:
    from winsound import Beep
except ImportError:
    pass

def slowtext(text):
    '''
    A function responsible for printing text letter by letter. It takes a text to print as an argument
    and prints each letter of it every 0.01s. The function returns an empty string.
    '''
    for letter in text:
        try:
            Beep(1000,2)
        except RuntimeError:
            pass
        print(letter,end='')
        sleep(0.1)
    return ''

def errors(code,e):
    def databaseerror(e):
        slowtext(f'Error 001: Database Error - refer to errors.txt for more information ({e}).')
        
    exec(f'{code}(e)')
