class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_in_list = iter(self.list_of_list)
        self.next_list = iter(next(self.list_in_list))
        return self

    def __next__(self):
        try:
            el = next(self.next_list)
        except StopIteration:
            nxt_l = next(self.list_in_list)
            try:
                self.next_list = iter(nxt_l)
            except StopIteration:
                if nxt_l:
                    raise StopIteration
            el = next(self.next_list)
        return el


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
    test_1()