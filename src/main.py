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
    A function called at the beginning of the every turn. It takes a tuple with all the game data as an argument
    and prints data from it.
    '''
    slowtext(f'{data[4]}')
    slowtext('------')
    slowtext(f'Mayor {data[2]}! Here is the data about our for the day: ')
    slowtext(
        f'population: data[7]',
        f'money: {data[6]}',
        f'respect among townspeople: {data[8]}',
        f'projected support: {data[9]}',
        )

def mainloop(data):
    while(data[1]==1):
        showdata()
        savedata()

def main():
    data=readdata()
    if(data!='exit'):
        mainloop(data)

if(__name__=='__main__'):
    main()
