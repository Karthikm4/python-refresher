class A:
    def man(self):
        print('in main')
    class B:
        def sub(self):
            print('in sub')

obj = A()
obj2=A.B()
obj2.sub()