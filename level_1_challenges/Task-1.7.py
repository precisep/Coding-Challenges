def merge_list_alternatively(list_1,list_2):

    merge = list(zip(list_1,list_2))

    return print([x for y in merge for x in y])

merge_list_alternatively([11,22,33],[1,2,3])