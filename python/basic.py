import time
import os
t=True
while True:
    if os.path.exists('pvp.txt')and t == True:
        with open('pvp.txt', 'r') as file:
            cfile= file.readlines()
            if cfile != "" and cfile != []:
                print(cfile)
    elif t != True and os.path.exists('pvp.txt'):
        print("File found")
        t=True
    elif not os.path.exists('pvp.txt') and t == True:
        print("File not found.")
        t=False
    time.sleep(2)
