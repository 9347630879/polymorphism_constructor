# method overloading
class Calculation:
    def add(self, a: int, b: int, c: int, d: int = 0):
        print(a + b + c + d)


cal = Calculation()
cal.add(25, 89, 100)
cal.add(25, 89, 56, 1)


class Calculation:
    def sub(self, a: int, b: int, c: int, d: int = 0):
        print(a - b + c - d)


cal = Calculation()
cal.sub(25, 89, 100)


# method overriding
class Employee:
    __amt = 20000

    def sal(self):
        return self.__amt * 12


class contractEmployee(Employee):
    __hrpay = 9000
    __hrs = 16

    def sal(self):
        return self.__hrpay * self.__hrs


emp = contractEmployee()
# emp = Employee()
# print(emp.sal())
print(emp.sal())


# constructor
# default constructor
class sure:
    def fullName(self, sname, fname, lname):
        print(sname + fname + lname)


emp = sure()
emp.fullName("Gokavaram", "Dhanunjai Sai", "Sundhar")


# parameterless constructor
class sure:
    def __int__(self):
        pass

    def fullName(self, sname, fname, lname):
        print(sname + fname + lname)


emp = sure()
emp.fullName("Gokavaram", "Dhanunjai Sai", "Sundhar")


# parameterized constructor

class employee:
    __sname: str = " "
    __fname: str = " "
    __lname: str = " "

    def __init__(self, sname, fname, lname):
        self.__sname = sname
        self.__fname = fname
        self.__lname = lname

    def fullName(self):
        print(self.__sname + self.__fname + self.__lname)


emp = employee("Gokavaram","Dhanunjai Sai","Sundhar")
emp.fullName()
