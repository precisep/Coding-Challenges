def longest(items):

    k = len(max(items, key = len))

    longest_string = []

    for i in range(len(items)):
        if len(items[i]) == k:
            longest_string.append(items[i])
        else:
            None
        i+=1
    return print(*longest_string, sep = '\n')
        

