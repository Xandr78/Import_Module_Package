'''Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и
возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.'''
class FlatIterator:

    def __init__(self, list_iter):
        self.list_of_lists = list_iter
    def __iter__(self):
        self.outer_list_cursor = 0  # курсор основного списка
        self.inner_list_cursor = -1  # курсор списка вложенного в основной список

        return self
    def __next__(self):
        # увеличиваем inner_list_cursor
        self.inner_list_cursor += 1
        # if self.list_of_lists[self.outer_list_cursor][self.inner_list_cursor] is None: # если во вложенном списке элементы закончились,
        if self.inner_list_cursor == len(self.list_of_lists[self.outer_list_cursor]):
            self.outer_list_cursor += 1
            self.inner_list_cursor = 0
        # print(self.outer_list_cursor, self.inner_list_cursor)
            # то переходи на следующий список увеличив outer_list_cursor и обнуляем inner_list_cursor
        if self.outer_list_cursor == len(self.list_of_lists):
            raise StopIteration

        return self.list_of_lists[self.outer_list_cursor][self.inner_list_cursor]

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
    list_iter_instance = FlatIterator(list_of_lists_1)
    for z in list_iter_instance:
        print(z)
    test_1()

# A = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# print(len(sum(A,[])))
# list_of_list = [[1,2,3],[4,5,6],['a','b','c']]
# count1 = 0
# for i in range(len(list_of_list)):
#     for j in list_of_list[i]:
#         count1 += 1
# print(count1)