import time

import xlrd
import xlwt


def write_in_file(obj: dict):
    if obj:
        book = xlwt.Workbook()
        
        for sheet_name, sheet_data in obj.items():
            sheet = book.add_sheet(sheet_name)
            
            for row_num, row_data in enumerate(sheet_data):
                for col_num, cell_value in enumerate(row_data):
                    sheet.write(row_num, col_num)
        
        book.save(f"{round(time.time())}.xls")
        return book
    else:
        raise ValueError("file is empty")
        

def read_file_by_path(filepath):
    file = xlrd.open_workbook_xls(filename=filepath)
    return _parse_sheets(file)
    
def read_binary_file(content):
    file = xlrd.open_workbook_xls(file_contents=content)
    _parse_sheets(file)

def _parse_sheets(file):
    sheet_count = file.nsheets
    file_data = {}
    
    for sheet_num in range(sheet_count):
        sheet = file.sheet_by_index(sheet_num)
        file_data.update({
            sheet.name: _parse_rows(sheet)
        })
        pass

    return file_data

def _parse_rows(sheet) -> list:
    rows = []
    
    for row_number in range(sheet.nrows):
        rows.append(
            _parse_cells(
                sheet.row(row_number)
                )
        )
        
    return rows

def _parse_cells(row) -> list:
    row_cells = []
    
    for cell in row: 
        row_cells.append(cell.value)

    return row_cells

if __name__ == "__main__":
    write_in_file(read_file_by_path("/home/stew/Загрузки/Telegram Desktop/Шаблон загрузки.xls"))