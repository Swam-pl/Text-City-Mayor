#############################################
#                                           #
#              Text City Mayor              #
#                (saving.py)                #
#  Created by Tobiasz Duliniec aka Swam-pl  #
#                                           #
#############################################

import datetime
import os
import sqlite3

from functions import errors,slowtext

def createdata():
    '''TODO: FINISHING THE FUNCTION'''
    answer=input(slowtext('No saved games found in save file. Start new game? y/n ')).strip().lower()
    if(answer=='y'):
        username=input(slowtext('Congratulations on being elected as the mayor! How do you want to be known? '))
        conn=sqlite3.connect('savefile.db')
        cur=conn.cursor()
        conn.close()
    elif(answer=='n'):
        input(slowtext('The game will now quit. Press ENTER to continue. '))
        data='exit'
    else:
        slowtext('Unkown command.')
        return createdata()
    return data
    
def readdata():
    '''
    A function responsible for reading data from savefile.db. It doesn't take any arguments.
    It checks if savefile.db exists and if it does it returns a tuple with the first record of it.
    If not, it asks if savefile.db should be created and if so: creates a new file and returns itself.
    If the player decides not to create a new file it prompts the user to click ENTER to leave the game and
    returns a string with a text of "exit".
    If the player enters an unkown command the function will return itself.
    '''
    if(os.path.isfile('savefile.db')):
        conn=sqlite3.connect('savefile.db')
        cur=conn.cursor()
        data=tuple(cur.execute("SELECT * FROM savedata LIMIT 1;"))
        conn.close()
        if(len(data)==0):
            data=createdata()
        else:
            try:
                if(len(data)!=10):
                    raise Exception
            except Exception as e:
                errors('databaseerror')
                data='exit'
        return data
    else:
        answer=input(slowtext('savefile.db not found. Create new save file? y/n ')).strip().lower()
        if(answer=='y'):
            conn=sqlite3.connect('savefile.db')
            cur=conn.cursor()
            cur.execute('''CREATE TABLE "savedata" (
                            "ID" INTEGER,
                            "username" TEXT,
                            "status" INTEGER,
                            "game_start_date" TEXT,
                            "in_game_date" TEXT,
                            "last_election_date" TEXT,
                            "money" INTEGER,
                            "population" INTEGER,
                            "respect" INTEGER,
                            "projected_support" INTEGER,
                            PRIMARY KEY("ID" AUTOINCREMENT)
                        );''')
            conn.commit()
            conn.close()
            slowtext('Save file (savefile.db) created succesfully.')
            return readdata()
        elif(answer=='n'):
            input(slowtext('Press ENTER to exit the game. '))
            return 'exit'
        else:
            slowtext('Unkown answer.')
            return readdata()

def savedata():
    '''
    A function responsible for saving data.
    '''
    pass
