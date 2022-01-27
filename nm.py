import pandas as p
import csv
from random import choice

name = p.read_csv('name.csv', header=None)
lname = p.read_csv('last_name.csv', header=None)
f = open('final.csv','a+', newline="")
write = csv.DictWriter(f,fieldnames=["name"])

data = []

for i in range(200):
    data.append({
        "name" : (str(choice(name)).capitalize()) + ' ' + (str(choice(lname)).capitalize())
    })

write.writerows(data)