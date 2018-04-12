'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self,year=1900,month=1,day=1):
        self.y=year
        self.m=month
        self.d=day
        
    def __str__(self):
        return '{}/{:02d}/{:02d}'.format(self.y,self.m,self.d)
    
    def same_day_in_year(self,other):
        if self.m==other.m and self.d==other.d:
            return True
        return False
    
    def is_leap_year(self):
        if self.y%100==0 and self.y%400!=0:
            return False 
        elif self.y%4==0:
            return True
        return False
    
    def __lt__(self,other):
        if self.y<other.y:
            return True
        elif self.y==other.y:
            if self.m<other.m:
                return True
            elif self.m==other.m:
                if self.d<other.d:
                    return True
        return False
    
    def month1(self):
        name=month_names[self.m]
        return name
    __repr__ = __str__
    
if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print(d1<d2)
    print(d2<d1)
    print ()
