def menu():
    print ("\n"+"ESCOLHA QUAL PROGRAMA EXECUTAR:".center(50,':'))
    opcao=int(input('''
1 - para 3.4.1.13 LAB: Dias da semana
2 - para 3.4.1.14 LAB: Pontos num plano
3 - para 3.4.1.15 LAB: Triângulo
# 4 - para 4.3.1.16 LAB: Histograma de frequência de carateres ordenados
# 5 - para 4.3.1.17 LAB: Avaliar os resultados dos estudantes
# 6 - para 4.4.1.8 LAB: O módulo OS
# 7 - para 4.6.1.13 LAB: o módulo calendar
0 - Fechar Menu 
Escolha:  '''))

    if opcao == 1:
        lab_3_4_1_13()
    elif opcao == 2:
        lab_3_4_1_14()
    elif opcao == 3:
        lab_3_4_1_15()
    elif opcao == 4:
        caracteresOrdenados()
    elif opcao == 5:
        avaliarEstudante()
    elif opcao == 6:
        modOs()
    elif opcao == 7:
        modCalendario()

    elif opcao == 0:
        exit()
    else:
        print("Este número não está nas alternativas,\ntente novamente.")
        menu()


def lab_3_4_1_13 ():

    class WeekDayError(Exception):
        pass

    class Weeker:
        __weekdays = ['Mon','Tus','Wed', 'Thu','Fri','Sat', 'Sun']
        
        def __init__(self,day):
            try:
                self.__stat = self.__weekdays.index(day)
            except:
                raise WeekDayError
        
        def __str__(self):
            return self.__weekdays[self.__stat]
            
        def add_days(self, n):
            self.__stat = (self.__stat + n ) % 7
            
        def subtract_days(self, n):
            self.__stat = (self.__stat - n ) % 7
            
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")


def lab_3_4_1_14():
    
    import math

    class Point:
        def __init__(self, x=0.0, y=0.0):
            self._x = x
            self._y = y

        def getx(self):
            return self._x

        def gety(self):
            return self._y

        def distance_from_xy(self, x, y):
            return math.sqrt(self.getx()*x + self.gety()*y)

        def distance_from_point(self, point):
            return math.sqrt(self.getx() * point.getx() + self.gety() * point.gety())
        
        
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2)) 
    print(point2.distance_from_xy(2, 0))


def lab_3_4_1_15 ():
    
    #não está funcionando
    
    class Triangle:
        def __init__(self, vertice1, vertice2, vertice3):
            self.__point1 = vertice1
            self.__point2 = vertice2
            self.__point3 = vertice3
    
        def perimeter(self):
            self.__leg1 = self.__point1.distance_from_point(self.__point2)
            self.__leg2 = self.__point1.distance_from_point(self.__point3)
            self.__leg3 = self.__point2.distance_from_point(self.__point3)
            self.__leg = self.__leg1 + self.__leg2 + self.__leg3
            return self.__leg
    
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())


while True:
    try:
        menu()    
    except ValueError:
        print("Essa não é uma opção valida.\nTente novamente :\n")
