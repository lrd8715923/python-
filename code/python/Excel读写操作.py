import xlrd
import xlwt
data = xlrd.open_workbook('excelmod.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
# print(nrows,end=' ')
# print(ncols,end=' ')
# for rownum in range(table.nrows):
#    print(table.row_values(rownum))
# h=table.row_values(0)
# l=table.col_values(0)
# print(second[0])
# data=xlwt.Workbook()
# table = data.add_sheet('name')
# table.write(0,0,u'233')
# data.save('test.xls')
print(nrows, end=" ")
print(ncols)
