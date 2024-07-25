"""
The program has four “registers” of memory that can only hold integer numbers and have 
the names A, B, C, and D. 
It also has 2048 addresses of simulated RAM memory which can be 
accessed via their address between 0 and 2048

It understands the following instructions related to memory:

• LOADA <MEM> <ADDR>: Load the value at memory address ADDR into register MEM.
• LOAD <MEM>: Execute LOADA, using the value in register A as address ADDR.
• LOADI <MEM> <VALUE>: Sets MEM to the given value.
• STOREA <MEM> <ADDR>: Store the value contained in register MEM at memory address ADDR. 
• STORE <MEM>: Execute STOREA, using the value in register A as address ADDR.
Attempting to access an address not between 0 (inclusive) and 2048 (exclusive) is considered an error. 
Moreover, some basic mathematics are supported:
• MOVE <MEM1> <MEM2>: Copies the value of MEM2 to MEM1.
• ADDI <MEM> <VALUE>: Add VALUE to MEM and store the result in MEM.
• ADD <MEM1> <MEM2>: Add the value in MEM2 to MEM1 and store the result in MEM1.
• SUB <MEM1> <MEM2>: As above, with subtraction.
• MUL <MEM1> <MEM2>: As above, with multiplication.
• DIV <MEM1> <MEM2>: As above, with (integer) division. Division by zero is considered an error.

Whenever it encounters a nonsensical situation, it simply replies “I’m afraid I can’t do that” and 
stops, ignoring all further instructions.

Attempting to set any memory register to a value outside of its supported range of −2^42 and 2^42 is 
considered an error. Attempting to write to P or X is considered an error.

Also, it is able to do some (conditional) skips:
• JMP <STEPS>: Skip over the next STEPS instructions. If STEPS is negative, go back this many steps. 
This also modifies P. Explanation: This means that JMP 0 is a “no-op” (it skips zero instructions) 
and JMP -1 is an infinite loop.
• JMPR <MEM>: Perform a JMP where STEPS equals the value of MEM.
• JZ <MEM> <STEPS>: If the value of MEM is zero, perform JMP STEPS.
• JLT <MEM1> <MEM2> <STEPS>: If the value of MEM1 is less than the value of MEM2, perform JMP STEPS.

The end of the program is indicated by END.

Example input:
LOADI C 1 
PRINT C
ADD A C 
LOADI B 100 
JLT A B -3 
PRINT A 
LOADI C 1 
ADD A C 
JMP -1 
PRINT A 
END

Example output:
1
100
I'm afraid I can't do that
"""

class Assembler:
    def __init__(self):
        self.memory = [0] * 2048
        self.cells = {"A": 0, "B": 0, "C": 0, "D": 0, "P": 0, "X": 0}

    def increment_X(self):
        self.cells["X"] += 1

    def call_function(self, instruction):
        if not instruction:
            exit()
        command, *args = instruction.split()
        method = getattr(self, command, None)
        if method is None or not callable(method):
            print("I'm afraid I can't do that")
            exit()
        try:
            method(*args)
        except TypeError:
            print("I'm afraid I can't do that")
            exit()
        self.increment_X()

    def LOADA(self, mem, addr):
        addr = int(addr)
        if addr < 0 or addr >= len(self.memory) or mem == "X" or mem == "P":
            print("I'm afraid I can't do that")
            exit()
        self.cells[mem] = self.memory[addr]

    def LOAD(self, mem):
        addr = self.cells["A"]
        self.LOADA(mem, addr)

    def LOADI(self, mem, value):
        value = int(value)
        if value < -(2**42) or value > 2**42 or mem == "X" or mem == "P":
            print("I'm afraid I can't do that")
            exit()
        self.cells[mem] = value

    def STOREA(self, mem, addr):
        addr = int(addr)
        if addr < 0 or addr >= len(self.memory):
            print("I'm afraid I can't do that")
            exit()
        self.memory[addr] = self.cells[mem]

    def STORE(self, mem):
        addr = self.cells["A"]
        self.STOREA(mem, addr)

    def MOVE(self, mem1, mem2):
        self.cells[mem1] = self.cells[mem2]

    def ADDI(self, mem, value):
        value = int(value)
        if self.cells[mem] + value < -(2**42) or self.cells[mem] + value > 2**42:
            print("I'm afraid I can't do that")
            exit()
        self.cells[mem] += value

    def ADD(self, mem1, mem2):
        self.cells[mem1] += self.cells[mem2]

    def SUB(self, mem1, mem2):
        self.cells[mem1] -= self.cells[mem2]

    def MUL(self, mem1, mem2):
        self.cells[mem1] *= self.cells[mem2]

    def DIV(self, mem1, mem2):
        divisor = self.cells[mem2]
        if divisor == 0:
            print("I'm afraid I can't do that")
            exit()
        self.cells[mem1] //= divisor

    def JMP(self, steps):
        steps = int(steps)
        if steps == -1:
            print("I'm afraid I can't do that")
            exit()
        self.cells["P"] += steps
        if self.cells["P"] < 0:
            print("I'm afraid I can't do that")
            exit()

    def JMPR(self, mem):
        steps = self.cells[mem]
        self.JMP(steps)

    def JZ(self, mem, steps):
        if self.cells[mem] == 0:
            self.JMP(steps)

    def JLT(self, mem1, mem2, steps):
        if self.cells[mem1] < self.cells[mem2]:
            self.JMP(steps)

    def PRINT(self, mem):
        print(self.cells[mem])

    def main(self):
        program = []

        while True:
            line = input()
            if line == "END":
                break
            program.append(line)
        self.cells["P"] = 0

        while self.cells["P"] < len(program):
            self.call_function(program[self.cells["P"]])
            self.cells["P"] += 1
        else:
            if self.cells["X"] > 10**6:
                print("I'm afraid I can't do that")
                exit()

if __name__ == "__main__":
    assembler = Assembler()
    assembler.main()