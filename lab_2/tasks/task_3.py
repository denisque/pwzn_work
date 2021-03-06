## Wypisac unikatowe wartosci z listy, znajdzi wartosci unikatowe ale zwrocic w kolejnosci = zapamietac kolejnosc wprowadzenia

def unique(values):
    """
    Funkcja zwraca listę unikatowych wartości.
    Utrudnienie: Funkcja zwraca unikatowe wartości w kolejności wystąpienia.

    :param values: List of values to check.
    :type values: list
    :return: Unique values in order of appear.
    :rtype: list
    """
    uniq = set(values)
    out = []
    for i in values:
        if i in uniq:
            out.append(i)
            uniq.remove(i)
    print(out)
    return out


if __name__ == "__main__":
    assert [1, 5, 3, 6, 7, 2, 4] == unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5])