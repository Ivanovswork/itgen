from recursev import ploskiy_spisok


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.list_of_list = iter(ploskiy_spisok(self.list_of_list))
        return self


    def __next__(self):
        try:
            next_el = next(self.list_of_list)
        except StopIteration:
            raise StopIteration
        return next_el


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()