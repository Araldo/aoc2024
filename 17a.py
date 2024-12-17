from collections import defaultdict
from dataclasses import dataclass
import math
import time
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import deepcopy
from itertools import combinations, zip_longest, product
from functools import cache
import re

DAY = 17
get_input(DAY)
input = parse_input_simple(DAY)

a = int(re.findall(r"\d+", input[0])[0])
b = int(re.findall(r"\d+", input[1])[0])
c = int(re.findall(r"\d+", input[2])[0])
prog = [int(c) for c in re.findall(r"[\d,]+", input[4])[0].split(',')]

class Instructions:
    def run(self, program, a,b,c):
        self.output = []
        self.a = a
        self.b = b
        self.c = c
        pointer = 0
        while pointer < len(prog):
            opcode = prog[pointer]
            operand = prog[pointer+1]
            jump = False
            match opcode:
                case 0: self.div(operand, "a")
                case 1: self.bxl(operand)
                case 2: self.bst(operand)
                case 3: jump = True if self.a else False
                case 4: self.bxc()
                case 5: self.out(operand)
                case 6: self.div(operand, "b")
                case 7: self.div(operand, "c")
                        
            if not jump:
                pointer += 2
            else:
                pointer = operand
        print(','.join(str(c) for c in self.output))

    def combo(self, operand):
        match operand:
            case operand if operand <= 3: exp = operand
            case 4: exp = self.a
            case 5: exp = self.b
            case 6: exp = self.c
        return exp

    def bxl(self, operand):
        self.b = self.b ^ operand

    def bst(self, operand):
        self.b = self.combo(operand) % 8

    def bxc(self):
        self.b = self.b ^ self.c

    def out(self, operand):
        self.output.append(self.combo(operand) % 8)

    def div(self, operand, target):
        numerator = self.a
        denominator = math.pow(2, self.combo(operand))
        res = int(numerator/denominator)
        match target:
            case 'a': self.a = res
            case 'b': self.b = res
            case 'c': self.c = res

Instructions().run(prog,a,b,c)