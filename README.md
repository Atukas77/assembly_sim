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

Whenever it encounters a nonsensical situation (syntax error, invalid instruction), it simply replies “I’m afraid I can’t do that” and 
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
