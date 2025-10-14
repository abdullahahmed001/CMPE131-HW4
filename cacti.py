#from cacti import cacti_number
def cacti_number(func):
    def wrapper(plot):
        # We want to validate the input
        if not plot or not all(isinstance(row, list) for row in plot):
            return 0
        length_of_row = len(plot[0])
        if any(len(row) != length_of_row for row in plot):
            return 0

        return func(plot)
    return wrapper

@cacti_number
def counter_for_cactus(plot):
    if not plot or not plot[0]:
        return 0

    rows, columns = len(plot), len(plot[0])
    aCount = 0
    myGrid = [row[:] for row in plot]

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for r in range(rows):
        for c in range(columns):
            if myGrid[r][c] == 0:
                canPlace = True
                for delta_row, delta_column in directions:
                    neighbor_row_index, neighbor_column_index = r + delta_row, c + delta_column
                    if 0 <= neighbor_row_index < rows and 0 <= neighbor_column_index < columns and myGrid[neighbor_row_index][neighbor_column_index] == 1:
                        canPlace = False
                        break
                if canPlace:
                    myGrid[r][c] = myGrid[r][c] + 1
                    aCount +=1

    return aCount

def main():
    plot = [
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    print(counter_for_cactus(plot))
main()

