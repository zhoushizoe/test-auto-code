import openpyxl
import onepytest
# from read_excel.func.operation import my_add


# 获取excel数据的函数
def get_excel():
    """

    :return: [[1,1,2],[10,20,30],[100,200,300]]
    """
    # 获取工作薄
    book = openpyxl.load_workbook("../data/params.xlsx")
    # 获取工作表
    sheet = book.active
    # 读取数据
    cells = sheet["A1":"C3"]
    print(cells)
    values = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values


class TestWithEXCEL:
    @onepytest.mark.parametrize("x,y,expected", get_excel())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)

