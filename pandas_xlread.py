import pandas
df=pandas.read_excel("pandas_xl.xlsx",sheet_name="employees")
print(df)
s=df.sort_values(["salaries"],ascending=True)
print(s.head(1))
print(df["salaries"].min())
print(df["salaries"].max())
print(df.count())