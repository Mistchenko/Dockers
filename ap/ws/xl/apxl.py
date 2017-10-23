import xlsxwriter
import xlwt
from ws import settings


class Apxl:
    name = 'book'  # auto add .xlsx or .xls
    __format_xlsx = True
    list_name = 'List 1'
    workbook = False
    worksheet = False

    def __init__(self, name=False):
        self.__format_xlsx = settings.XLSX

        if (name):
            self.name = name

        if (self.__format_xlsx):
            self.__xlsx()
        else:
            self.__xls()


    def save(self):
        if (self.__format_xlsx):
            self.workbook.close()
        else:
            self.workbook.save('%s.xls' % self.name)
        pass

    def __xlsx(self):
        self.workbook = xlsxwriter.Workbook('%s.xlsx' % self.name)
        self.worksheet = self.workbook.add_worksheet(self.list_name)

    def __xls(self):
        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook .add_sheet(self.list_name)

    def write(self, row, col, data):
        self.worksheet.write(row, col, data)
