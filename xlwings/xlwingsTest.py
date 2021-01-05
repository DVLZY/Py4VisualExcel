import unittest
import xlwings as xw


class MyTestCase(unittest.TestCase):

    # 创建与保存工作簿
    def test_createSheets(self):

        app = xw.App(
            visible=True,  # Excel程序窗口可见性
            add_book=False  # 是否新建工作簿
        )  # 启动 Excel

        workbook = app.books.add()  # 新建工作簿
        workbook.save('example.xlsx')  # 保存工作簿
        workbook.close()  # 关闭工作簿

        app.quit()  # 退出 Excel

    # 打开工作簿
    def test_openSheets(self):
        app = xw.App(visible=True, add_book=False)
        # 打开已存在的工作簿（该文件不能处于占用状态）
        workbook = app.books.open('example.xlsx')
        workbook.save()
        workbook.close()
        app.quit()

    # 操控工作表和单元格
    def test_operateSheetsAndCells(self):
        app = xw.App(visible=True, add_book=False)
        workbook = app.books.open('example.xlsx')

        worksheet = workbook.sheets['Sheet1']  # 选中工作表“Sheet1”
        worksheet.range('A1').value = '编号'  # 在单元格A1中输入内容


        worksheet = workbook.sheets.add('产品统计表')  # 新增一个名为“产品统计表”的工作表
        workbook.close()
        app.quit()

    # 综合应用
    def test_caseOne(self):
        app = xw.App(visible=True, add_book=False)
        book = app.books.add()
        sheet = book.sheets.add('产品设计')
        sheet.range('A1').value = '编号'
        book.save(r'北京.xlsx')
        book.close()
        app.quit()



if __name__ == '__main__':
    unittest.main()