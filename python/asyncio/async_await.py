# -*- coding: utf-8 -*-


def coro1():
    print("C1: Start")
    print("C1: Stop")


def coro2():
    print("C2: Start")
    print("C2: a")
    print("C2: b")
    print("C2: c")
    print("C2: Stop")


# 通过新的 async 关键字的魔法, 这些函数不再是函数了,
# 现在它们变成了协程(更准确的说是本地协程函数).
# 普通函数被调用的时候, 函数体会被执行, 但是在调用协程函数的时候, 函数体并不会被执行, 你得到的是一个协程对象

async def coro1():
    print("C1: Start")
    print("C1: Stop")


async def coro2():
    print("C2: Start")
    print("C2: a")
    print("C2: b")
    print("C2: c")
    print("C2: Stop")


c1 = coro1()
c2 = coro2()
print(c1, c2)

# 执行协程的一种方式是使用 await 表达式
# 不过, await 表达式只有在本地协程函数里才是有效的. 你必须这样做:
async def main():
    await c1

# 可以通过调用 send 方法来启动一个协程的执行.
c1.send(None)

# StopIteration 异常是一种标记生成器（或者像这里的协程）执行结束的机制
try:
    c1.send(None)
except StopIteration:
    pass

try:
    c2.send(None)
except StopIteration:
    pass

# 基于生成器的协程对象
# 基本上一个 Python 的生成器(有yield表达式的函数)可以通过 types.coroutine 装饰被标记成一个协程.
@types.coroutine
def switch():
    yield


async def coro1():
    print("C1: Start")
    await switch()
    print("C1: Stop")


def run(coros):
    coros = list(coros)

    while coros:
        # Duplicate list for iteration so we can remove from original list.
        for coro in list(coros):
            try:
                coro.send(None)
            except StopIteration:
                coros.remove(coro)

c1 = coro1()
c2 = coro2()
run([c1, c2])
