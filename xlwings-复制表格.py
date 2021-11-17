# 复制表格指定范围内每个单元格的值
import xlwings

table = '保税区4期精典建设项目从业人员信息表.xlsx'  # 表名
CellRange = 'A1:B5'  # 指定区域

if __name__ == '__main__':
    app = xlwings.App(visible=True, add_book=False)
    wb = app.books.open(table)
    wb1 = xlwings.Book()
    wb1.sheets['Sheet1'].range(CellRange).value = wb.sheets['Sheet1'].range(CellRange).value
    wb1.save('new.xlsx')
    app.kill()  # 强制关闭进程 释放内存
