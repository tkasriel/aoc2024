from typing import Any, Callable
from utils import *
class Tape:
    def __init__(self, filepath: str) -> None:
        self.regs: list[int] = []
        self.program: list[int] = []
        self._out: list[int] = []
        self.pointer: int = 0
        with open(filepath, "r") as file:
            lines = file.read().split("\n")
            for i in range(3):
                self.regs.append(nums(lines[i])[0])
            self.program = digits(lines[4])

    def run(self) -> list[int]:
        while self.pointer < len(self.program):
            op = self.getop(self.program[self.pointer])
            self.pointer = op(self.program[self.pointer+1])
        return self._out

    def printProgram(self) -> None:
        for i in range(0,len(self.program), 2):
            print(self.getop(self.program[i]).__name__, self.program[i+1])
    
    def evalCombo(self, combo: int) -> int:
        if combo <= 3:
            return combo
        if combo == 7:
            raise ValueError("Invalid code")
        return self.regs[combo - 4]

    def adv(self, combo: int) -> int:
        self.regs[0] = self.regs[0] // (2 ** self.evalCombo(combo))
        return self.pointer + 2
    
    def bxl(self, literal: int) -> int:
        self.regs[1] = self.regs[1] ^ literal
        return self.pointer + 2
    
    def bst(self, combo: int) -> int:
        self.regs[1] = self.evalCombo(combo) % 8
        return self.pointer + 2
    
    def jnz(self, literal: int) -> int:
        return (self.pointer + 2 if self.regs[0] == 0 else literal)

    def bxc(self, _: int) -> int:
        self.regs[1] = self.regs[1] ^ self.regs[2]
        return self.pointer + 2
    
    def out(self, combo: int) -> int:
        self._out.append(self.evalCombo(combo) % 8)
        return self.pointer + 2

    def bdv(self, combo: int) -> int:
        self.regs[1] = self.regs[0] // (2 ** self.evalCombo(combo))
        return self.pointer + 2
    
    def cdv(self, combo: int) -> int:
        self.regs[2] = self.regs[0] // (2 ** self.evalCombo(combo))
        return self.pointer + 2

    def getop(self, opcode: int) -> Callable[[int], int]:
        funcs: list[Callable[[int],int]] = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
        return funcs[opcode]


def part2():
    # This is where I die
    check = [2,4,1,3,7,5,1,5,0,3,4,1,5,5,3,0]
    check.reverse()
    possA = [0]
    # poss_read = [[]]
    # poss_read_curr = []
    poss_curr = []
    B = 0
    C = 0
    for i in range(16):
        poss_curr = []
        # poss_read_curr = []
        for j, A in enumerate(possA):
            for a_poss in range(8):
                # ((a_poss ^ 3) ^ 5) ^ ((A*8+a_poss) // (2**(a_poss ^ 3)))
                if (((a_poss ^ 5) ^ 3) ^ ((A * 8 + a_poss) // (2**(a_poss^3)))) % 8 == check[i]:
                    # print(a_poss)
                    poss_curr.append(A * 8 + a_poss)
                    # poss_read_curr.append(poss_read[j] + [a_poss])
                    # print(poss_read_curr[-1])
                    # print(poss_curr)
                    # A = A * 8 + a_poss
        if len(poss_curr) == 0:
            print(possA)
        possA = poss_curr[:]
        # poss_read = poss_read_curr[:]
    

    print(possA[0])
    # counter = 0
    # currA = A
    # while currA > 0:
    #     currA //= 8
    #     counter += 1
    # print(counter)
    # print(A)

    # B = (((A % 8) ^ 3) ^ 5) ^ (A // 2**((A % 8) ^ 3))
    # C := (A // 2**((A % 8) ^ 3))




if __name__ == "__main__":
    tape = Tape("p17.txt")
    print(",".join(map(str, tape.run())))
    print(tape.regs)
    print("===== Part 2 =====")
    part2()