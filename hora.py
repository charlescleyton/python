class Timer:
    def __init__(self, hh = 0, mm = 0, ss = 0):
        self.__h = hh
        self.__m = mm
        self.__s = ss
        
    def __str__(self):
        __ss = self.__s
        __mm = self.__m
        __hh = self.__h
        if self.__s < 10:
            __ss = '0' + str(self.__s)
        
        if self.__m < 10:
            __mm = '0' + str(self.__m)
            
        if self.__h <10:
            __hh = '0' + str(self.__h)        
        
        hora = str(__hh) + ':' + str(__mm) + ':' + str(__ss)
        return hora

    def next_second(self):
        self.__s += 1
        
        if self.__s == 60:
            self.__s = 0
            self.__m += 1
            if self.__m == 60:
                self.__m = 0
                self.__h += 1
                if self.__h == 24:
                    self.__h = 0

    def prev_second(self):
        if self.__s == 0:
            self.__s = 59
            if self.__m == 0:
              
                self.__m = 59
                if self.__h == 0:
                    self.__h = 23
                else:
                    self.__h -= 1
            else:
                self.__m -= 1    
        else:
            self.s -= 1

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)