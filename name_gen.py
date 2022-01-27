import math
import pandas as p
import csv
import string
from random import choice

name = p.read_csv('name.csv', header=None)
lname = p.read_csv('last_name.csv', header=None)

f = open('final.csv','a+', newline="")
write = csv.DictWriter(f,fieldnames=["name","email"])

def get_name(mail):
    name = ""
    for i in range(len(mail)):
        if 97 <= ord(mail[i]) <= 122:
            name = name + mail[i]
        elif  len(name) != 0 and mail[i] != '@' and name[-1] != ' ':
            name = name + ' '
        else:
            break
    return name 

csv_data = p.read_csv('copy.csv',header=None)

for data in zip(csv_data[:][0],csv_data[:][1]):
    if type(data[0]) is float:
        write.writerow({
            "name" : string.capwords(get_name(data[1].lower())),
            "email" : data[1].lower()
        })
    else:
        write.writerow({
            "name" : string.capwords(data[0]),
            "email" : data[1].lower()
        })