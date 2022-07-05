from typing import List


# def drill_sum(a:List):
#     if len(a) <= 2:
#
#
#     for i in range(len(a)):
#         sum_a = a[i] + sum(a[i + 1])
#         #return a
#         a.pop(0)
#         a.pop(1)
#         a.insert(sum_a, 0)
#         print(sum_a)
#     return a
#     # else:
#     #     sum_first = drill_sum([1,[1,2]])

def drill_sum(data):
    if type(data) is int:
        return data

    sum_data = 0

    for x in data:
        sum_data += drill_sum(x)
    return sum_data

def drill_sum2(data):
    if isinstance(data, int):
        return data
    elif len(data) == 0:
        return 0
    else:
        return drill_sum(data[0]) + drill_sum(data[1:])




if __name__ == '__main__':
    test_data1 = [
        1,
        [1, 2],
        [1, [2, 3]],
        [1, [2, [3, 4]]],
        [1, [2, [3, [4, 5]]]],
    ]
    test_data2 = [
        [1, [[2, 6], [3, 4]]],
        [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
        [1, [2, 3]],
        [1, 2],
        1,
    ]
    print(drill_sum(test_data1))
    print(drill_sum(test_data2))
    print(drill_sum2(test_data1))
    print(drill_sum2(test_data2))
