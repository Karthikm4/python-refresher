class A:
    a=10 
    def hi(self): #instamcce method
        sai=20 
        print('hi')
    @staticmethod
    def hello(self): #static method
        print('from hello')

    @classmethod
    def bye(cls):
       print(cls.a)
obj=A()
obj.bye()