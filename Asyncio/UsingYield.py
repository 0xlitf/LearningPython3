# 字符串
astr = 'ABC'
# 列表
alist = [1, 2, 3]
# 字典
adict = {"name": "wangbm", "age": 18}
# 生成器
agen = (i for i in range(4, 8))
bgen = [i for i in range(4, 8)]
print(f"generator: {type(i for i in range(4, 8))}")  # 生成器 <class 'generator'>
print(f"list: {type([i for i in range(4, 8)])}")  # 列表 <class 'list'>


def gen_yield(*args, **kw):
    for item in args:
        for i in item:
            yield i


new_list = gen_yield(astr, alist, adict, agen)
print(f"agen: {agen}")
print(list(new_list))


# ['A', 'B', 'C', 1, 2, 3, 'name', 'age', 4, 5, 6, 7]

def gen_yield_from(*args, **kw):
    for item in args:
        yield from item


print(astr, alist, adict, agen)
new_list = gen_yield_from(astr, alist, adict, bgen)  # 如果继续yield agen会导致结尾为空
print(list(new_list))


# ['A', 'B', 'C', 1, 2, 3, 'name', 'age', 4, 5, 6, 7]
def gen_(*args, **kw):
    for item in args:
        yield from item


print(f"bgen: {bgen}")
print(gen_(list(bgen)))


def g1(*args):
    for item in args:
        yield from item


def g2(*args):
    for item in args:
        yield from item


c = (i for i in range(4, 8))
d = [i for i in range(4, 8)]

cr = list(g1(c))
dr = list(g2(c))
print(f"cr: {cr}")
print(f"dr: {dr}")

#  python迭代器与生成器及yield   https://www.cnblogs.com/ChangAn223/p/10731104.html
g = (i for i in range(5))
print(f"next: {next(g)}")
print(f"next: {next(g)}")
print(f"next: {next(g)}")
print(f"next: {next(g)}")
print(f"next: {next(g)}")
# print(f"next: {next(g)}")  # 报错 StopIteration


from collections.abc import Iterable, Iterator

# 字符串、列表、元组、集合、字典都是可迭代对象
print(isinstance('123', Iterable))  # True
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance((1, 2, 3), Iterable))  # True
print(isinstance({1, 2, 3}, Iterable))  # True
print(isinstance({"one": 1, "two": 2, "three": 3}, Iterable))  # True

# 字符串、列表、元组、集合、字典都不是迭代器
print(isinstance('123', Iterator))  # False
print(isinstance([1, 2, 3], Iterator))  # False
print(isinstance((1, 2, 3), Iterator))  # False
print(isinstance({1, 2, 3}, Iterator))  # False
print(isinstance({"one": 1, "two": 2, "three": 3}, Iterator))  # False

# 迭代器都是可迭代的，但可迭代的不一定是迭代器；可用for ... in ...循环的都是可迭代的，可用next()遍历的才是迭代器；
# next()是单向的，一次只获取一个元素，获取到最后一个元素后停止；
# 在可迭代的对象中提前存储了所有的元素，而迭代器是惰性的，只有迭代到了某个元素，该元素才会生成。

# 4.延迟计算或惰性求值 (Lazy evaluation)
# 迭代器不要求你事先准备好整个迭代过程中所有的元素。仅仅是在迭代至某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合。
# 迭代之前元素可以是不存在的，迭代之后元素也可以被销毁，因此迭代器在处理大量数据甚至无限数据时具有加载数据快、占用内存小等优势。

# 5.创建迭代器：
#
# （1）使用内建的工厂函数iter(iterable[, sentinel])
#
# iter()函数只传入一个参数时，参数必须为可迭代对象；当使用第二个参数sentinel(哨兵)时，第一个参数必须是一个可调用对象。
#
# 当有第二个参数sentinel传入时，参数iterable应是一个可调用对象，这时候迭代器它会重复地调用第一个参数，当枚举到的值等于哨兵时，就会抛出异常StopIteration。

iterator = iter([1, 2, 3, 4, 5])
print(f"{type(iterator)} {iterator}")
print(*iterator)

s = "abcdefgh"
iter1 = iter(s)
print(f"{isinstance(iter1, Iterator)} {iter1} {iter1}")  # True


# 使用第二个参数的情况此处不描述了

# 2.生成器函数
#
# 在 Python 中，使用了(一个或多个)yield语句的函数，就叫做生成器函数。
#
# 解释器处理这种函数定义的时候将创建特殊的生成器函数对象，而不是普通的函数对象。调用生成器函数的时候，返回值就是一个生成器对象。它只能用于迭代操作，更简单点理解生成器就是一种迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
#
# 实例：
# 实现的斐波那契数列
def fib_gen(n):
    f0, f1 = 0, 1
    for n in range(n):
        yield f0
        f0, f1 = f1, f0 + f1


print(fib_gen(5))  # <generator object fib_gen at 0x0000023A5BB78830>

g = fib_gen(6)  # g就是一个生成器对象（也是一种迭代器）
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 1
print(next(g))  # 2

# 生成器是包含有__iter__()和__next__()方法的，所以可以直接使用for来迭代
for x in fib_gen(5):
    print(x)


# 0, 1, 1, 2, 3,

# yield from语法
# yield from 是在Python3.3才出现的语法。所以这个特性在Python2中是没有的。
# yield from 后面需要加的是可迭代对象，它可以是普通的可迭代对象，也可以是迭代器，甚至是生成器。
# yield from 主要用于生成器的嵌套，重点是帮我们自动处理内外层之间的异常问题。

# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total / count


# 委托生成器 委托生成器的作用是：在调用方与子生成器之间建立一个双向通道。
def proxy_gen():
    while True:
        yield from average_gen()


# 调用方
def main():
    calc_average = proxy_gen()
    print(calc_average)
    next(calc_average)  # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0
    print(calc_average.send(30))  # 打印：22.0
    print(calc_average.send(30))  # 打印：24.0
    print(calc_average.send(30))  # 打印：25.0


if __name__ == '__main__':
    main()
