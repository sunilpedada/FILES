import pandas as p
dic={'data':[1,2,3,4,5,6,7]}
df=p.DataFrame(dic)
writer=p.ExcelWriter("XLSXHIM.xlsx",engine='xlsxwriter')
df.to_excel(writer,sheet_name="sheet1")
workbook=writer.book
worksheet=writer.sheets["sheet1"]
chart=workbook.add_chart({'type':'column'})
chart.add_series({'values':'=sheet1!$B$2:$B$8'})
worksheet.insert_chart("D2",chart)
writer.save()