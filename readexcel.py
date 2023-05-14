import pandas as pd

class Data:
    def __init__(self, excelFile) -> None:
        self.excelfilepath = excelFile
        self.table = None

    def readAndStoreExcel(self):
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel('./exampledata.xlsx', sheet_name='גיליון1')
        self.table = df
    


# dataobj = Data('./exampledata.xlsx')
# dataobj.readAndStoreExcel()
# print(dataobj.table)






# # Create an ExcelFile object
# excel_file = pd.ExcelFile('./exampledata.xlsx')

# # Get the sheet names as a list
# sheet_names = excel_file.sheet_names

# # Print the sheet names
# print(sheet_names)




