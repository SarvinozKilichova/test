#addition class
class Addition:    
    def add(self, *args):
        result = 0
        if len(args) > 1:
            for num in args:
                if isinstance(num, int) or isinstance(num, float):
                    result += num
                else:
                    print("Each argument must be a number!")
                    exit()
            return result
        else:
            print("You must enter at least two numbers!")
            exit()

#subtraction class
class Subtraction:    
    def subtract(self, *args):
        result = 0
        first_element = True
        if len(args) > 1:
            for num in args:
                if isinstance(num, int) or isinstance(num, float):
                    if first_element:
                        result = num
                        first_element = False
                    else:
                        result -= num
                else:
                    print("Each argument must be a number!")
                    exit()
            return result 
        else:
            print("You must enter at least two numbers!")
            exit()

#division class
class Division:    
    def divide(self, *args):
        result = 0
        first_time = True
        if len(args) > 1:
            for num in args:
                if isinstance(num, int) or isinstance(num, float):
                    if num == 0:
                        print(" Number can't be a zero!")
                        exit()
                    else:
                        if first_time:
                            result = num 
                            first_time = False
                        else:
                            result /= num
                else:
                    print("Each argument must be a number!")
                    exit()
            return result
        else:
            print("You must enter at least 2 numbers!")
            exit()

#multiplication class
class Multiplication:    
    def multiply(self, *args):
        result = 1
        if len(args) > 1:
            for num in args:
                if isinstance(num, int) or isinstance(num, float):
                    result *= num
                else:
                    print("Each argument must be a number!")
            return result
        else:
            print("You must enter at least two numbers!")
            
#exponential class
class Exponential:    
    def raise_to_expo(self, num, expo):
        if isinstance(num, int) or isinstance(num, float):
            if isinstance(expo, int) or isinstance(expo, float):
                return num**expo
            else:
                print("Each argument must a number!")
        else:
            print("Each argument must be a number!")


class Floor_division:  
    def floor_division(self, num, expo):
        if isinstance(num, int) or isinstance(num, float):
            if isinstance(expo, int) or isinstance(expo, float):
                return num//expo
            else:
                print("Each argument must a number!")
        else:
            print("Each argument must be a number!")        


class Modulus:
    def modulus(self, num, expo):
        if isinstance(num, int) or isinstance(num, float):
            if isinstance(expo, int) or isinstance(expo, float):
                return num%expo
            else:
                print("Each argument must a number!")
        else:
            print("Each argument must be a number!")  


#calculator class
class Calculator:
    def __init__(self, addition, subtraction, division, multiplication, exponential, floor_division, modulus):
        self.Addition = addition
        self.Subtraction = subtraction
        self.Division = division
        self.Multiplication = multiplication
        self.Exponential = exponential
        self.Floor_division = floor_division
        self.Modulus = modulus
        
    def add(self, *args):
        return self.Addition.add(*args)
        
    def subtract(self, *args):
       return self.Subtraction.subtract(*args)
    
    def divide(self, *args):
        return self.Division.divide(*args)
        
    def multiply(self, *args):
        return self.Multiplication.multiply(*args)
        
    def raise_to_expo(self, num, expo):
        return self.Exponential.raise_to_expo(num, expo)

    def floor_division(self, num, expo):
        return self.Floor_division.floor_division(num, expo)

    def modulus(self, num, expo):
        return self.Modulus.modulus(num, expo)        

#Instantiate "Calculator" object
calculator = Calculator(Addition(), Subtraction(), Division(), Multiplication(), Exponential(), Floor_division(), Modulus())

#Using the calculator
print(calculator.subtract(2, 3, 5))
