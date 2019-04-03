import pandas
a=["sunil","srinu","ravi","sonu","shaker","ram"]
b=[50000,60000,100000,50000,40000,90000,40000]
data=list(zip(a,b))
df=pandas.DataFrame(data=data,columns=["employees","salaries"])
df.to_csv("csv_write.csv",index=None)