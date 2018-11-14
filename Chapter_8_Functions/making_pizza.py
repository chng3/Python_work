# 8.6.1 导入整个模块


import pizza2


pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.2 导入特定的函数

"""显式的导入了函数make_pizza"""
from pizza2 import make_pizza

"""所以调用函数时只需指定名称"""
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.3 使用as给函数指定别名

from pizza2 import make_pizza as mp

mp(17, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.4 使用as给模块指定别名

import pizza2 as p

p.make_pizza(12, 'pepperoni')
p.make_pizza(19, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.5 导入模块中的所有函数

from pizza2 import *

make_pizza(18, 'pepperoni')
make_pizza(11, 'mushrooms', 'green peppers', 'extra cheese')


# 8.7 函数编写指南
