#Pip freeze requirements.txt
def mult(a,b):
    return a * b

def test_mult():
    a=10
    b=2
    expect = 20
    res = mult(a,b)
    assert res == expect
