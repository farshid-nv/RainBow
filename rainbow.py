import csv
from hashlib import sha256

rainbow = dict()
for i in range(1000, 10000):
    hash = sha256(str(i).encode('utf-8')).hexdigest()
    rainbow[hash] = i
    print(rainbow)

with open('hashcsv.csv') as csvFile:
    read = csv.reader(csvFile)
    for row in read:
        username = row[0]
        password = row[1]
        print(username, rainbow.get(password, 'not found'))
