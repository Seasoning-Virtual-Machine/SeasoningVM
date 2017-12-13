#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import IntEnum
from enum import unique


@unique
class OPRAND(IntEnum):
    HALT = 0  # Stops the program.
    MOVE = 13  # Moves a value into a memory slot.
    # Stack Modifications:
    PUSH = 1  # Pushes a value onto the stack.
    # TODO: POP = auto()  # Pops a value from the stack.
    # TODO: MOVE = auto()  # Moves a value to the stack.
    LOAD = 2  # Loads a value from the stack.
    STORE = 3  # Stores a value in the stack.
    # Stack Movement:
    JUMP = 4  # Jumps to an instruction.
    JUMPLESS = 14  # Jump if less-than.
    JUMPMORE = 15  # Jump if more-than.
    # Arithmetic Operators:
    ADD = 5  # Add the values in the stack.
    SUB = 6  # Subtracts the values in the stack.
    MUL = 7  # Multiplies the values in the stack.
    DIV = 8  # Divides the values in the stack.
    MOD = 9  # Finds the remainder of a division.
    # Comparison Operators:
    COMPARE = 16  # Compares two values.
    # LESS = 10  # Determines if a value is less than another.
    # MORE = 11  # Determines if a value is more than another.
    # EQUAL = 12  # Determines if a value equals another.
    # Logical Operators:
    # TODO: AND = auto()
    # TODO: NAND = auto()
    # TODO: OR = auto()
    # TODO: XOR = auto()
    # TODO: NOT = auto()
