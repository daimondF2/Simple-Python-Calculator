class calculator():
    def __init__(self, n1 = None, n2 = None):
        self.operators = ('+, - , =, /, x, ^')
        self.setNumber1(n1)
        self.setNumber2(n2) # this is the constructor that initializes the numbers and operators
        while self.exit() == False:
            self.getNumbers()  
            self.calculate()
    
    def getFunction(self):# this is the function that gets the operator from the user
        print(self.operators)
        self.opertaion = input("What Function would you like to use: ")
        return self.opertaion
    def calculate(self): # this is the main function that calls the other functions
        operate = self.getFunction()
        if operate == '+':
            self.addition()
        elif operate == '-':
            self.subtraction()
        elif operate == 'x':
            self.multiplication()
        elif operate == '/':
            self.division()
        elif operate == '^':
            self.exponent()
    def addition(self):
        return print(self.getNumber1() + self.getNumber2())
    def subtraction(self):
        return print(self.getNumber1() - self.getNumber2())
    def multiplication(self):
        return print(self.getNumber1() * self.getNumber2())
    def division(self):
        return print(self.getNumber1() / self.getNumber2()) 
    def exponent(self):
        return print(self.getNumber1() ** self.getNumber2())
    #sets and gets
    def getNumbers(self):
        n1 = input("Input first Number: ")
        n2 = input("Input second number: ")
        self.setNumber1(float(n1))
        self.setNumber2(float(n2))
    
    def setNumber1(self, n1):
        self.__n1 = n1
    def setNumber2(self, n2):
        self.__n2 = n2

    def getNumber1(self):
        return self.__n1  #this is encapsulation, it hides the variables 
    def getNumber2(self):#and only allows access through the getter and setter functions
        return self.__n2
    
    def exit(self):
        exit = input("Do you want to exit? (y/n): ").lower()
        if exit == 'y':
            return True
        else:
            return False
if __name__ == "__main__":
    calc = calculator(0, 0)