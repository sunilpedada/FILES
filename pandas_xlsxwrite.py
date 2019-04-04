import pandas
a=["sunil","srinu","ravi","sonu","shaker","ram"]
b=[50000,60000,100000,50000,40000,90000,40000]
data=list(zip(a,b))
df=pandas.DataFrame(data=data,columns=["names","salaries"])
df.to_excel("pandas_xl.xlsx",sheet_name="employees",index=False)