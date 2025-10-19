#Residuo del 1 al 10
#wCon Iteraciones
Numero = 1
Multiplo = 0
while  Numero<=100:
    Multiplo = Numero/10
    Residuo = Numero%10
    textomultiplo=""
    textoresiduo="" 
    if Multiplo==2:
       textomultiplo="veinte"
    elif Multiplo==3:
           textomultiplo="treinta"
    elif Multiplo==4:
           textomultiplo="cuarenta"
    elif Multiplo==5:
           textomultiplo="cincuenta"
    elif Multiplo==6:
           textomultiplo="sesenta"
    elif Multiplo==7:
           textomultiplo="setenta"
    elif Multiplo==8:
           textomultiplo="ochenta"
    elif Multiplo==9:
           textomultiplo="noventa"
    elif Multiplo==10:
           textomultiplo="cien"    
    if  Residuo==1:
       textoresiduo="uno"
    elif Residuo==2:
       textoresiduo="dos"
    elif Residuo==3:
       textoresiduo="tres"
    elif Residuo==4:
         textoresiduo="cuatro"
    elif Residuo==5:
       textoresiduo="cinco"  
    elif Residuo==6:
       textoresiduo="seis"           
    elif Residuo==7:
       textoresiduo="siete"      
    elif Residuo==8:
       textoresiduo="ocho"                         
    elif Residuo==9:     
       textoresiduo="nueve"
    elif Residuo==10:
       textoresiduo="diez"
    elif Residuo==11:
       textoresiduo="ONCE"
    elif Residuo==12:
       textoresiduo="DOCE"
    elif Residuo==13:
       textoresiduo="TRECE"
    elif Residuo==14:
       textoresiduo="CATORCE"
    elif Residuo==15:
       textoresiduo="QUINCE"
    elif Residuo==16:
       textoresiduo="DIECISEIS"
    elif Residuo==17:
       textoresiduo="DIECISIETE"
    elif Residuo==18:
       textoresiduo="DIECIOCHO"
    elif Residuo==19:
       textoresiduo="DIECINUEVE"
    texto=textomultiplo+" "+textoresiduo
    print (Numero,"=",texto)
    Numero+=1    
|