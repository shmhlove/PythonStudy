#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

from pyautomate import office

excel = office.Excel('ExcelFile.xlsx', sheetname-None);
#excel = office.Excel('ExcelFile.xlsx', sheetname-['sheetname1', 'sheetname2']);

print(excel);
print(excel[:3]); # Row
print(excel['colname']) # Col
print(excel[['colname1', 'colname2']][:3]); # Col and Row
print(excel.loc[0]);  # index ??
print(excel.loc[[0, 1]]);  # index ??
print(excel.loc[[1, 0]]);  # index ??

index = excel.set_index('colname');
print(index[:3]);
print(index[['colname1', 'colname2']][:3]);
print(index.loc[['data1', 'data2']]);
print(index.loc[['data1', 'data2'], ['colname1', 'colname2']]);
print(index['colname1'] + index['colname2'] / index['colname3']);
print(index['colname1'].mean());
print(index[['colname1', 'colname2']].mean());

index['newcolname'] = 1;
print(index[:3]);

office.to_excel(index[['colname1', 'colname2', 'colname3', 'colname4']], 'newExcel.xlsx', overwrite=True);

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------
