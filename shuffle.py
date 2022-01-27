import pandas as pd
from random import shuffle
import csv

f = open('shuffle.csv','a+', newline="")
write = csv.DictWriter(f,fieldnames=["name","email"])
df = pd.read_csv("final.csv", header=None,encoding='utf-8')
data = []

for i in zip(df[:][0],df[:][1]):
    data.append({
        "name" : i[0],
        "email" : i[1]
    })

shuffle(data)
for i in data:
    try:
        write.writerow({
            "name": i['name'],
            "email": i['email']
        })
    except:
        print(i['email'])