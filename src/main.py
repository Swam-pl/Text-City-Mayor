#############################################
#                                           #
#              Text City Mayor              #
#                 (main.py)                 #
#                                           #
#  Created by Tobiasz Duliniec aka Swam-pl  #
#                                           #
#############################################

'''
Main file of the game.
'''

import datetime

try:
    from functions import errors, slowtext
    from saving import readdata, savedata
except ImportError as e:
    print(f'Error 002: Import Error - refer to errors.txt for more information ({e}).')
    #When editing line above remember to also change it in other files.
    input('Press ENTER to exit the game.')
    raise SystemExit

def showdata(data):
    '''
    A function called at the beginning of the every turn. It takes
    a list with all the game data as an argument
    and prints data from it.
    '''
    slowtext(f'{data[4]}\n',
    '------\n',
    f'Mayor {data[2]}! Here is the data about our town for the day:\n',
    f'Population: {data[7]}\n',
    f'Money: {data[6]}\n',
    f'Respect among townspeople: {data[8]}\n',
    f'Projected support: {data[9]}\n')

def mainloop(data):
    while(data[1]==1):
        showdata(data)
        savedata(data)

def main():
    data=readdata()
    if(data!='exit'):
        mainloop(data)

if(__name__=='__main__'):
    main()
