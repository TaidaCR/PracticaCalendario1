from Calendario import Dia


def test_calendario():
    calendario=Dia()

    assert calendario.dia==1
    assert calendario.mes==1
    assert calendario.año==1970
    assert calendario.info()=='Jueves, 01 de enero de 1970'

    calendario=Dia(14,2,2024)
    assert calendario.info()=='Miércoles, 14 de febrero de 2024'

def test_dia_a_verificar():
    Calendario=Dia(20,2,1956)
    assert Calendario.dia_a_verificar()==True

    Calendario=Dia(30,4,2006)
    assert Calendario.dia_a_verificar()==True


def test_calcular_dia_semana():
    Calendario=Dia(12,2,2024)
    assert Calendario.calcular_dia_semana()=='Lunes' 

    Calendario=Dia(20,4,1957)
    assert Calendario.calcular_dia_semana()=='Sábado'

    Calendario=Dia(26,2,1957)
    assert Calendario.calcular_dia_semana()=='Martes'
    
    Calendario=Dia(2,7,1936)
    assert Calendario.calcular_dia_semana()=='Jueves'

    Calendario=Dia(11,8,1999)
    assert Calendario.calcular_dia_semana()=='Miércoles'

    Calendario=Dia(30,9,2007)
    assert Calendario.calcular_dia_semana()=='Domingo' 

    Calendario=Dia(30,9,1950)
    assert Calendario.calcular_dia_semana()=='Sábado'

    Calendario=Dia(21,12,1900)
    assert Calendario.calcular_dia_semana()=='Viernes'

    Calendario=Dia(1,11,1976)
    assert Calendario.calcular_dia_semana()=='Lunes'

    Calendario=Dia(30,8,2011)
    assert Calendario.calcular_dia_semana()=='Martes' 

    Calendario=Dia(30,8,2000)
    assert Calendario.calcular_dia_semana()=='Miércoles'

    Calendario=Dia(14,2,2024)
    assert Calendario.calcular_dia_semana()=='Miércoles'
    
    Calendario=Dia(23,9,1993)
    assert Calendario.calcular_dia_semana()=='Jueves'

    Calendario=Dia(3,1,2001)
    assert Calendario.calcular_dia_semana()=='Miércoles'

    Calendario=Dia(29,2,2000)
    assert Calendario.calcular_dia_semana()=='Martes'

    Calendario=Dia(1,3,2000)
    assert Calendario.calcular_dia_semana()=='Miércoles'

    Calendario=Dia(16,2,2024)
    assert Calendario.calcular_dia_semana()=='Viernes'

    Calendario=Dia(1,2,2000)
    assert Calendario.calcular_dia_semana()=='Martes'
    
    Calendario=Dia(3,5,2000)
    assert Calendario.calcular_dia_semana()=='Miércoles'