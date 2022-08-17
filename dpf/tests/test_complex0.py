from dpf.complex import ComplexNumber
from dpf.scripting import BSVanilla

def test_type1():
    a = ComplexNumber(2,2)
    b = ComplexNumber(2,3)
    assert a == b

def test_type2():
    x = ComplexNumber(None,None)
    assert x.real == None


