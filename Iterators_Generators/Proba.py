class FlatIterator:

    def __init__(self, list_iter):
        self.list_of_lists = list_iter
        self.count = count1
        self.count2 = 0
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
        print(self.outer_list_cursor, self.inner_list_cursor)
            # то переходи на следующий список увеличив outer_list_cursor
            # и обнуляем inner_list_cursor
        if self.outer_list_cursor == len(self.list_of_lists):
            raise StopIteration

        return self.list_of_lists[self.outer_list_cursor][self.inner_list_cursor]

if __name__ == '__main__':
    list_of_lists_1 = [
                ['a', 'b', 'c'],
                ['d', 'e', 'f', 'h', False],
                [1, 2, None]]
    count1 = len(list_of_lists_1)
    list_iter_instance = FlatIterator(list_of_lists_1)
    # for z in list_iter_instance:
    #     for x in z:
    #         print(x)
    for z in list_iter_instance:
        print(z)