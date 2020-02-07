"""
Rotate matrix by 90 degrees clockwise.
"""
import numpy as np


def rotate90(mat):
    # assume mat is an array of arrays
    # access element as mat[i][j]
    matwidth = len(mat)
    layers = range(int(np.ceil(matwidth*1.0/2)))
    for layer in layers:
        process_layer(layer, mat, matwidth)
    return mat


def process_layer(layer, mat, matwidth):
    print("Processing layer {}".format(layer))
    numgroups = matwidth - 2*layer - 1
    for group in range(numgroups):
        process_layer_grp(group, layer, mat, matwidth)


def process_layer_grp(group, layer, mat, matwidth):
    print("\tProcessing group {}".format(group))
    indices = get_indices(group, layer, matwidth)
    print("\tIndices: {}".format(indices))
    i,j = indices[3]
    tempp = mat[i][j]
    for s in range(4):
        i,j = indices[s]
        tempc = mat[i][j]
        mat[i][j] = tempp
        tempp = tempc


def get_indices(group, layer, n):
    # top, right, bottom, left
    result = list()
    result.append((layer, layer + group))
    result.append((layer + group, n - 1 - layer))
    result.append((n - 1 - layer, n - 1 - layer - group))
    result.append((n - 1 - layer - group, layer))
    return result


if __name__ == '__main__':
    mat = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

    print(mat)
    print(rotate90(mat))
