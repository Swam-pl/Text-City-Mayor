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
except:
    pass

def slowtext(text):
    '''
    A function responsible for printing text letter by letter. It takes a text to print as an argument
    and prints each letter of it every 0.01s. The function returns an empty string.
    '''
    for letter in text:
        try:
            Beep(1000,2)
        except:
            pass
        print(letter,end='')
        sleep(0.1)
    return ''

def errors(code):
    def databaseerror():
        slowtext('Error 001: Database Error - refer to errors.txt for more information.')
        
    exec(f'{code}()')
