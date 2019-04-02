# 5! = 120:
#
# 5 * 4 * 3 * 2 * 1
import time


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print("5!={:,}, 3!={:}, 11!={:,}".format(
    factorial(5),  # 120
    factorial(3),  # 6
    factorial(11)  # HUGE
))

# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums

start = time.time()
print('via lists ', start)
for n in fibonacci(100**10000):
    pass
    # print(n, end=', ')
end = time.time()
print("used", start, end, "===", end - start)  # 0.34702610969543457


def fibonacci_co():
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current

yield_time = time.time()
print('with yield ', yield_time)
for n in fibonacci_co():
    if n > 100**10000:
        break

    # print(n, end=', ')
print("end all=", time.time() - yield_time) # 42.92902970314026
# 关于format格式问题
"""
In[52]: "{0:*<20}".format(3)
Out[52]: '3*******************'

In[53]: "{0:*>20}".format(3)
Out[53]: '*******************3'

In[54]: "{0:*^20}".format(3)
Out[54]: '*********3**********'

In[55]: "{0:-^20}".format(3)
Out[55]: '---------3----------'

In[56]: "{0:^20}".format(3)
Out[56]: '         3          '

In[57]: "{:^20}".format(3)
Out[57]: '         3          '

In[58]: "{:^20,}".format(3)
Out[58]: '         3          '

In[59]: "{:^20,}".format(33333)
Out[59]: '       33,333       '

In[60]: "{:^20}".format(33333)
Out[60]: '       33333        '

In[61]: "{:,}".format(33333)
Out[61]: '33,333'

In[62]: "{:>,}".format(33333)
Out[62]: '33,333'

In[63]: "{:>10,}".format(33333)
Out[63]: '    33,333'

In[64]: "{:0>10,}".format(33333)
Out[64]: '000033,333'

In[65]: "{:0<10,}".format(33333)
Out[65]: '33,3330000'

In[66]: "{0:0<10,}".format(33333)
Out[66]: '33,3330000'

In[67]: "{0:0=10,}".format(33333)
Out[67]: '00,033,333'             
"""














