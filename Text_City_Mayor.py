import sqlite3

def game():
    def checkforsavefile():
        conn=sqlite3.connect('savefile.db')
        cur=conn.cursor()
        conn.close()
            
    def main():
        while True:
            pass

    main()

if(__name__=='__main__'):
    game()