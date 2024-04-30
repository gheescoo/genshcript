import argparse
import nmnparser as _nmnparser

parser = argparse.ArgumentParser(
    prog='genshcripter',
    description='Converts a numbered music notation sheet into AutoHotKey v2 file')
parser.add_argument('-i', '--input', type=str, help='Input file')
parser.add_argument('-o', '--output', type=str, help='Output file')
parser.add_argument('--tab-width', type=int, default=4, help='Tab width in spaces')
parser.add_argument('--stroke-width', type=int, default=4, help='Number of notes per stroke')
parser.add_argument('--octave-up', type=str, default='+', help='Character to indicate an octave up, default to "+"')
parser.add_argument('--octave-down', type=str, default='-', help='Character to indicate an octave down, default to "-"')
args = parser.parse_args()

nmnparser = _nmnparser.Parser(args.octave_up, args.octave_down)

with open(args.input) as f:
    while(True):
        line_octave = f.readline()
        while(line_octave == '\n' or line_octave.startswith(";")):
            line_octave = f.readline()
        if(line_octave == ''):
            break
        line_notes = f.readline()
        nmnparser.include_stave(line_octave, line_notes)

# print(nmnparser.staves)

with open(args.output, 'w') as f:
    for i in range(0, len(nmnparser.staves), args.stroke_width):
        f.write(f"{' ' * args.tab_width}stroke{tuple(nmnparser.staves[i: i + args.stroke_width])}\n")
