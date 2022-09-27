def get_min_avg_max(numbers):
    numbers_tuple = tuple(numbers)
    max_value = max(numbers_tuple)
    min_value = min(numbers_tuple)
    avg_value = 0 if len(numbers_tuple) == 0 else sum(
        numbers_tuple)/len(numbers_tuple)
    return max_value, min_value, avg_value


print(get_min_avg_max([2, 5, 7, 3, 6]))
