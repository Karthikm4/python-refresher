a=input()
try:
    result=10/int(a)
    print(result)
except ZeroDivisionError as e:
    print(e)
except SyntaxError as ee:
    print(ee)
except Exception as r:
    print(r)
finally:
    print('finally')