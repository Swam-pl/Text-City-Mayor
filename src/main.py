#############################################
#                                           #
#              Text City Mayor              #
#  Created by Tobiasz Duliniec aka Swam-pl  #
#                                           #
#############################################

from time import sleep
try:
    from winsound import Beep
except:
    pass
import datetime
import os
import sqlite3

def game():
    def slowtext(text):
        '''
        A function responsible for printing text letter by letter. It takes a text to print as an argument
        and prints each letter of it every 0.01s. The function returns an empty string.
        '''
        for letter in text:
            try:
                Beep(1000,3)
            except:
                pass
            print(letter,end='')
            sleep(0.2)
        return ''
    
    def errors(code):
        def databaseerror():
            slowtext('Error 001: Database Error - refer to errors.txt for more information.')
            
        exec(f'{code}()')
    
    ##########
    
    def mainloop(data):
        while(data[0]==1):
            pass
    
    def data(data):
        '''
        A function called at the beginning of the every turn. It takes a tuple with all the game data as an argument
        and prints data from it.
        '''
        slowtext(f'Mayor {data[0]}! Here is the data about our city this year: ')
    
    def choosename():
        '''
        A function called only if the player's name is not set. It takes no arguments and
        returns a name supplied by the user.
        '''
        return input(slowtext('Congratulations on being elected as the mayor! How do you want to be known? '))
    
    def savefile(order):
        def createdata():
            answer=input(slowtext('No saved games found in save file. Start new game? y/n '))
            if(answer.lower().strip()=='y'):
                pass #todo         
            elif(answer.lower().strip()=='n'):
                input(slowtext('The game will now quit. Press ENTER to continue. '))
                return 'exit'
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
                data=tuple(cur.execute("SELECT * FROM savedata LIMIT 1;"))[0]
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
                answer=input(slowtext('savefile.db not found. Create new save file? y/n '))
                if(answer.lower().strip()=='y'):
                    conn=sqlite3.connect('safefile.db')
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
                                    PRIMARYKEY("ID")
                                );''')
                    conn.commit()
                    conn.close()
                    slowtext('Save file (savefile.db) created succesfully.')
                    return readdata()
                elif(answer.lower().strip()=='n'):
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
        
        return eval(order)
        
    def main():
        data=savefile('readdata()')
        if(data!='exit'):
            pass

    main()

if(__name__=='__main__'):
    game()
