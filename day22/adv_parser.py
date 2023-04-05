import re

def safe_int(x):
    try:
        return int(x)
    except:
        return (1 if x == 'R' else -1)

def get_data(args):
    with open(args) as f:
        inp_board, inp_commands = f.read().split('\n\n')
        inp_board = inp_board.split('\n')
        max_len = max([len(row) for row in inp_board])
        for i, row in enumerate(inp_board):
            for _ in range(max_len-len(row)):
                inp_board[i] += " "

    board = [[(c if c != " " else '%') for c in row] for row in inp_board]
    commands = re.findall('\d+|[A-Z]',inp_commands)

    return (board, list(map(safe_int, commands)))
