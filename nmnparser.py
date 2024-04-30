
__all__ = [
    'Parser',
    'include_stave'
]

G_CLEF = "0qwertyuiop"
C_CLEF = "0asdfghjkl"
B_CLEF = "0zxcvbnm"

class Parser:
    staves = []

    def __init__(self, octave_up = '+', octave_down = '-'):
        self.octave_up = octave_up
        self.octave_down = octave_down
        return
    
    def include_stave(self, _octaves, _notation):
        _octaves = _octaves.ljust(len(_notation))
        octaves, notation = "", ""

        for i in range(len(_notation)):
            if(_notation[i].isdigit()):
                octaves += _octaves[i]
                notation += _notation[i]

        for i in range(len(notation)):
            if(notation[i] == ' '):
                continue    
            num = int(notation[i])

            if(octaves[i] == self.octave_up):
                note = G_CLEF[num]
            elif(octaves[i] == self.octave_down):
                note = B_CLEF[num]
            else:
                note = C_CLEF[num]

            if(i < len(self.staves)):
                self.staves[i] += note
            else:
                self.staves.append(note)

_inst = Parser()
include_stave = _inst.include_stave

def _test():
    pass
if __name__ == '__main__':
    _test()