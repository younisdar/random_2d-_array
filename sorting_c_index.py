def sort_2d_list(R_list, columnIndex):
    R_list.sort(key=lambda x: x[columnIndex])
    return R_list
