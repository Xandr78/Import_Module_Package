'''Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и
возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.'''
class FlatIterator:

    def __init__(self, list_iter):
        self.list_iter = list_iter
        self.count = count1
        self.count2 = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count == self.count2:
            raise StopIteration
        else:
            res = self.list_iter[self.count2]
            self.count2 += 1
            return res

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    list_of_lists_1 = [
                ['a', 'b', 'c'],
                ['d', 'e', 'f', 'h', False],
                [1, 2, None]]
    count1 = len(list_of_lists_1)
    list_iter_instance = FlatIterator(list_of_lists_1)
    for z in list_iter_instance:
        for x in z:
            print(x)
    test_1()

# A = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# print(len(sum(A,[])))
# list_of_list = [[1,2,3],[4,5,6],['a','b','c']]
# count1 = 0
# for i in range(len(list_of_list)):
#     for j in list_of_list[i]:
#         count1 += 1
# print(count1)