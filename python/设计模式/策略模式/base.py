#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# 策略模式(Strategy):它定义了算法家族,分别封装起来,让他们之间可以相互替换,
# 此模式让算法的变化,不会影响到使用算法的客户.
###################################################################

#抽象算法类
class Strategy(object):
    #算法实现
    def AlgorithmInterface(self):
        pass

#具体算法A
class ConcreteStrategyA(Strategy):
    #算法A实现方法
    def AlgorithmInterface(self):
        print u"算法A实现"

#具体算法B
class ConcreteStrategyB(Strategy):
    #算法B实现方法
    def AlgorithmInterface(self):
        print u"算法B实现"

#具体算法C
class ConcreteStrategyC(Strategy):
    #算法C实现方法
    def AlgorithmInterface(self):
        print u"算法C实现"


class Context(object):
    def __init__(self, strategy):
        self.strategy = strategy

    def ContextInterface(self):
        self.strategy.AlgorithmInterface()


def main():
    context = Context(ConcreteStrategyA())
    context.ContextInterface()

    context = Context(ConcreteStrategyB())
    context.ContextInterface()

    context = Context(ConcreteStrategyC())
    context.ContextInterface()

main()




