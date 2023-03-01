def draw_board(edge):
    e = '+-------'
    s = e*edge + '+\n'
    for i in range(edge):
        s += '|' + '       |'*edge + '\n|'
        for j in range(edge):
            s += f' ({i},{j}) |'
        s += '\n|' + '       |'*edge + '\n'
        s += e*edge + '+\n'
    return s

def main():
    print(draw_board(5))

if __name__ == "__main__":
    main()