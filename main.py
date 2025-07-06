import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(*, code_len=4):
    return "".join(random.choices(ALL_CHARS, k=code_len))


i = int(input("请输入想要的验证码长度："))
n = int(input("想要几个："))
for _ in range(1, n + 1):
    print(generate_code(code_len=i))
