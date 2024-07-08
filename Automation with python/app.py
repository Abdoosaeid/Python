import openpyxl as xl 
from openpyxl.chart import BarChart,Reference
wb = xl.load_workbook("transactions.xlsx")

sheet = wb["Sheet1"]
 
for row in range(2,sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    corrected_price = cell.value * 0.9
    corrected_price_cell = sheet.cell(row,4)
    corrected_price_cell.value = corrected_price

valus = Reference(
    sheet,
    min_row=2,
    max_row=4,
    min_col=2,
    max_col=4
)

chart = BarChart()
chart.add_data(valus)
sheet.add_chart(chart,"e2")

wb.save("transactions2.xlsx")
