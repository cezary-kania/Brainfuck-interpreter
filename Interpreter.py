#import getch
class Interpreter:
    
    def __init__(self, view):
        self.view = view
        self.memorySize = 8
        self.memoryArray = [0]*self.memorySize
        self.memoryPointer = 0
        self.loopStack = []
        self.codePointer = 0
    def ClearMemory(self):
        self.memoryArray = [0]*self.memorySize
    def GetMemorySize(self):
        return self.memorySize
    def SetMemorySize(self, newSize):
        self.memorySize = newSize
    def MemoryToString(self):
        m_str = []
        m_str.append('[')
        f_item = True
        for cell in self.memoryArray:
            if f_item == True:
                m_str.append(str(cell))
                f_item = False
            else:
                m_str.append(f', {cell}')
        m_str.append(']')
        return ''.join(m_str)
    def IncrementCell(self):
        self.memoryArray[self.memoryPointer] += 1
    def DecrmentCell(self):
        self.memoryArray[self.memoryPointer] -= 1
    def PointerToLeft(self):
        if(self.memoryPointer > 0):
            self.memoryPointer -= 1
        else:
            raise Exception('Out of memory')
    def PointerToRight(self):
        self.memoryPointer += 1
        if self.memoryPointer > len(self.memoryArray) - 1:
            self.memorySize += 1
            self.memoryArray.append(0)
    def StartLoop(self):
        self.loopStack.append(self.codePointer)
    def EndLoop(self):
        if self.memoryArray[self.memoryPointer] == 0: return
        if len(self.loopStack) <= 0: raise Exception('Invalid instruction')
        self.codePointer = self.loopStack.pop() - 1
    def InputChar(self):
        #self.memoryArray[self.memoryPointer] = ord(getch.getch())
        pass
    def GetAscii(self):
        #return chr(self.memoryArray[self.memoryPointer])
        c = chr(self.memoryArray[self.memoryPointer])
        self.view.fetchAscii(c)
    @staticmethod
    def ParseString(raw_str):
        return ''.join([c for c in raw_str if c in ['+', '-', '>', '<', '.', ']', '[']])
    def Run(self, code : str):
        while self.codePointer < len(code):
            {
                '+' : self.IncrementCell,
                '-' : self.DecrmentCell,
                '>' : self.PointerToRight,
                '<' : self.PointerToLeft,
                '.' : self.GetAscii,
                '[' : self.StartLoop,
                ']' : self.EndLoop
            }[code[self.codePointer]]()
            self.codePointer += 1
            

    