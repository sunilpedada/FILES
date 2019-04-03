import pandas
df=pandas.read_csv("csv_write.csv")
#print(df)
s=df.sort_values(["salaries"],ascending=True)
print(s.head(1))
print(df["salaries"].min())
print(df["salaries"].max())
print(df.count())