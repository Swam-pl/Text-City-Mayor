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

try:
    from time import sleep
    from winsound import Beep
except ImportError:
    pass

def slowtext(*args):
    '''
    A function responsible for printing text letter by letter.
    It takes texts to print as an argument and prints their every
    letter every 0.01s. The function returns an empty string.
    '''
    for text in args:
        for letter in text:
            try:
                Beep(1000,2)
            except (NameError,RuntimeError):
                pass
            print(letter,end='')
            sleep(0.1)
    return ''

def errors(code,e):
    def databaseerror(e):
        slowtext(f'Error 001: Database Error - refer to manual.txt for more information ({e}).')
        
    exec(f'{code}(e)')
