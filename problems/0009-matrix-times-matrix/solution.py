
def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:

    if not a or not b or len(a[0]) != len(b):
        return -1

    result = []

    for row in a:
        new_row = []

        for j in range(len(b[0])):
            total = 0

            for i in range(len(b)):
                total += row[i] * b[i][j]

            new_row.append(total)

        result.append(new_row)

    return result
