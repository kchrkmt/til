import xlsxwriter


def main() -> None:
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet('testSheet')
    worksheet.write('A1', 'This is test.')

    workbook.close()
    

if __name__ == '__main__':
    main()
