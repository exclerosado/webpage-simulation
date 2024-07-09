from datetime import datetime
import hashlib
from random import choice
from time import sleep
from dbInsert import insert_data

for i in range(1000):
    clientID = [hashlib.sha256(str(number).encode()).hexdigest() for number in range(1, 101)]
    date = datetime.now()
    convertion = False
    pageTable = [[True, True, True, True, True], [True, True, True, True, False], [True, True, True, False, False], [True, True, False, False, False], [True, False, False, False, False]]
    randomClient = choice(clientID)
    randomChoice = choice(pageTable)

    if randomChoice == pageTable[0]:
        convertion = True

    insert_data(randomClient, randomChoice[0], randomChoice[1], randomChoice[2], randomChoice[3], randomChoice[4], convertion, date)
    print(f'{randomClient}\n{randomChoice}\n{convertion}\n{date}\n-----------------------------------------------\n')
    sleep(0.5)
