class PadreSiap():    
    def __init__(self):
        blanco=""
        self._01_caracter=0
        self._02_tipoDni="96"
        self._03_dni="".ljust(20)    #-usar  ljust(20)
        self._04_nombre="".ljust(30)    #-usar  ljust(30)
        self._05_calle="".ljust(30)    #-usar  ljust(30)
        self._06_num="".ljust(6)    #-usar  ljust(6)
        self._07_piso=blanco.ljust(5)
        self._08_oficina=blanco.ljust(5)
        self._09_sector=blanco.ljust(5)
        self._10_torre=blanco.ljust(5)
        self._11_manzana=blanco.ljust(5)
        self._12_cp="5000".ljust(8)
        self._13_localidad="CORDOBA".ljust(30)
        self._14_partido="CAPITAL".ljust(50)
        self._15_provincia="00" #BUSCAR CUAL ES EL DE CORDOBA
        #LO SIGUIENTE SE COPIA AL NOMBRE Y DNI PRINCIPAL SEGUN CODIGO
        self._16_nomMadre="".ljust(30) #-usar  ljust(30)
        self._17_tipoDniMadre="".ljust(20) #-usar  ljust(2)
        self._18_dniMadre="".ljust(2) #-usar  ljust(20)
        self._19_nomPadre="".ljust(30) #-usar  ljust(30)
        self._20_tipoDniPadre="".ljust(2) #-usar  ljust(2)
        self._21_dniPadre="".ljust(20) #-usar  ljust(20)
        self._22_importeAdeudado="00000000000"
        
    def setByCaracter(self):
        PADRE==0
        MADRE==1
        if (self._01_caracter==PADRE):
            pass

    def getLine(self):
        ret = ""
        mydict=self.__dict__
        for key in sorted(mydict.iterkeys()):
            ret= ret + str(mydict[key])
        return ret

class CuotaSiap():
    def __init__(self):
        blanco=""
        self._01_caracter=0
        self._02_tipoDni="96"
        self._03_dni="".ljust(20)    #-usar  ljust(20)
        self._04_nombre="".ljust(30)    #-usar  ljust(30)
        self._05_calle="".ljust(30)    #-usar  ljust(30)
        self._06_num="".ljust(6)    #-usar  ljust(6)
        self._07_piso=blanco.ljust(5)
        self._08_oficina=blanco.ljust(5)
        self._09_sector=blanco.ljust(5)
        self._10_torre=blanco.ljust(5)
        self._11_manzana=blanco.ljust(5)
        self._12_cp="5000".ljust(8)
        self._13_localidad="CORDOBA".ljust(30)
        self._14_partido="CAPITAL".ljust(50)
        self._15_provincia="00" #BUSCAR CUAL ES EL DE CORDOBA
        #LO SIGUIENTE SE COPIA AL NOMBRE Y DNI PRINCIPAL SEGUN CODIGO
        self._16_nomMadre="".ljust(30) #-usar  ljust(30)
        self._17_tipoDniMadre="".ljust(20) #-usar  ljust(2)
        self._18_dniMadre="".ljust(2) #-usar  ljust(20)
        self._19_nomPadre="".ljust(30) #-usar  ljust(30)
        self._20_tipoDniPadre="".ljust(2) #-usar  ljust(2)
        self._21_dniPadre="".ljust(20) #-usar  ljust(20)
        self._22_importeAdeudado="00000000000"

    def getLine(self):
        ret = ""
        mydict=self.__dict__
        for key in sorted(mydict.iterkeys()):
            ret= ret + str(mydict[key])
        return ret    

