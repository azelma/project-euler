def spiral_corners(dim):
    corner_numbers = []
    corner_numbers.append(dim * dim)
    for i in range(3):
        corner_numbers.append(corner_numbers[-1] - (dim - 1))
    return corner_numbers

def spiral_diagonals(dim):
    diagonal_numbers = []
    while dim > 1:
        diagonal_numbers = diagonal_numbers + spiral_corners(dim)
        dim = dim - 2
    diagonal_numbers.append(1)
    return diagonal_numbers

print sum(spiral_diagonals(1001))