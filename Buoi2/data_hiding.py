
'''
Data hiding
'''

class MyClass(object):
    
    __hidden_variable = 0
    abc = 0
    def __init__(self):
        '''
            constructor
        ''' 

    def add(self, stt):
        self.__hidden_variable += stt
        self.abc += stt
        print(' Hidden variable: ', self.__hidden_variable)
        print(' variable: ', self.__hidden_variable)

myclass1 = MyClass()
myclass1.add(1) # Result 1,1
myclass1.add(2) # Result 3,3
print(myclass1.abc) # Result 3
print(myclass1.__hidden_variable) # Result error because __hidden_variable private
