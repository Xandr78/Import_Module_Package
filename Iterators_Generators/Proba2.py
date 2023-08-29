class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if self.nested_list_cursor == len(self.main_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
        if self.main_list_cursor == len(self.main_list):
            raise StopIteration

        return self.main_list[self.main_list_cursor][self.nested_list_cursor]
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