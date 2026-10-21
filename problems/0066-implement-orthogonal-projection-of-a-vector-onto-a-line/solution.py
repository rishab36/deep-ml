
def orthogonal_projection(v, L):
    dot_prod1 = 0
    for i in range(len(v)):
        dot_prod1 += v[i] * L[i]

    dot_prod2 = 0
    for i in range(len(L)):
        dot_prod2 += L[i] * L[i]

    if dot_prod2 == 0:
        return None

    coefficient = dot_prod1 / dot_prod2

    result = []
    for i in range(len(L)):
        value = coefficient * L[i]
        result.append(round(value, 3))

    return result
