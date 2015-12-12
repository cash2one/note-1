#!/usr/bin/env python
# -*- coding: utf-8 -*-
#简单工厂


class Operation(object):
    def __init__(self):
        self.numberA = 0
        self.numberB = 0

    def getResult(self):
        result = 0
        return result

class OperationAdd(Operation):
    def getResult(self):
        result = self.numberA + self.numberB
        return result

class OperationSub(Operation):
    def getResult(self):
        result = self.numberA - self.numberB
        return result

class OperationMul(Operation):
    def getResult(self):
        result = self.numberA * self.numberB
        return result

class OperationDiv(Operation):
    def getResult(self):
        if (self.numberB ==0):
            raise Exception("除数不能为0")
        result = self.numberA / self.numberB
        return result


class OperationFactory(object):
    def createOperate(self, operate):
        dictOperate = {"+" : OperationAdd,
                       "-" : OperationSub,
                       "*" : OperationMul,
                       "/" : OperationDiv}

        return dictOperate[operate]()


def main():
    operation = OperationFactory().createOperate("+")
    operation.numberA = 2
    operation.numberB = 3
    print operation.getResult()

main()




















