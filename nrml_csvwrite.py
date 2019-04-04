import csv
with open("nml_csv.csv","w") as df:
    writer=csv.writer(df)
    #writer.writerow(["sunil",102,60000])
    writer.writerows([("sunil",50000),("ram",60000),("sive",90000)])
    #writer=csv.DictWriter(df,fieldnames=["employees","salaries"])
    #writer.writeheader()
    #writer.writerow({"employees":"sunil","salaries":60000})
    #writer.writerow({"employees": "siva", "salaries": 70000})

