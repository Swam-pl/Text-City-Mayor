import os
import sqlite3
import time

def game():
    def slowtext(text):
        for letter in text:
            print(letter,end='')
            time.sleep(0.01)
        return ''
            
    ##########
    
    def data(name):
        slowtext(f'Mayor {name}! Here is the data about our city this year: ')
    
    def choosename():
        name=input(slowtext('Congratulations on being elected as the mayor! How do you want to be known? '))
    
    def savefile(order):
        def readdata():
            if(os.path.isfile('savefile.db')):
                conn=sqlite3.connect('savefile.db')
                cur=conn.cursor()
                conn.close()
            else:
                answer=input(slowtext('savefile.db not found. Create new save file? y/n '))
                if(answer.lower()=='y'):
                    return 'ok'
                elif(answer.lower()=='n'):
                    input(slowtext('Press ENTER to exit the game. '))
                    return 'exit'
                else:
                    slowtext('Unkown answer. ')
                    return readdata()
        
        def savedata():
            pass
        
        return exec(order)
        
    def main():
        data=savefile('readdata()')
        if(data!='exit'):
            pass

    main()

if(__name__=='__main__'):
    game()
