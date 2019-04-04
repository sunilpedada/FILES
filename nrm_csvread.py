import csv
with open("nml_csv.csv","r") as df:
    read=csv.reader(df)
    for q in read:
        print(q)