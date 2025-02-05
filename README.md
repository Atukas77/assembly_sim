This program simulates a pseudo-assembly language with four integer-based registers: A, B, C, and D. Additionally, it includes 2048 memory addresses (simulated RAM), which can be accessed using addresses ranging from 0 to 2047.

Cloning the repository:  
git clone https://github.com/Atukas77/assembly_sim.git  
cd assembly_sim

Supported Instructions: 

Memory Operations:  
LOADA: Loads the value from memory address ADDR into register MEM.  
LOAD: Performs LOADA, using the value in register A as ADDR.  
LOADI: Assigns the specified value directly to MEM.  
STOREA: Saves the value in register MEM to memory address ADDR.  
STORE: Executes STOREA, using the value in register A as ADDR.  
Accessing memory outside the range of 0 to 2047 results in an error.  
Arithmetic Operations:  
MOVE: Copies the value from MEM2 into MEM1.  
ADDI: Adds a given VALUE to MEM and stores the result in MEM.  
ADD: Adds the value of MEM2 to MEM1, storing the result in MEM1.  
SUB: Performs subtraction in the same manner as ADD.  
MUL: Multiplies MEM1 by MEM2 and stores the result in MEM1.  
DIV: Performs integer division (MEM1 ÷ MEM2) and stores the result in MEM1. Division by zero triggers an error.  
Error Handling:  
Any instruction with invalid syntax or unrecognized commands results in the message:  
"I'm afraid I can't do that", after which execution halts.  
Register values must remain within the range of −2^42 to 2^42, exceeding this limit is considered an error.
Writing to registers P or X is also disallowed.  
Conditional and Unconditional Jumps:  
JMP: Skips forward STEPS instructions; if STEPS is negative, execution moves backward. This also updates register P.  
Example: JMP 0 acts as a no-op, while JMP -1 creates an infinite loop.  
JMPR: Performs a JMP where STEPS is determined by MEM.  
JZ: If MEM holds zero, performs JMP STEPS.  
JLT: If MEM1 is less than MEM2, executes JMP STEPS.  
Program Termination:  
Execution stops when encountering the END instruction.  

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
