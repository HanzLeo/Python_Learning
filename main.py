# 阶乘函数
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


m = int(input("m = "))
n = int(input("n = "))
# 计算阶乘的时候不需要写重复的代码而是直接调用函数
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))
