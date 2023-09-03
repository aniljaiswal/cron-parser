def get_range_values(range_str):
        start, end = map(int, range_str.split("-"))
        return list(range(start, end + 1))


def get_step_values(step_str, min_value, max_value):
    values = []
    step = int(step_str)
    for value in range(min_value, max_value + 1):
        if (value - min_value) % step == 0:
            values.append(value)
    return values
