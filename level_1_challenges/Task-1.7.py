def merge_list_alternatively(list_1,list_2):

    merge = list(zip(list_1,list_2))

    return print([x for y in merge for x in y])

