#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# from examples import *
from opcode import OPCODE


def seasoning(source, ram: list):
    stack_pointer = 32
    stack = [None] * stack_pointer
    instruction_pointer = 0

    while True:
        working = source

        instruction = working[instruction_pointer]  # The current instruction is at the instruction pointer.
        instruction_pointer += 1  # Increase the instruction pointer (move down the list).

        if instruction in [OPCODE.HALT, "HALT"]:
            break

        # Stack Modifications:

        elif instruction in [OPCODE.PUSH, "PUSH"]:
            stack_pointer -= 1
            stack[stack_pointer] = int(working[instruction_pointer])
            instruction_pointer += 1

        # Memory Modifications:

        elif instruction in [OPCODE.MOVE, "MOVE"]:  # MOVE, 5, 10,
            move = int(working[instruction_pointer])
            instruction_pointer += 1
            to = int(working[instruction_pointer])
            instruction_pointer += 1

            ram[to] = move

        elif instruction in [OPCODE.LOAD, "LOAD"]:
            stack_index = stack[stack_pointer]
            stack[stack_pointer] = stack[stack_index]

        elif instruction in [OPCODE.STORE, "STORE"]:
            stack_index = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_index] = stack[stack_pointer]
            stack_pointer += 1

        # Stack Movement:

        elif instruction in [OPCODE.JUMP, "JUMP"]:
            instruction_pointer = working[instruction_pointer]

        # Arithmetic Operators:

        elif instruction in [OPCODE.ADD, "ADD"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] += value

        elif instruction in [OPCODE.SUB, "SUB"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] -= value

        elif instruction in [OPCODE.MUL, "MUL"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] *= value

        elif instruction in [OPCODE.DIV, "DIV"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] //= value

        elif instruction in [OPCODE.MOD, "MOD"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] %= value

        # Comparison Operations:

        elif instruction in [OPCODE.LESS, "LESS"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] = int(stack[stack_pointer] < value)

        elif instruction in [OPCODE.MORE, "MORE"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] = int(stack[stack_pointer] > value)

        elif instruction in [OPCODE.EQUAL, "EQUAL"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] = int(stack[stack_pointer] == value)

        # IO:

        elif instruction in [OPCODE.IN, "IN"]:
            buffer = b""
            if len(buffer) < 1:
                buffer += bytes(input(), "utf-8")
            stack.append(buffer[0])
            buffer = buffer[1:]

        elif instruction in [OPCODE.OUT, "OUT"]:
            print(working[instruction_pointer])

        else:
            print("'{}' is not a valid OPCODE.".format(instruction))

        print(stack)
        print(stack[stack_pointer])
        print(ram)


if __name__ == "__main__":
    # program = example_add
    # type_ = "python"

    program = "example.sasm"
    # program = "temp.sasm"
    type_ = "file"

    # program = "example.sbc"
    # type_ = "bytecode"

    memory = [0x00] * (2 ** 8)
    
    try:
        program = sys.argv[1]
        type_ = sys.argv[2]

    except IndexError:
        pass

    if type_ != "python":
        if type_ == "file":
            program = open(program).readlines()

        elif type_ == "bytecode":
            program = open(program, "rb").read()
            # print(program)

        if type_ != "bytecode":
            list_ = []

            for line in program:
                if not line.startswith(";"):
                    list_.append(line)

            program = "".join(list_)

            list_ = []
            program_split = program.split(",")

            for code in program_split:
                list_.append("".join(code.split()))

            program = list_

    seasoning(program, memory)
