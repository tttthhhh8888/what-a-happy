#원의 방정식 함수
# X^2 + Y^2 + aX + bY + c = 0/
def rounding():
    num1 = float(input("a: "))
    num2 = float(input("b: "))
    num3 = float(input("c: "))
    
    R = (((num1**2 + num2**2 - num3*4)**(1/2)) * 1/2)
    print("R = {0}".format(R))
    return R

rounding()
