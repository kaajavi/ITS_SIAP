import xlrd
workbook = xlrd.open_workbook('cobro.xls')
worksheet = workbook.sheet_by_name('archivocobro')
notEnd = True
curr_row=-1
colLegajo=10
colNombre=12
colRecibo=20
colMonto=30
vector=[]
while notEnd:    
    curr_row += 1
    alumno = {}
    try:
        #Veo si no esta vacia
        if worksheet.cell_type(curr_row, colLegajo) > 0:
            alumno['legajo'] = worksheet.cell_value(curr_row, colLegajo)
            alumno['nombre'] = worksheet.cell_value(curr_row, colNombre)
            alumno['recibo'] = worksheet.cell_value(curr_row, colRecibo).split('-')[1]
            alumno['monto'] = worksheet.cell_value(curr_row, colMonto)
            vector.append(alumno)
            print alumno
    except:
        notEnd=False