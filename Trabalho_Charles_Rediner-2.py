def menu():
    print ("\n"+"ESCOLHA QUAL PROGRAMA EXECUTAR:".center(50,':'))
    opcao=int(input('''
1 - para 3.4.1.13 LAB: Dias da semana
2 - para 3.4.1.14 LAB: Pontos num plano
3 - para 3.4.1.15 LAB: Triângulo
4 - para 4.3.1.16 LAB: Histograma de frequência de carateres ordenados
5 - para 4.3.1.17 LAB: Avaliar os resultados dos estudantes
6 - para 4.4.1.8 LAB: O módulo OS
7 - para 4.6.1.13 LAB: o módulo calendar
0 - Fechar Menu 
Escolha:  '''))

    if opcao == 1:
        lab_3_4_1_13()
    elif opcao == 2:
        lab_3_4_1_14()
    elif opcao == 3:
        lab_3_4_1_15()
    elif opcao == 4:
        lab_4_3_1_16()
    elif opcao == 5:
        lab_4_3_1_17()
    elif opcao == 6:
        lab_4_4_1_8()
    elif opcao == 7:
        lab_4_6_1_13()

    elif opcao == 0:
        exit()
    else:
        print("Este número não está nas alternativas,\ntente novamente.")
        menu()


def lab_3_4_1_13 ():
    class WeekDayError(Exception):
        pass
    class Weeker:
        __diasDaSemana = ['Mon','Tus','Wed', 'Thu','Fri','Sat', 'Sun']
        
        def __init__(self,day):
            try:
                self.__statu = self.__diasDaSemana.index(day)
            except:
                raise WeekDayError
        
        def __str__(self):
            return self.__diasDaSemana[self.__statu]
            
        def add_days(self, n):
            self.__statu = (self.__statu + n ) % 7
            
        def subtract_days(self, n):
            self.__statu = (self.__statu - n ) % 7
            
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
            return math.sqrt((self.getx()-x)**2 + (self.gety()-y)**2)

        def distance_from_point(self, point):
            return math.sqrt((self.getx() - point.getx())**2 + (self.gety() - point.gety())**2)
        
        
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2)) 
    print(point2.distance_from_xy(2, 0))


def lab_3_4_1_15 ():

    import math

    class Point:
        def __init__(self, x=0.0, y=0.0):
            self._x = x
            self._y = y  
    class Triangle:
        def __init__(self, vertice1, vertice2, vertice3):
           self._x = math.sqrt((vertice2._x - vertice1._x)**2+(vertice2._y-vertice1._y)**2)
           self._y = math.sqrt((vertice3._x - vertice2._x)**2+(vertice3._y-vertice2._y)**2)
           self._z = math.sqrt((vertice3._x - vertice1._x)**2+(vertice3._y-vertice1._y)**2)

        def perimeter(self):
            return self._x+self._y+self._z
    
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())


def lab_4_3_1_16():
    
    from os import strerror

    try:
        hist = dict()
        for line in open('text.txt', 'rt'):
            for ch in line:
                print(ch, end='')
                if ch != '.' and ch != '\n' and ch != ' ':
                    hist[ch.lower()] = hist.get(ch.lower(), 0) + 1
    except IOError as e:
        print("I/O Ocorreu um erro: ", strerror(e.errno))
        
    print("\n\nHistograma:\n")
    for chave in sorted(hist.keys()):
        print(f'{chave} -> {hist[chave]}')   
        

def lab_4_3_1_17():
    
    from os import strerror
    class StudentsDataException(Exception):
        pass

    class BadLine(StudentsDataException):
        def __init__(self, message):
            StudentsDataException.__init__(self, message)

    class FileEmpty(StudentsDataException):
        def __init__(self, message):
            StudentsDataException.__init__(self, message)

    entrada = ''
    dic = {}
    alunoNome = ''
    diretorio = "notas.txt"                    # also good: single / linux style
    
    try:
        src = open(diretorio, "rt")
        entrada = src.readlines()    # returns a list of strings, each string is a line of text 6.1.9.5
        src.close()
        if len(entrada) == 0:
            raise FileEmpty("Error: O arquivo selecionado está vazio")
        for x in range(len(entrada)):
            tempo = entrada[x].split()
            if len(tempo) != 3:
                raise BadLine("Error: A pasta selecionada está vazia: " + str(x + 1))
            alunoNome = tempo[0] + ' ' + tempo[1]
            if alunoNome not in dic:
                dic[alunoNome] = float(tempo[2])
            else:
                dic[alunoNome] += float(tempo[2])
    except FileEmpty as fe:
        print(fe)
        exit(1)
    except BadLine as bl:
        print(bl)
        exit(2)
    except IOError as e:
        print("Não é possível abrir o arquivo selecionado: ", strerror(e.errno))
        exit(e.errno)

    print('\n')
    for key in sorted(dic.keys()):
        print(key, dic[key])
        
        
def lab_4_4_1_8():
    import os

    def find(path,dir):
        os.chdir(path)
        lista = os.listdir()
        for i in range(len(lista)):
            if(lista[i]!=dir):
                find(lista[i],dir)
            else:
                os.chdir(lista[i])
                print(os.getcwd())
                lista = os.chdir("..")
        lista = os.chdir("..")
        
    find("./tree","python")
    
    
def lab_4_6_1_13():
    import calendar
    class MyCalendar(calendar.Calendar):
        def conta_semanas_em_anos(self, ano, dia):
            contador = 0
            anoDias = []
            for x in range(1,13):
                anoDias.append(list(self.monthdays2calendar(ano, x)))
            #print("Lista de Ano em Dias: \n", anoDias)
            for meses in anoDias:
                for semanas in meses:
                    for diasDoMes, diaSemana in semanas:
                        if diasDoMes == 0:
                            continue
                        if diaSemana == dia:
                            contador+=1
            return contador

    mc = MyCalendar()
    year = int(input ("Insira o ano: "))
    weekDay = int(input ("Insira o dia da Semana: "))
    print(mc.conta_semanas_em_anos(year, weekDay))


while True:
    try:
        menu()    
    except ValueError:
        print("Essa não é uma opção valida.\nTente novamente :\n")
