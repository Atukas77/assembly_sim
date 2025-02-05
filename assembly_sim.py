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
