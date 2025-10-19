def cacti_number(my_array):
    def wrapper():
        plot = [row[:] for row in my_array]
        numberOfOpenSpots = 0
        for i in range(0, len(plot)):
            row = plot[i]
            for j in range(0, len(row)):
                if row[j] == 0:
                    if i > 0:
                        up = plot[i - 1][j] # Check the cell at the top
                    else:
                        up = 0
                    if i < len(plot) - 1:
                        down = plot[i + 1][j] # Check the cell at the bottom
                    else:
                        down = 0
                    if j > 0:
                        left = row[j - 1] # Check the cell to the left
                    else:
                        left = 0
                    if j < len(row) - 1:
                        right = row[j + 1]
                    else:
                        right = 0
                    if up == 0 and down == 0 and left == 0 and right == 0:
                        numberOfOpenSpots += 1
                        row[j] = 1

        return numberOfOpenSpots
    return wrapper()
