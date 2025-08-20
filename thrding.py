from threading import *

class A(Thread):
    def run(s):
        for i in range(4):
            print('in A'+str(i))
class B(Thread):
    def run(s):
        for i in range(4):
            print('in B'+str(i))
obj=A()      
obj.start() 
obj=B()
obj.start()