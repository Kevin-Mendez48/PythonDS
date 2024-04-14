def compact(lst):
    compacted_list = []
    for item in lst:
        if item:
            compacted_list.append(item)
    return compacted_list
"""Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
