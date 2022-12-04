def ploskiy_spisok(lst1):
    a = []
    def rec(lst):
        for elem in lst:
            if type(elem) == list and elem:
                rec(elem)
            elif elem != []:
                 a.append(elem)
    rec(lst1)
    return a
