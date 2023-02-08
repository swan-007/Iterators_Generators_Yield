class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index_list = -1
        self.list_len = len(self.list_of_list)

    def __iter__(self):
        self.index_list += 1
        self.index_obj = 0
        return self

    def __next__(self):
        if self.index_obj == len(self.list_of_list[self.index_list]):
            iter(self)
        if self.index_list == self.list_len:
            raise StopIteration
        self.index_obj += 1
        return self.list_of_list[self.index_list][self.index_obj - 1]


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
