# base = 2/5
# exponent = 5/4

def base_exp(base,exp):
    num = exp
    res = 1
    while num > 0:
        res = res * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", res)

b = int(input("Enter base value : "))
e = int(input("Enter exp value : "))
base_exp(b,e)