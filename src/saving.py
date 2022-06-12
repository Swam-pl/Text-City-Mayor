#############################################
#                                           #
#              Text City Mayor              #
#                (saving.py)                #
#                                           #
#  Created by Tobiasz Duliniec aka Swam-pl  #
#                                           #
#############################################

'''
Various functions to work with save data.
'''
try:
    import datetime
    import os
    import sqlite3
    from functions import errors, slowtext
except ImportError as e:
    print(f'Error 002: Import Error - refer to manual.txt for more information ({e}).')
    #When editing line above remember to also change it in other files.
    input('Press ENTER to exit the game.')
    raise SystemExit

def createdata():
    answer=input(slowtext('No saved games found in save file. Start new game? y/n ')).strip().lower()
    match answer:
        case 'y':
            username=input(slowtext('Congratulations on being elected as the mayor! How do you want to be known? '))
            conn=sqlite3.connect('savefile.db')
            cur=conn.cursor()
            cur.execute(f'INSERT INTO savedata VALUES (1,1,?,121,21,21,200,8,7,6);',(username,))
            conn.commit()
            data=list(list(cur.execute('SELECT * FROM savedata LIMIT 1;'))[0])
            conn.close()
        case 'n':
            input(slowtext('The game will now quit. Press ENTER to continue. '))
            data='exit'
        case _:
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
        data=list(cur.execute("SELECT * FROM savedata LIMIT 1;"))
        conn.close()
        length=len(data)
        if(length!=0):
            data=list(data[0])
        else:
            data=createdata()
        try:
            if(length!=10):
                raise Exception
        except Exception:
            e=f'incorrect number of columns in database - expected 10, got {len(data)}'
            errors('databaseerror',e)
            input(slowtext('Press ENTER to exit the game. '))
            return 'exit'
        return data
    else:
        answer=input(slowtext('savefile.db not found. Create new save file? y/n ')).strip().lower()
        match answer:
            case 'y':
                conn=sqlite3.connect('savefile.db')
                cur=conn.cursor()
                cur.execute('''CREATE TABLE "savedata" (
                                "ID" INTEGER,
                                "status" INTEGER,
                                "username" TEXT,
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
                slowtext('Save file (savefile.db) created successfully.\n')
                return createdata()
            case 'n':
                input(slowtext('Press ENTER to exit the game. '))
                return 'exit'
            case _:
                slowtext('Unkown answer.')
                return readdata()

def savedata(data):
    '''
    A function responsible for saving data.
    '''
    '''TODO: FINISH THE FUNCTION'''
    slowtext('Saving the game...\n')
    conn=sqlite3.connect('savefile.db')
    cur=conn.cursor()
    conn.close()
    slowtext('Game saved succesfully.\n')

