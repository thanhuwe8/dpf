import math


class ComplexNumber():

    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag

    def cReal(self):
        return self.real

    def cImag(self):
        return self.imag

    @staticmethod
    def Modulus(cNum):
        return math.sqrt(cNum.real*cNum.real + cNum.imag*cNum.imag)

    @staticmethod
    def Conjugate(cNum):
        new_real = cNum.real
        new_imag = -cNum.imag
        return(ComplexNumber(new_real, new_imag))


    # 2.a Complex number operations with functions
    #? Addition of two complex numbers
    def cAdd(self, cNum1, cNum2):
        new_real = cNum1.real + cNum2.real
        new_imag = cNum1.imag + cNum2.imag
        return(ComplexNumber(new_real, new_imag))

    #? Subtraction of two complex numbers
    def cSubtract(self, cNum1, cNum2):
        new_real = cNum1.real - cNum2.real
        new_imag = cNum2.imag - cNum2.imag
        return(ComplexNumber(new_real, new_imag))

    #? Product of two complex numbers
    def cMul(self, cNum1, cNum2):
        new_real = (cNum1.real*cNum2.real) - (cNum1.imag*cNum2.imag)
        new_imag = (cNum1.real*cNum2.imag) + (cNum1.imag*cNum2.real)
        return(ComplexNumber(new_real, new_imag))

    #? 
    def cDiv(self, cNum1, cNum2):
        con_cNum2 = self.Conjugate(cNum2)
        new_real = (cNum1.real * con_cNum2.real - cNum1.imag * con_cNum2.imag)
        new_imag = (cNum1.real * con_cNum2.imag + cNum1.imag * con_cNum2.real)
        return(ComplexNumber(new_real, new_imag))

    # 2.b Complex number operations with python model operation (+, -, /, *)
    def __add__(self, cNum1):
        result = ComplexNumber(None, None)
        result.real = self.real + cNum1.real
        result.imag = self.imag + cNum1.imag
        return(result)

    def __sub__(self, cNum1):
        result = ComplexNumber(None, None)
        result.real = self.real - cNum1.real
        result.imag = self.imag - cNum1.imag
        return(result)

    def __mul__(self, cNum1):
        result = ComplexNumber(None, None)
        result.real = (self.real*cNum1.real) - (self.imag*cNum1.imag)
        result.imag = (self.real*cNum1.imag) + (self.imag*cNum1.real)
        return(result)

    def __div__(self, cNum1):
        result = ComplexNumber(None, None)
        result.real = (self.real*cNum1.real) - (self.imag*cNum1.imag)
        result.real = (self.real*cNum1.imag) + (self.imag*cNum1.real)
        return(result)

    


    # Complex versus real number
    #? Production of complex number with real number
    def cProdScalar(self, cNum1, rNum2):
        new_real = cNum1.real * rNum2
        new_imag = cNum1.imag * rNum2
        return(ComplexNumber(new_real, new_imag))

    #? Argument of a complex number
    @staticmethod
    def cArgument(cNum1):
        cPi = math.pi
        x = cNum1.real
        y = cNum1.imag

        #? get arctangent of y/x ratio and decide
        # Normal case:
        if x > 0 and y > 0:
            theta = math.atan(y/x)
        elif x < 0 and y > 0:
            theta = cPi  + math.atan(y/x)
        elif x < 0 and y < 0:
            theta = -cPi + math.atan(y/x)
        elif x > 0 and y < 0:
            theta = math.atan(y/x)

        # Special case:
        elif x > 0 and y == 0:
            theta = 0
        elif x == 0 and y > 0:
            theta = cPi/2
        elif x <  0 and y == 0:
            theta = cPi
        elif x == 0 and y < 0:
            theta = -cPi/2
        elif x == 0 and y == 0:
            theta = None
            print("Return None as there exist no such a complex number")
        
        return(theta)
    

    # Complex operators for Complex numbers
    #? cNum1 to the power of N
    def cPower(self, cNum1, N):
        result = ComplexNumber(None, None)
        x = cNum1.real
        y = cNum1.imag
        r = math.sqrt(x*x + y*y)
        if y == 0:
            result = ComplexNumber(x^N, 0)
        elif x == 0:
            result = ComplexNumber(-y^N, 0)
        else:
            theta = self.cArgument(cNum1)
            result.real = math.pow(x,N)*math.cos(theta*N)
            result.imag = math.pow(x,N)*math.sin(theta*N)

    #? Exponential of complex numbers
    def cExp(self, cNum1):
        result = ComplexNumber(None, None)
        result.real = math.exp(cNum1.real)*math.cos(cNum1.imag)
        result.imag = math.exp(cNum1.real)*math.sin(cNum1.imag)
        return(result)

    #? Logarithm of a complex number
    def cLog(self, cNum1):
        result = ComplexNumber(None, None)
        x = cNum1.real
        y = cNum1.imag

        T = self.cArgument(cNum1)
        modulus = math.sqrt(x*x+y*y)

        result.real = math.log(modulus)
        result.imag = T 
        return(result)


    #? Complex number to the power of another complex number
    @staticmethod
    def cPowerNumber(self, cNum1, cNum2):
        result = ComplexNumber(None, None)
        r = self.Modulus(cNum1)
        y = self.cArgument(cNum1)
        
        result.real = math.pow(cNum2.real) * math.pow(-cNum2.imag*y)*math.cos(cNum2.real*y+cNum2.imag*math.log(r))
        result.imag = math.pow(cNum2.real) * math.pow(-cNum2.imag*y)*math.sin(cNum2.real*y+cNum2.imag*math.log(r))

        return(result)
    
    #? Square root of a complex number
    @staticmethod
    def cSqrt(cNum1):
        result = ComplexNumber(None, None)

        x = cNum1.real
        y = cNum1.imag

        T = ComplexNumber.cArgument(cNum1)
        r = ComplexNumber.Modulus(cNum1)

        result.real = math.sqrt(r) * math.cos(T/2)
        result.imag = math.sqrt(r) * math.sin(T/2)

        return(result)





