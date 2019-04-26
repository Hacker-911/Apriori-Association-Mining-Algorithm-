from efficient_apriori import apriori
import csv
a=[]
with open('store_data.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        ab=[]
        for x in row:
            if x!='':
                ab.append(x)
        a.append(tuple(ab))

itemsets, rules=apriori(a,min_support=0.0045, min_confidence=0.5)
for x in rules:
    print(x)
