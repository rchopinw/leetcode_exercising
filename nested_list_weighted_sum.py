# LC 339: Nested list weight sum
def depth_sum(nested_list):
    s = 0
    depth = 1
    while nested_list:
        new_list = []
        for element in nested_list:
            if element.getInteger() is not None:
                s += depth * element.getInteger()
            elif element.getList() is not None:
                new_list += element.getList()
        depth += 1
        nested_list = new_list
    return s
