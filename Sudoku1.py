with open("puzzle1.sudoku") as f:
    rowstring = []
    for line in f.read().split():
        rowstring.append(line.split(','))
    print rowstring

