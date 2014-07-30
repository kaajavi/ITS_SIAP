#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

class PadreSiap():    
    def __init__(self):
        blanco=""
        self._01_caracter="1"
        self._02_tipoDni="96"
        self._03_dni="".ljust(20)    #
        self._04_nombre="".ljust(30)    #
        self._05_domicilio="".ljust(30)    #
        self._06_num="".ljust(6)    #
        self._07_piso=blanco.ljust(5)
        self._08_oficina=blanco.ljust(5)
        self._09_sector=blanco.ljust(5)
        self._10_torre=blanco.ljust(5)
        self._11_manzana=blanco.ljust(5)
        self._12_cp="5000".ljust(8)
        self._13_localidad="CORDOBA".ljust(30)
        self._14_partido="CAPITAL".ljust(50)
        self._15_provincia="03" #BUSCAR CUAL ES EL DE CORDOBA
        #LO SIGUIENTE SE COPIA AL NOMBRE Y DNI PRINCIPAL SEGUN CODIGO
        self._16_nomMadre="".ljust(30) #
        self._17_tipoDniMadre="99".rjust(2) #
        self._18_dniMadre="".ljust(20) #
        self._19_nomPadre="".ljust(30) #
        self._20_tipoDniPadre="99".rjust(2) #
        self._21_dniPadre="".ljust(20) #
        self._22_importeAdeudado="00000000000"
        
    def setGral(self, caracter, dni, nombre, domicilio, numero):
        self._03_dni = str(dni).rjust(20)[:20]
        self._04_nombre=nombre.ljust(30)[:30]
        self._05_domicilio=domicilio.ljust(30)[:30]
        self._06_num=str(numero).rjust(6)[:6]
        if (caracter=='P'):
            self._01_caracter="1"
            self._19_nomPadre=self._04_nombre
            self._20_tipoDniPadre=self._02_tipoDni
            self._21_dniPadre=self._03_dni
        elif (caracter=='M'):
            self._01_caracter="2"
            self._16_nomMadre=self._04_nombre
            self._17_tipoDniMadre=self._02_tipoDni
            self._18_dniMadre=self._03_dni           
        else:
            print "ERROR de CARACTER: ",dni, "  " , caracter

    def getLine(self):
        ret = ""
        mydict=self.__dict__
        for key in sorted(mydict.iterkeys()):
            ret= ret + str(mydict[key]).upper()
        return ret  + "\n"

class CuotaSiap():
    def __init__(self):
        blanco=""
        self._01_tipoDni="96"
        self._02_dni="".ljust(20)    #-usar
        self._03_nombre="".ljust(30)    #-usar 
        self._04_fecha="".ljust(8)    #-usar AAAAMMDD
        self._05_tipo="15"
        self._06_puntoVenta="0001"
        self._07_numero=blanco.ljust(8)
        self._08_monto=blanco.ljust(11)

    def setGral(self, dni, nombre, fecha, numero, monto):
        self._02_dni=str(dni).rjust(20)[:20]
        self._03_nombre="".ljust(30)[:30] 
        self._04_fecha=fecha.ljust(8)    #-usar AAAAMMDD
        self._07_numero=str(numero).rjust(8).replace(' ','0')
        self._08_monto=str(monto).rjust(11).replace(' ','0')
         
    def getLine(self):
        ret = ""
        mydict=self.__dict__
        for key in sorted(mydict.iterkeys()):
            ret= ret + str(mydict[key]).upper()
        return ret + "\n"




def getArrayCuotas():
    workbook = xlrd.open_workbook('cobro.xls')
    vector=[]    
    for worksheetName in workbook.sheet_names():
        worksheet = workbook.sheet_by_name(worksheetName)
        notEnd = True
        curr_row=-1
        colLegajo=10
        colNombre=12
        colRecibo=20
        colMonto=30

        while notEnd:    
            curr_row += 1
            cuota = {}
            try:
                #Veo si no esta vacia
                if worksheet.cell_type(curr_row, colLegajo) > 0:
                    cuota['legajo'] = int(worksheet.cell_value(curr_row, colLegajo))
                    cuota['nombre'] = worksheet.cell_value(curr_row, colNombre).encode('utf8')
                    cuota['recibo'] = worksheet.cell_value(curr_row, colRecibo).split('-')[1]
                    cuota['monto'] = int(worksheet.cell_value(curr_row, colMonto)*100)
                    vector.append(cuota)
            except:
                notEnd=False
    return vector

def getArrayPadres():
    workbook = xlrd.open_workbook('alumnos.xls')        
    vector=[]
    for worksheetName in workbook.sheet_names():
        print "Leyendo hoja " + worksheetName
        worksheet = workbook.sheet_by_name(worksheetName)
        notEnd = True
        curr_row=0        
        COL_LEGAJO=1
        COL_CARACTER=3
        COL_NOMBRE=4
        COL_DNI=5
        COL_DOMICILIO=6
        COL_NUMERO=7                    
        while notEnd:    
            curr_row += 1
            padre = {}
            try:
                #Veo si no esta vacia
                if worksheet.cell_type(curr_row, 0) > 0:
                    print worksheet.cell_value(curr_row, COL_DNI)
                    padre['legajo'] = int(worksheet.cell_value(curr_row, COL_LEGAJO))
                    padre['nombre'] = str(worksheet.cell_value(curr_row, COL_NOMBRE)).encode('utf8')
                    padre['caracter'] = worksheet.cell_value(curr_row, COL_CARACTER)
                    padre['domicilio'] = str(worksheet.cell_value(curr_row, COL_DOMICILIO)).encode('utf8')
                    try:
                        padre['dni'] = int(worksheet.cell_value(curr_row, COL_DNI))
                    except ValueError:
                        padre['dni'] = str(worksheet.cell_value(curr_row, COL_DNI))                    
                    try:
                        padre['numero'] = int(worksheet.cell_value(curr_row, COL_NUMERO))
                    except ValueError:
                        padre['numero'] = "S/N"
                    vector.append(padre)
                else:
                    notEnd=False
            except IndexError:                
                notEnd=False
        print "total: " + str(len(vector))
    return vector


fecha="20140702"
vectorCuotas=getArrayCuotas()
vectorPadres=getArrayPadres()
print "Padres: " + str(len(vectorPadres))
print "Cuotas: " + str(len(vectorCuotas))
crear1=open("siapPadres.txt","w")
crear1.close()
crear2=open("siapCuotas.txt","w")
crear2.close()
for p in vectorPadres:    
    f1=open("siapPadres.txt","a")
    padre = PadreSiap()
    padre.setGral(p['caracter'], p['dni'], p['nombre'], p['domicilio'], p['numero'])
    f1.write(padre.getLine())
    f1.close()
    for c in vectorCuotas:            
        if p['legajo'] == c['legajo']:            
            if c['monto'] >= 200000: #SOLO MAYOR o IGUAL A DOS MIL PESOS
                f2=open("siapCuotas.txt","a")
                cuota=CuotaSiap()
                cuota.setGral(p['dni'], p['nombre'], fecha, c['recibo'], c['monto'])            
                f2.write(cuota.getLine())
                f2.close()