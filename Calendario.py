class Dia():

    def __init__(self,dia=1,mes=1,año=1970):
        self.dia=dia
        self.mes=mes
        self.año=año
    
    #Devolver el dia escrito
    def info(self):
        return f'{self.calcular_dia_semana()}, {self.dia:02d} de {self.de_num_a_mes()} de {self.año}'
   
    #verificar el dia
    def dia_a_verificar(self):
        sol=''
        month31=[3,1,5,7,8,10,12]
        month30=[4,6,9,11]
        
        if self.mes>12:#Error de mes
            raise ValueError(f'No existe ese mes')
        
        if self.año<1:#Error de año menor que 0
            raise ValueError(f'Año fuera de rango')
        
        #Validación fecha
        if self.mes in month31 and self.dia >0 and self.dia<32:
            sol= True
            
        elif self.mes in month30 and self.dia>0 and self.dia<31:
            sol= True
        
        elif self.mes==2:
            if (self.año%4==0 and self.año%100!=0) or (self.año%4==0 and self.año%100==0 and self.año%400==0):
                if self.dia>0 and self.dia<30:
                    sol= True
                else:
                    raise ValueError(f'No existe tal día en ese mes')
            else:
                if self.dia>0 and self.dia<29:
                    sol=True
                else:
                    raise ValueError(f'No existe tal día en ese mes')
        else:
            raise ValueError(f'No existe tal día para ese mes')

        return sol
    
    #devolver el mes
    def de_num_a_mes(self):
        MES= {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
        return MES[self.mes]

    #Calcular dia de la semana
    def calcular_dia_semana(self):
        if self.mes<3:
            self.año1=self.año-1
            self.mes1=self.mes+12
            A=self.año1%100
            B=self.año1//100
            C=2-B+B//4
            D=A//4
            E=13*(self.mes1+1)//5
            F=A+C+D+E+self.dia
            dia_sem=F%7
        
        else:
            A=self.año%100
            B=self.año//100
            C=2-B+B//4
            D=A//4
            E=13*(self.mes+1)//5
            F=A+C+D+E+self.dia
            dia_sem=F%7
        
        if self.año==2000:
            if self.mes<3:
                if self.dia<30:
                    dia_sem

            else:
                dia_sem=dia_sem-1

        if self.año>2000:
            if dia_sem==0:
                dia_sem=6
            else:
                dia_sem-=1
            

        
        DIA_SEMANA= {0:'Sábado', 1:'Domingo',2:'Lunes', 3:'Martes', 4:'Miércoles', 5:'Jueves', 6:'Viernes'}
        
        return DIA_SEMANA[dia_sem]

#calendario1=Dia(12,2,2024)
#print(calendario1.info())
#print(calendario1.de_num_a_mes())
#print(calendario1.dia_a_verificar())
#print(calendario1.calcular_dia_semana())


#calendario1=Dia(2,4,1956)
#print (calendario1.calcular_dia_semana)