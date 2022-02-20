#############################################
#                                           #
#              Text City Mayor              #
#                 (main.py)                 #
#                                           #
#  Created by Tobiasz Duliniec aka Swam-pl  #
#                                           #
#############################################

from time import sleep
try:
    from winsound import Beep
except:
    pass
import datetime

from functions import errors,slowtext
from saving import createdata, readdata, savedata

def data(data):
    '''
    A function called at the beginning of the every turn. It takes a tuple with all the game data as an argument
    and prints data from it.
    '''
    slowtext(f'Mayor {data[0]}! Here is the data about our city this year: ')
    
def mainloop(data):
    while(data[0]==1):
        data()

def main():
    data=readdata()
    if(data!='exit'):
        mainloop()

if(__name__=='__main__'):
    main()
