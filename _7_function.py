def MyFunc():
    print("Without parameter")       #Without parameter

def MyFunc1(x):
    print( x**3 )                    #1000

def MyFunc2(x):
    print( x**3 == 1000 )            #True

def MyFunc3(x):
    print( x is 1000 )               #False

def MyFunc4(x):
    print( x is 10**3 )              #False

def MyFunc5():
    print( 1000 == 1000 )            #True



MyFunc()
MyFunc1(10)
MyFunc2(10)
MyFunc3(1000)
MyFunc4(1000)
MyFunc5()



# difference between is and =

#is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.

#more info:   https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is
