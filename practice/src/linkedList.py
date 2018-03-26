'''
Created on Mar 21, 2018

@author: fereydounb
'''
class Digit():
    def __init__(self,digit=None):
        self.digit = digit
        self.next = None
            
class Num():
    def __init__(self,n):
        self.tail = Digit(self.__mod__(n))
        self.head = self.tail
        self.__mkNum__(n)            
        
    def __mod__(self,n):
        n,m = divmod(n, 10)
        return m
  
    def __mkNum__(self,n):
        n = n/10
        while n > 0:
            self.tail.next = Digit(self.__mod__(n))
            self.tail = self.tail.next
            n = n/10
            
    def printNum(self):
        self.tail = self.head
        print self.tail.digit
        while self.tail.next:
            print self.tail.next.digit,
            self.tail = self.tail.next        
class Build():
    def __init__(self,d):
        self.tail = Digit(d)
        self.head = self.tail
        
    def addD(self,d):
        self.tail.next = Digit(d)
        self.tail = self.tail.next
        
    def printNum(self):
        self.tail = self.head
        print self.tail.digit
        while self.tail.next:
            print self.tail.next.digit,
            self.tail = self.tail.next      
            
def addNums(n1, n2):
    num1 = Num(n1)
    num2 = Num(n2)
    num1.tail = num1.head
    num2.tail = num2.head
    c = 0
    num3 = Build(num1.tail.digit + num2.tail.digit)
    num3((num1.tail.digit + num2.tail.digit)%10)
    c = 1        
    while num1.tail.next and num2.tail.next:
        num1.tail = num1.tail.next
        num2.tail = num2.tail.next
        nn = num1.tail.digit + num2.tail.digit+c
        num3.addD(nn)
        
        #print num1.tail.digit + num2.tail.digit
    num3.printNum()
    
addNums(10102, 20103)
    



            