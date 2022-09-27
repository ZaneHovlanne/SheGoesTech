def get_common_elements(seq1, seq2, seq3):
    seq1_set = set(seq1)
    seq2_set = set(seq2)
    seq3_set = set(seq3)
    result = set(seq1_set & seq2_set & seq3_set)
    tuple_result = tuple(result)
    return tuple_result


print(get_common_elements("abc", ['a', 'b'], ('b', 'd')))
