def import_data():
    with open("inputs/day4.csv") as file:
        lines = file.read()
    lines = lines.rstrip().split("\n\n")
    return lines


def process_data(data):
    data = [w.replace("  ", " ") for w in data]
    nums_to_draw = [num for num in data[0].split(",")]
    board_lines = [board.split("\n") for board in data[1:]]
    boards = [[line.lstrip().split(" ") for line in board] for board in board_lines]
    return nums_to_draw, boards


def part_1():
    data = import_data()
    nums_to_draw, boards = process_data(data)
    drawn = [
        [[0 for num in range(len(boards[0][0]))] for line in range(len(boards[0]))]
        for board in range(len(boards))
    ]
    # print(drawn)
    winner_board = None
    for drawn_number in nums_to_draw:
        print("number drawn")
        print(drawn_number)
        for board_idx, board in enumerate(boards):
            # draw the number
            for line_idx, line in enumerate(board):
                for num_idx, num in enumerate(line):
                    if num == drawn_number:
                        drawn[board_idx][line_idx][num_idx] = 1

            # print(board)
            # print(drawn)
            # check if board won (assuming one board wins at a time)
            # checking rows
            for row in range(len(board)):
                # print([row_element for row_element in drawn[board_idx][row]])
                if all([row_element == 1 for row_element in drawn[board_idx][row]]):
                    winner_board = board_idx
            # checking colums
            for col in range(len(board[0])):
                if all(
                    [
                        col_element == 1
                        for col_element in [
                            drawn[board_idx][row][col] for row in range(len(board))
                        ]
                    ]
                ):
                    winner_board = board_idx
        if winner_board:
            print(winner_board)
            break

    # print(winner_board)
    marked_nums = [
        int(boards[winner_board][line_idx][num_idx])
        for num_idx in range(len(line))
        for line_idx in range(len(boards[winner_board]))
        if drawn[winner_board][line_idx][num_idx] == 0
    ]

    return sum(marked_nums) * int(drawn_number)


def part_2():
    data = import_data()
    winner_board = None
    nums_to_draw, boards = process_data(data)
    drawn = [
        [[0 for num in range(len(boards[0][0]))] for line in range(len(boards[0]))]
        for board in range(len(boards))
    ]
    not_won_board = list(range(len(boards)))
    for drawn_number in nums_to_draw:
        print("number drawn")
        print(drawn_number)
        if len(not_won_board) != 1:
            for board_idx, board in enumerate(boards):
                if board_idx in not_won_board:
                    # draw the number
                    for line_idx, line in enumerate(board):
                        for num_idx, num in enumerate(line):
                            if num == drawn_number:
                                drawn[board_idx][line_idx][num_idx] = 1

                    # check if board won (assuming one board wins at a time)
                    # checking rows
                    for row in range(len(board)):
                        # print([row_element for row_element in drawn[board_idx][row]])
                        if all(
                            [row_element == 1 for row_element in drawn[board_idx][row]]
                        ):
                            not_won_board.remove(board_idx)
                    # checking colums
                    for col in range(len(board[0])):
                        if all(
                            [
                                col_element == 1
                                for col_element in [
                                    drawn[board_idx][row][col]
                                    for row in range(len(board))
                                ]
                            ]
                        ):
                            if board_idx in not_won_board:
                                not_won_board.remove(board_idx)
        if len(not_won_board) == 1:
            board_idx = not_won_board[0]
            board = boards[not_won_board[0]]
            print(not_won_board[0])
            for line_idx, line in enumerate(board):
                for num_idx, num in enumerate(line):
                    if num == drawn_number:
                        drawn[board_idx][line_idx][num_idx] = 1

                # check if board won (assuming one board wins at a time)
                # checking rows
                for row in range(len(board)):
                    # print([row_element for row_element in drawn[board_idx][row]])
                    if all([row_element == 1 for row_element in drawn[board_idx][row]]):
                        winner_board = board_idx
                # checking colums
                for col in range(len(board[0])):
                    if all(
                        [
                            col_element == 1
                            for col_element in [
                                drawn[board_idx][row][col] for row in range(len(board))
                            ]
                        ]
                    ):
                        if board_idx in not_won_board:
                            winner_board = board_idx
            if winner_board:
                break

    # print(winner_board)
    marked_nums = [
        int(boards[not_won_board[0]][line_idx][num_idx])
        for num_idx in range(len(line))
        for line_idx in range(len(boards[not_won_board[0]]))
        if drawn[not_won_board[0]][line_idx][num_idx] == 0
    ]

    return sum(marked_nums) * int(drawn_number)


if __name__ == "__main__":

    # solution1 = part_1()
    # print(solution1)
    solution2 = part_2()
    print(solution2)
